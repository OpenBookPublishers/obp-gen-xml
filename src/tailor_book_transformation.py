import os
import argparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def replace_version(soup, schema_version):
    """
    Find the schema URL in the xsl file and replace the version with
    the one supplied to the function.
    """
    xsl_schema = soup.find('xsl:stylesheet')['xmlns:doi']
    doi_schema = urljoin(xsl_schema, schema_version)

    soup.find('xsl:stylesheet')['xmlns:doi'] = doi_schema

    return soup


def refine_includes(file_path):
    """
    Parse all the include statements in the xsl file.
    Leave in place the successful ones, discard the ones
    which would fail.
    """
    with open(file_path, 'r') as in_file:
        soup = BeautifulSoup(in_file, 'html.parser')

        includes = soup.find_all('xi:include')
        for include in includes:
            if not os.path.isfile(include.get('href')):
                include.extract()

        return soup


def write_output(file_path, soup):
    with open(file_path, 'w+') as out_file:
        out_file.write(soup.prettify(formatter='minimal'))


def run():
    desc = 'Tailor Section Transformation'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('input_file',
                        help='Input book-transformation xsl file')
    parser.add_argument('output_file',
                        help='Output book-transformation xsl file')
    parser.add_argument('-v', '--version',
                        help='CrossRef schema version',
                        required=True)

    args = parser.parse_args()

    soup_includes = refine_includes(args.input_file)
    soup_version = replace_version(soup_includes, args.version)
    write_output(args.output_file, soup_version)


if __name__ == "__main__":
    run()
