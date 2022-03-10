## shutil

Calling `shutil.copy`(source, destination) will copy the file at the path
source to the folder at the path destination.

Calling `shutil.move`(source, destination) will move the file or folder at the path
source to the path destination and will return a string of the absolute path of
the new location.

Calling `os.unlink`(path) will delete the file at path.

Calling `os.rmdir`(path) will delete the folder at path. This folder must be
empty of any files or folders.

Calling `shutil.rmtree`(path) will remove the folder at path, and all files
and folders it contains will also be deleted.

## send2trash

Using **send2trash** is much safer than Python’s regular delete functions,
because it will send folders and files to your computer’s trash or recycle bin
instead of permanently deleting them. If a bug in your program deletes
something with send2trash you didn’t intend to delete, you can later restore
it from the recycle bin.

    use the send2trash.send2trash() function to delete files and folders.
    
    Note that the send2trash() function can only send files to the recycle bin; it cannot pull files out of it.

You can use `os.walk`() in a for loop statement to walk a directory
tree, much like how you can use the range() function to walk over a range of numbers.
    A string of the current folder’s name
    A list of strings of the folders in the current folder
    A list of strings of the files in the current folder

## zipfile
```py
import zipfile
# read; by default opens in read mode
zip_file=zipfile.ZipFile('zip-file.zip')
# to get contents
zip_file.namelist()
# to ge file info
zip_file.getinfo('file-name')
# to open in write mode; to create new zip files
zip_file=zipfile.ZipFile('new-zip-file.zip','w')
# add a new file; it will overwrite
zip_file.write('file',compress_type=zipfile.ZIP_DEFLATED)
# to append new files in existing zip file
zip_file=zipfile.ZipFile('zip-file.zip','a')
# extract a file; by default extracts in same folder if second argument is missing
zip_file.extract('file-to-extract','to-where')
# to extract all
zip_file.extractall()
```