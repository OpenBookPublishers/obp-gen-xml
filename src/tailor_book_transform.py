from bs4 import BeautifulSoup
import os
import argparse

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
    desc='Tailor Section Transformation'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('input_file',
                        help = 'Input section transformation xsl file')
    parser.add_argument('output_file',
                        help = 'Output section transformation xsl file')

    args = parser.parse_args()

    soup = refine_includes(args.input_file)
    write_output(args.output_file, soup)


if __name__ == "__main__":
    run()
