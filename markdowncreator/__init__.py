"""
markdowncreator

Add links to a Markdown file and format them appropriately

Usage:
    markdowncreator <title> <link> [<section>] [<subsection>]
    markdowncreator (-h | --help)

Options:
    -h, --help                      Show this screen.

Example:
    markdowncreator "Python Articlea" "https://example.com/python" "Python" "Modules"
"""


def create_link(title, link):
    return ' * [{}]({})\n'.format(title, link)


def create_title(title):
    return '# {}\n'.format(title)


def create_section(section):
    return '## {}\n'.format(section)


def create_subsection(sub):
    return '#### {}\n'.format(sub)


def parse(input_):
    for i in input_:
