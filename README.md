# obp-gen-xml
Wrapper to produce the XML editions of OBP books.

## How to run this tool
### Setup
This wrapper requires `saxonb-xslt` and `python3-bs4` to be installed on your system. On Debian (or Debian-based distributions) this package can be installed via

`apt-get install libsaxonb-java python3-bs4`

To perform the setup, run:

`bash setup`

The setup contains the necessary instruction to initialise the submodule.

### Conversion
To start the conversion, place the **epub file** and the **DOI deposit** in the _obp-gen-xml_ folder. Finally, run:

`bash run prefix`

where _prefix_ is the name of the book and the DOI deposit files; i.e.: `bash run Siklos-Advanced_Problems2`.

### Clean-up

`bash clean [-y]`

would remove temporary files (untracked files and folders) from the _obp-gen-xml_ folder. The script asks for the user's confirmation before removing the files, but if you are running this as part of a script you might want to use the`-y` flag to bypass the confirmation. 

## DEV
### tailor_book_transform.py
This suite of scripts works as expected, but the introduction of `tailor_book_transform.py` is to be regarded as a _temporary patch_.

The stylesheet `Transform-to-XML-book.xsl` merges together XML files of the book sections. This is performed by tentative _includes_ of possible filenames hardcoded in the spreadsheet. All this works smoothly with the XML parser embedded in Oxygen, but the (apparently less tolerant) XML parser that `saxonb-xslt` uses fails at the first occurrence of a missing file.

`tailor_book_transform.py` creates a temporary and simplified version of `Transform-to-XML-book.xsl` which lists only the successful includes.

There are a number of possible solutions, including (a) forcing `saxonb-xslt` to use a different XML parser and (b) re-write the `Transform-to-XML-book.xsl` to make its list of includes more precise.