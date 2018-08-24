import markdowncreator


def test_markdowncreator_create_link():
    """Test that markdown links are created correctly.
    """
    # Setup
    link = 'https://example.com/python_page'
    title = 'Example Python Page'

    # Assertion
    output = markdowncreator.create_link(title, link)
    expected = ' * [Example Python Page](https://example.com/python_page)\n'
    assert output == expected


def test_markdowncreator_create_title():
    """Test that markdown title is created correctly.
    """
    # Setup
    title = 'notes-and-links'

    # Assertion
    output = markdowncreator.create_title(title)
    expected = '# notes-and-links\n'
    assert output == expected


def test_markdowncreator_create_section():
    """Test that markdown section is created correctly.
    """
    # Setup
    section = 'Python'

    # Assertion
    output = markdowncreator.create_section(section)
    expected = '## Python\n'
    assert output == expected


def test_markdowncreator_create_subsection():
    """Test that markdown sub-section is created correctly.
    """
    # Setup
    sub = 'Python Subsection'

    # Assertion
    output = markdowncreator.create_subsection(sub)
    expected = '#### Python Subsection\n'
    assert output == expected
