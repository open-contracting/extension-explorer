# Tender Date Published

This extension adds a field to explicitly indicate the date and time when the tender was published. This field can be different from `tender/tenderPeriod/startDate` and `date` fields.

## Usage

Having this information in a easy way to access it can have many benefits, for instance, to be able to compute some indicators that will say how many days a potential bidder has to prepare an offer.

To satisfy such use cases, the `tender/datePublished` field should be used.

## Example

```json
{
  "tender": {
    "datePublished": "2019-07-23T1:27:10.673000-06:00"
  }
}
```

## Changelog

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/892>.

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
