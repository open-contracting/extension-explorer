from yaml import load


def extract_collection(fileobj, keywords, comment_tags, options):
    """
    Yields the title and description values of a collection's YAML file.
    """
    data = load(fileobj)
    yield 1, '', data['title'], ['title']
    if data['description']:
        yield 1, '', data['description'], ['description']
