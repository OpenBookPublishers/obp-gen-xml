import argparse
from string import Template
import os


def template_sub(file_path, args):
    '''
    Replace the placeholders with data in the file template with
    the one supplied to the function.
    '''
    with open(file_path, 'r') as in_file:
        # Create the Template object
        template = Template(in_file.read())

        # Add schema version to the metadata dictionary
        metadata = {'schema_version': args.version}

        # If --include_file was supplied an argument
        if args.include_file:
            include_statements = get_include_statements(args.include_file)

            metadata = {
                **metadata,
                **include_statements
                }

        return template.safe_substitute(metadata)

def get_include_statements(include_file):
    '''
    Check if file in include_file exists and add an entry 
    for inclusion
    '''
    include_template = '''
                <xi:include href="{}">
                    <xi:fallback/>
                </xi:include>
    '''

    statement = []
    
    with open(include_file, 'r') as in_file:
        for line in in_file:
            file_path = line.rstrip()
            if os.path.isfile(file_path):
                statement.append(include_template.format(file_path))

    return {'book_contents': ''.join(statement)}

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
    parser.add_argument('-i', '--include_file',
                        help='File path of the file containing the possible \
                              filename to include in the book document')    

    args = parser.parse_args()

    process_xslt = template_sub(args.input_file, args)
    write_output(args.output_file, process_xslt)


if __name__ == "__main__":
    run()
