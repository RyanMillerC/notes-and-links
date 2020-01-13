# Useful *nix Commands

> A list of commands I frequently forget.

### Check Listening Ports

`lsof -i -P -n | grep LISTEN`

**NOTE:** Will only show ports that user is listening on unless running as root

### Zip a Directory

`zip -r compressed_filename.zip foldername`
