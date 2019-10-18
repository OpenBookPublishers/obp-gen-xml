# obp-gen-xml
Wrapper to produce the XML editions of OBP books.

## How to run this tool
### Setup
This wrapper requires `saxonb-xslt` and `pyvenv-3.5` to be installed on your system. On Debian (or Debian-based distributions) this package can be installed via `apt-get install libsaxonb-java pyvenv-3.5`. After that, run `bash setup` to perform the setup.

### Conversion
To start the conversion, place the **epub file** and the **DOI deposit** in the `../XML-last` folder; finally run `bash run`.

### Clean-up
Running `bash clean` would remove temporary files from `XML-last/` (untracked files and folders). The script asks for the user's confirmation before removing the files, but if you are running this as part of a script you might want to use the`-y` flag to bypass the confirmation. 

## DEV
This suite of scripts works as expected, but the introduction of `tailor_book_transform.py` is to be regarded as a _temporary patch_.

The stylesheet `Transform-to-XML-book.xsl` merges together XML files of the book sections. The stylesheet contains a list of possible filenames, and it performs tentative _includes_ on each of them. This works fine with the XML parser embedded in Oxygen, but the (apparently less tolerant) XML parser that `saxonb-xslt` uses fails at the first occurrence of a missing file.

`tailor_book_transform.py` creates a temporary and simplified version of `Transform-to-XML-book.xsl` which lists only the successful includes.

There are a number of possible solutions, including (a) forcing `saxonb-xslt` to use a different XML parser and (b) re-write the `Transform-to-XML-book.xsl` to make its includes more precise.
