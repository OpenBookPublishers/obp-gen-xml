from bs4 import BeautifulSoup
import os

with open('Transform-to-XML-book.xsl', 'r') as in_file:
    soup = BeautifulSoup(in_file, 'html.parser')

    includes = soup.find_all('xi:include')
    for include in includes:
        if not os.path.isfile(include.get('href')):
            include.extract()

    with open('Transform-to-XML-book_tailored.xsl', 'w') as out_file:
        out_file.write(soup.prettify(formatter='minimal'))
