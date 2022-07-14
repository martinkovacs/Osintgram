# Commands list and usage
```text
- addrs           Get all registered addressed by target photos
- cache           Clear cache of the tool
- captions        Get user's photos captions
- commentdata     Get a list of all the comments on the target's posts
- comments        Get total comments of target's posts
- followers       Get target followers
- followings      Get users followed by target
- fwersemail      Get email of target followers
- fwersnumber     Get phone number of target followers
- fwerssubset     Get the list of users who follow both target1 and target2
- fwingsemail     Get email of users followed by target
- fwingsnumber    Get phone number of users followed by target
- fwingssubset    Get the list of users followed by both target1 and target2
- hashtags        Get hashtags used by target
- highlights      Download target's highlights
- info            Get target info
- likes           Get total likes of target's posts
- mediatype       Get user's posts type (photo or video)
- photodes        Get description of target's photos
- posts           Download user's posts in output folder
- propic          Download user's profile picture
- stories         Download user's stories  
- tagged          Get list of users tagged by target
- target          Set new target
- wcommented      Get a list of user who commented target's photos
- wtagged         Get a list of user who tagged target
```

### addrs
Return a list with address (GPS) tagged by target in his photos.
The list has post, address and date fields.

### cache
Clears `config/settings.json` and `config/settings_web.json`

### captions 
Return a list of all captions used by target in his photos.

### commentdata
Return a list of all the comments on the target's posts

### comments
Return the total number of comments in target's posts

### exit
Exit from Osintgram

### FILE
Can set preference to save commands output in output folder. It save output in `<target username>_<command>.txt` file.

With `FILE=y` you can enable saving in file.

With `FILE=n` you can disable saving in file.

### followers
Return a list with target followers with id, nickname and full name

### followings
Return a list with users followed by target with id, nickname and full name

### fwersemail
Return a list of emails of target followers

### fwersnumber
Return a list of phone number of target followers

### fwerssubset
Returns the list of users who follow both target1 and target2

### fwingsemail
Return a list of emails of user followed by target

### fwingsnumber
Return a list of phone number of user followed by target

### fwingssubset
Returns the list of users followed by both target1 and target2

### hashtags
Return a list with all hashtag used by target in his photos

### highlights
Downloads target's highlights. Every tray (folder) in its own directory (output/traytitle/username_highlightid.jpg)
When you run the command, script ask you how many photos you want to download. 
Type ENTER to download all photos available or type a number to choose how many photos you want download.
Order is newest folder newest highlight to oldest folder oldest highlight.

Example:
- FolderA: A1, A2, A3 (newest)
- FolderB: B1 (oldest), B2, B3

Final order: A3 A2 A1 B3 B2 B1

### info
Show target info like:
- id
- full name
- biography
- followed
- follow
- is business account?
- business category (if target has business account)
- is verified?
- business email (if available)
- HD profile picture url
- connected Facebook page (if available)
- Whats'App number (if available)
- City Name (if available)
- Address Street (if available)
- Contact phone number (if available)

### JSON
Can set preference to export commands output as JSON in output folder. It save output in `<target username>_<command>.JSON` file.

With `JSON=y` you can enable JSON exporting.

With `JSON=n` you can disable JSON exporting.

### likes
Return the total number of likes in target's posts

### list (or help)
Show all commands available.

### mediatype
Return the number of photos and video shared by target

### photodes
Return a list with the description of the content of target's photos

### posts
Download all target's posts in output folder.
When you run the command, script ask you how many posts you want to download. 
Type ENTER to download all posts available or type a number to choose how many posts you want download.
```
Run a command: posts
How many posts you want to download (default all):
```

### propic
Download target profile picture (HD if is available)

### stories
Download all target's stories in output folder.

### tagged
Return a list of users tagged by target with ID, username and full name

### target
Set new target by username

### wcommented
Return a list of users who commented target's photos sorted by number of comments

### wtagged
Return a list of users who tagged target sorted by number of photos
