from yaml import safe_load


def extract_tag(fileobj, keywords, comment_tags, options):
    """Yield the title values in the YAML file."""
    for prefix, tags in safe_load(fileobj).items():
        for i, tag in enumerate(tags):
            yield 1, '', tag['title'], [f'/{prefix}/{i}/title']
