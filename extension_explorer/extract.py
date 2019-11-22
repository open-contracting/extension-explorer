from yaml import safe_load


def extract_tag(fileobj, keywords, comment_tags, options):
    """
    Yields the title values in the YAML file.
    """
    data = safe_load(fileobj)
    for prefix, tags in data.items():
        for i, tag in enumerate(tags):
            yield 1, '', tag['title'], ['/{}/{}/title'.format(prefix, i)]
