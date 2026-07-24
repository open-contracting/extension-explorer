# Sources

In many cases, an OCDS publication combines information from multiple information systems or databases. For example:

- A publisher can source information from multiple systems to author a single release.
- Different systems can be responsible for different types of contracting processes; for example, traditional procurement, framework agreements and public-private partnerships can be managed in different systems.
- Different systems can be responsible for different stages of the contracting process, published in different releases; for example, budget data from a Ministry of Finance system, and solicitation data from a Public Procurement Agency system.
- Different systems can cover different periods; for example, older data might not be migrated into a newer system.

Data's provenance is relevant to many use cases, including data verification.

To satisfy such use cases, this extension adds a `sources` array to the release schema, in which the publisher can list the information systems from which the data in the release originates.

## Example

```json
{
	"sources": [
		{
			"id": "sample-source",
			"name": "Sample Source",
			"url": "http://example.com"
		},
		{
			"id": "honducompras",
			"name": "HonduCompras 1.0",
			"url": "http://h1.honducompras.gob.hn/"
		}
	]
}
```

## Usage notes

There are some cases where the data source for a release comes from different information systems of the same publisher.

There are some cases in which you can link the data from the contracts database with the bidding and traditional process databases.

## Changelog

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/800>.
