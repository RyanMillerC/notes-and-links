import pytest

import markdowncreator


def test_main_missing_kwargs():
    """Verify main raises AttributeError on missing kwargs. Missing
    'title' below.
    """
    with pytest.raises(AttributeError):
        markdowncreator.main(link='https://example.com', section='Python')


def test_main_kwarg_is_set_to_none():
    """Verify main raises AttributeError on kwarg being set to
    None.
    """
    with pytest.raises(AttributeError):
        markdowncreator.main(link=None, title='Python', section='Python')
