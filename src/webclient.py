import base64
import binascii
import hashlib
import random
import string
import struct
import time

from Cryptodome import Random
from Cryptodome.Cipher import AES
from instagram_web_api import Client, ClientError, ClientLoginError
from nacl.public import PublicKey, SealedBox


class WebClient(Client):
    
    # Override this function from Client
    # Otherwise it throws missing rhx_gis error
    @staticmethod
    def _extract_rhx_gis(html):
        options = string.ascii_lowercase + string.digits
        text = ''.join([random.choice(options) for _ in range(8)])
        return hashlib.md5(text.encode()).hexdigest()
    
    @staticmethod
    def _encrypt_password(key_id, pub_key, password, version=10):
        key = Random.get_random_bytes(32)
        iv = bytes([0] * 12)

        timestamp = int(time.time())

        aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
        aes.update(str(timestamp).encode('utf-8'))
        encrypted_password, cipher_tag = aes.encrypt_and_digest(password.encode('utf-8'))

        pub_key_bytes = binascii.unhexlify(pub_key)
        seal_box = SealedBox(PublicKey(pub_key_bytes))
        encrypted_key = seal_box.encrypt(key)

        encrypted = bytes([
            1,
            key_id,
            *list(struct.pack('<h', len(encrypted_key))),
            *list(encrypted_key),
            *list(cipher_tag),
            *list(encrypted_password)
        ])
        encrypted = base64.b64encode(encrypted).decode('utf-8')

        return '#PWD_INSTAGRAM:{0!s}:{1!s}:{2!s}'.format(version, timestamp, encrypted)

    def _get_encryption_data(self):
        resp = self._make_request('https://www.instagram.com/data/shared_data/')
        
        key_id = int(resp["encryption"]["key_id"])
        pub_key = resp["encryption"]["public_key"]
        version = int(resp["encryption"]["version"])
        
        return key_id, pub_key, version

    def login(self):
        if not self.username or not self.password:
            raise ClientError('No username or password')

        key_id, pub_key, version = self._get_encryption_data()
        enc_password = self._encrypt_password(key_id, pub_key, self.password, version)

        self._init_rollout_hash()
        
        params = {'username': self.username, 'enc_password': enc_password, 'queryParams': '{}'}
        login_res = self._make_request('https://www.instagram.com/accounts/login/ajax/', params=params)
        if not login_res.get('status', '') == 'ok' or not login_res.get('authenticated', ''):
            raise ClientLoginError('Unable to login')

        if self.on_login:
            on_login_callback = self.on_login
            on_login_callback(self)
        
        return login_res
