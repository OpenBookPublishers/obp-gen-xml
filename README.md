# obp-gen-xml
Wrapper to produce the XML editions of OBP books.

Work in progress

## How to run this tool
### Setup
Run `bash setup` to perform the setup.

### Conversion
To start the conversion, place the **epub file** and the **DOI deposit** in the `../XML-last` folder; finally run `bash run`.

### Clean-up
Running `bash clean` would remove temporary files from `XML-last/` (untracked files and folders). The script asks for the user's confirmation before removing the files, but if you are running this as part of a script you might want to use the`-y` flag to bypass the confirmation. 

## DEV
### What works
 -  The `setup` script clones the repository.
 -  The `run` script triggers `XML-before-transformation.py` and `Transform-to-XML-section.xsl`, producing the expected output.
 -  The `clean` script does what it should.

### What doesn't work yet
 -  `Transform-to-XML-book.xsl` doesn't produce the expected output.
 -  `XML-after-transformation.py` still untested.
