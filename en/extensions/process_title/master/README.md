# Process title and description

In some cases it is important to provide an overall title and description for a contracting process, distinct from the individual title and description fields contained within `tender`, `awards` and `contracts` sections.

This extension adds `title` and `description` fields to the release schema.

These will often be used to provide a human-readable summary of information that is provided elsewhere in the OCDS document as structured data.

Publishers using these fields ought to be aware that not all applications will display their contents, and so key information for understanding the nature of the contracting process ought to also be provided using core OCDS fields.

## Example

```json
{
  "title": "Next-Generation Telecommunications PPP",
  "description": "The Next-Generation Telecommunications PPP project will guarantee the installation of a wholesale shared network that allows the provision of telecommunications services by current and future operators. The project will increase the telecommunication services coverage, promote competitive prices and enhance the quality of services according to international standards."
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### v1.1.5

- Review normative and non-normative words

### v1.1.4

- Add example to readme
- Update extension.json for Extension Explorer

### v1.1.3

- Use Apache 2.0 License
- Add tests and tidy code
