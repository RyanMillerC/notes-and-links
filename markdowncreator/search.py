import error_handler


def search_existing_link(md_link, md_contents):
    if md_link in md_conents:
        error_hander.critical(
            ValueError,
            'Link already exists in Markdown file'
        )
