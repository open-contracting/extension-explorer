# Additional Contact Points and Contact Point Languages

There are some cases where it is important to list multiple contact points for an organization, particularly in cases where each contact point deals with enquiries in particular languages only.

This extension adds an array of `additionalContactPoints` to the `Organization` object, and introduces an `availableLanguage` array of language codes to `ContactPoint`.

When this extension is used, publishers should include a **primary contact point** for the `contactPoint` object, on the basis that many applications will not be aware of the `additionalContactPoints` array. However, if a primary contact point can't be determined, all contact points may be disclosed in the `additionalContactPoints` array.

## Example

```json
{
  "parties": [
    {
      "id": "GB-LAC-E09000003",
      "roles": [
        "procuringEntity"
      ],
      "identifier": {
        "scheme": "GB-LAC",
        "id": "E09000003",
        "legalName": "AnyTown Council"
      },
      "name": "AnyTown Council",
      "address": {
        "streetAddress": "4, North London Business Park, Oakleigh Rd S",
        "locality": "London",
        "region": "London",
        "postalCode": "N11 1NP",
        "countryName": "United Kingdom"
      },
      "contactPoint": {
        "name": "Procurement Team",
        "email": "procurement-team@example.com",
        "telephone": "01234 345 346",
        "availableLanguage": [
          "en"
        ]
      },
      "additionalContactPoints": [
        {
          "name": "Procurement Team (International Enquiries)",
          "email": "procurement-team-international@example.com",
          "telephone": "01234 345 346 Extension 123",
          "availableLanguage": [
            "es",
            "fr",
            "de"
          ],
          "address": {
            "streetAddress": "5, North London Business Park, Oakleigh Rd S",
            "locality": "London",
            "region": "London",
            "postalCode": "N11 1NP",
            "countryName": "United Kingdom"
          }
        }
      ]
    }
  ]
}
```

## Modelling notes

`availableLanguage` is singular, although it is an array, to align with [Schema.org](https://schema.org/availableLanguage).

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2023-12-19

- Add `ContactPoint.address` field.

### 2020-06-04

- Review normative and non-normative words

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2019-03-20

- Set `"uniqueItems": true` on array fields.

### 2018-12-21

- Set `wholeListMerge` on `Organization.additionalContactPoints`
- Clarify use of language codes on `ContactPoint.availableLanguage`
