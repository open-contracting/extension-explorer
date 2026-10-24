# Exclusion grounds

Adds an object to describe the criteria to exclude tenderers from participating in a contracting process.

## Guidance

If you use a codelist for `tender.exclusionGrounds.criteria.type`, you should explain where the codes are from in your publication policy/user guide.

## Example

```json
{
  "tender": {
    "id": "1",
    "exclusionGrounds": {
      "criteria": [
        {
          "description": "Applicants not satisfying...",
          "type": "crime-org"
        }
      ]
    }
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.
