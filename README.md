# obp-gen-xml
Wrapper to produce the XML editions of OBP books.

Work in progress

## How to run this tool
Run `bash setup` to perform the setup. To start the conversion, place the epub file and the DOI deposit in the folder `../XML-last`; lastly run `bash run`.

## DEV
### What works
 -  The `setup` script clones the repository.
 -  The `run` script triggers `XML-before-transformation.py` and `Transform-to-XML-section.xsl`, producing the expected output.

### What doesn't work yet
 -  `Transform-to-XML-book.xsl` doesn't produce the expected output.
 -  `XML-after-transformation.py` still untested.
