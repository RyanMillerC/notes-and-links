"""
markdowncreator

Add links to a Markdown file and format them appropriately

Usage:
    markdowncreator <title> <link> <section> [<subsection>]
    markdowncreator (-h | --help)

Options:
    -h, --help                      Show this screen.

Example:
    markdowncreator "Python Article" "https://example.com/python" "Python" "Modules"
"""

import conlog

from docopt import docopt
from encase import Encase


def main(**kwargs):
    log = conlog.start(level='DEBUG')
    kwargs = Encase(kwargs)

    # If running from CLI
    if len(kwargs) == 0:
        args = Encase(docopt(__doc__, version=0.1))
        for key, value in args.items():
            new_key = key.strip('<>-')
            kwargs.set(new_key, value)

    # Verify required kwargs were passed
    reqs = ['title', 'link', 'section']
    for arg in reqs:
        if arg not in kwargs:
            raise AttributeError('{} was not passed'.format(arg))
        elif kwargs.get(arg) is None:
            raise AttributeError('{} is None, this should be set'.format(arg))

    log.debug('kwargs are: {}'.format(kwargs))

    # Read README.md
    with open('README.md', 'r') as stream:
        readme = stream.readlines()

    # Create Markdown strings
    md_link = create_link(kwargs.title, kwargs.link)
    md_section = create_section(kwargs.section)
    if kwargs.subsection:
        md_subsection = create_subsection(kwargs.subsection)

    # Verify md_link does not exist in file
    for line in readme:
        if line == md_link:
            log.error('This link is already in README.md')
            exit(1)

    sections = Encase()
    for index, line in enumerate(readme):
        if line[0:2] == '##':
            sections.set(line, index)

    log.info(readme)


def create_link(title, link):
    return ' * [{}]({})\n'.format(title, link)


def create_section(section):
    return '## {}\n'.format(section)


def create_subsection(sub):
    return '#### {}\n'.format(sub)


if __name__ == '__main__':
    main(link="LINK", title="TITLE", section="SECTION")
