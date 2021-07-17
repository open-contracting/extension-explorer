# Pagination

Adds a links object to packages, to support pagination.

## Links

The top-level `links` object in release packages and record packages has three fields:

- `next`: A URL to the next sequential package
- `prev`: A URL to the previous sequential package

To construct the `next` and/or `prev` URLs, it is encouraged to use query string parameters like:

- `since=TIMESTAMP`, to return a page of results that are modified after the `since` timestamp, in chronological order
- `offset=NUMBER`, to return a page of results that are positioned after the `offset` number, in sequential order (for example, if the results are retrieved from a [SQL database](https://www.postgresql.org/docs/current/queries-limit.html))

It is discouraged to use `page=NUMBER` with results ordered in reverse chronology, because:

- A given page won't return the same results over time. `page=1` will return different results today, next week, and next year.
- Users can receive duplicate results while paginating. For example, if a new release is published to page 1 while users are paginating, then the result at the bottom of each page will be moved to the top of the following page.
- It is harder for users to synchronize with the API. With `since` or `offset`, users can retrieve new results by submitting the timestamp or offset of their last request. With `page`, users need to determine which results are new or old.

Reference: [HTML link types](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types), [18F API Standards](https://github.com/18F/api-standards#pagination), [Government of Canada Standards on APIs](https://www.canada.ca/en/government/system/digital-government/modern-emerging-technologies/government-canada-standards-apis.html), [Government of Ontario API Guidelines](https://github.com/ongov/API-Guidelines/blob/develop/API-Guidelines.md#implement-pagination-and-data-segmentation), [OpenActive Realtime Paged Data Exchange](https://www.openactive.io/realtime-paged-data-exchange/#overall-approach).

## Ejemplo

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

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-11-05

- Remove `links.all`.
- Remove `packageMetadata`.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2020-04-15

- Deprecate `links.all`.
- Deprecate `packageMetadata`.
