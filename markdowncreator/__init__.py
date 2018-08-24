"""Module to format markdown.
"""


def create_link(title, link):
    return ' * [{}]({})\n'.format(title, link)


def create_title(title):
    return '# {}\n'.format(title)


def create_section(section):
    return '## {}\n'.format(section)


def create_subsection(sub):
    return '#### {}\n'.format(sub)