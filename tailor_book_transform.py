from bs4 import BeautifulSoup
import os

in_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'XML-last',
                       'Transform-to-XML-book.xsl')
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'XML-last',
                        'Transform-to-XML-book_tailored.xsl')

with open(in_path, 'r') as input:
    soup = BeautifulSoup(input, 'html.parser')

    includes = soup.find_all('xi:include')
    for include in includes:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'XML-last',
                                 include.get('href'))

        if not os.path.isfile(file_path):
            include.extract()

    with open(out_path, 'w') as output:
        output.write(soup.prettify(formatter='minimal'))
