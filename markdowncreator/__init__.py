"""Module to format markdown.
"""


def create_link(title, link):
    return ' * [{}]({})\n'.format(title, link)


def create_title(title):
    return '# {}\n'.format(title)
