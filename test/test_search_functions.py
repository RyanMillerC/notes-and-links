import pytest

import markdowncreator
import utils


def test_search_existing_link():
    """Test search_existing_link functionality.
    """
    # Setup
    link = 'https://example.com/python_page'
    title = 'Example Python Page'
    md_link = markdowncreator.create_link(title, link)
    md_contents = utils.read_file_to_list('test/search/existing_link.md')

    # Assertion
    with pytest.raises(ValueError):
        markdowncreator.search_existing_link(md_link, md_contents)
