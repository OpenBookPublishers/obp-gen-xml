import argparse
from string import Template

def replace_version(file_path, schema_version):
    """
    Replace the schema version in the file template with
    the one supplied to the function.
    """
    with open(file_path, 'r') as in_file:
        template = Template(in_file.read())

        metadata = {'schema_version': schema_version}

        return template.safe_substitute(metadata)


def write_output(file_path, process_xslt):
    with open(file_path, 'w+') as out_file:
        out_file.write(process_xslt)


def run():
    desc = 'Tailor Section Transformation'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('input_file',
                        help='Input section transformation xsl file')
    parser.add_argument('output_file',
                        help='Output section transformation xsl file')
    parser.add_argument('-v', '--version',
                        help='CrossRef schema version',
                        required=True)

    args = parser.parse_args()

    process_xslt = replace_version(args.input_file, args.version)
    write_output(args.output_file, process_xslt)


if __name__ == "__main__":
    run()
