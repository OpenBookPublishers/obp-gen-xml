import argparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def replace_version(file_path, schema_version):
    """
    Find the schema URL in the xsl file and replace the version with
    the one supplied to the function.
    """
    with open(file_path, 'r') as in_file:
        soup = BeautifulSoup(in_file, 'html.parser')

        xsl_schema = soup.find('xsl:stylesheet')['xmlns:doi']
        doi_schema = urljoin(xsl_schema, schema_version)

        soup.find('xsl:stylesheet')['xmlns:doi'] = doi_schema

        return soup

def write_output(file_path, soup):
    with open(file_path, 'w+') as out_file:
        out_file.write(soup.prettify(formatter='minimal'))

def run():
    desc='Tailor Section Transformation'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('input_file',
                        help = 'Input section transformation xsl file')
    parser.add_argument('output_file',
                        help = 'Output section transformation xsl file')
    parser.add_argument('-v', '--version',
		        help = 'CrossRef schema version',
		        required = True)

    args = parser.parse_args()

    soup = replace_version(args.input_file, args.version)
    write_output(args.output_file, soup)


if __name__ == "__main__":
    run()
