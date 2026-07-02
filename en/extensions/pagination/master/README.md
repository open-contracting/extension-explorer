# Pagination

Adds a links object to packages, to support pagination.

## Links

The top-level `links` object in release packages and record packages has three fields:

- `next`: A URL to the next sequential package
- `prev`: A URL to the previous sequential package

For guidance on constructing the `next` and/or `prev` URLs, refer to the [OCDS documentation](https://standard.open-contracting.org/latest/en/guidance/build/hosting/#pagination).

## Example

A publisher has a large number of releases. Instead of gathering them into one release package, it segments them into multiple release packages, via an API with pagination. The `links.next` field provides the link to the next page.

```json
{
  "uri": "https://standard.open-contracting.org/examples/releases/ocds-213czf-000-00001-05-contract.json",
  "license": "http://opendatacommons.org/licenses/pddl/1.0/",
  "publicationPolicy": "https://github.com/open-contracting/sample-data/",
  "version": "1.1",
  "releases": [
    {
      "ocid": "ocds-213czf-000-00001",
      "id": "ocds-213czf-000-00001-05-contract",
      "date": "2010-05-10T10:30:00Z",
      "language": "en",
      "tag": [
        "contract"
      ],
      "initiationType": "tender"
    }
  ],
  "links": {
    "next": "https://raw.githubusercontent.com/open-contracting/api-specification/master/multiple-file-api-next/releases-2015.json"
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-11-05

- Remove `links.all`.
- Remove `packageMetadata`.

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2020-04-15

- Deprecate `links.all`.
- Deprecate `packageMetadata`.
