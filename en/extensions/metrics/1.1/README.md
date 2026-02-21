# Metrics Extension

The metrics extension provides a common building block for reporting structured performance information on contracts.

Metrics are structured like an [OLAP data cube](https://en.wikipedia.org/wiki/OLAP_cube) with each instance of `Metric` representing a single **observation**, categorized by a number of **dimensions**.

The metrics extension can be used at:

- The `planning` stage for forecasts for a future contracting process (e.g. forecast demand levels)
- The `tender` stage for targets for the contracting process (e.g. target availability levels or KPIs)
- The `awards` and `contracts` stages for targets agreed with the successful supplier (e.g. availability levels or KPIs)
- The `implementation` stage for actual performance information (e.g. actual demand, physical progress, availability or KPIs)

Where the metrics extension is used to model targets for a contracting process, the `description` field can be used to indicate whether the target is a minimum or recommended target.

## Example

### Forecasts

```json
{
  "planning": {
    "forecasts": [
      {
        "id": "annualDemand",
        "title": "Annual Demand",
        "description": "The annual demand",
        "observations": [
          {
            "id": "1",
            "period": {
              "startDate": "2015-01-01T00:00:00Z",
              "endDate": "2015-12-31T23:59:59Z"
            },
            "measure": 10000,
            "dimensions": {
              "vehicleType": "Car"
            }
          },
          {
            "id": "2",
            "period": {
              "startDate": "2015-01-01T00:00:00Z",
              "endDate": "2015-12-31T23:59:59Z"
            },
            "measure": 1000,
            "dimensions": {
              "vehicleType": "Trucks"
            },
            "notes": "Simple note"
          }
        ]
      }
    ]
  }
}
```

### Physical progress

The physical progress of a highway's construction, by percent completion and kilometres constructed:

```json
{
  "contracts": [
    {
      "id": "1",
      "awardID": "1",
      "implementation": {
        "metrics": [
          {
            "id": "completionPercent",
            "title": "Construction progress (percent)",
            "description": "Percent completion of the construction of example highway",
            "observations": [
              {
                "id": "completionPercent-2016-Q1",
                "period": {
                  "startDate": "2016-03-31T23:59:59Z",
                  "endDate": "2016-03-31T23:59:59Z"
                },
                "measure": "25",
                "unit": {
                  "name": "percent",
                  "id": "P1",
                  "scheme": "UNCEFACT"
                }
              }
            ]
          },
          {
            "id": "completionKilometres",
            "title": "Construction progress (kilometres)",
            "description": "Progress of construction of example highway measured in kilometres",
            "observations": [
              {
                "id": "completionKilometres-2016-Q1",
                "period": {
                  "startDate": "2016-03-31T23:59:59Z",
                  "endDate": "2016-03-31T23:59:59Z"
                },
                "measure": "15",
                "unit": {
                  "name": "kilometre",
                  "id": "KMT",
                  "scheme": "UNCEFACT"
                }
              }
            ]
          }
        ]
      }
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

### 2020-04-24

- Add `minProperties`, `minItems` and/or `minLength` properties.

### 2019-03-20

- Set `"uniqueItems": true` on array fields, and add `"minLength": 1` on required string fields.
- Make `Observation.unit` non-nullable, like `Item.unit`.
- Make `Observation.dimensions` non-nullable (undo earlier change).

### 2018-05-08

- Make `Metric.id` and `Observation.id` required to support revision tracking and [list merging](https://standard.open-contracting.org/latest/en/schema/merging/#array-values)

### 2018-05-01

- Add title and description to `Observation.period` and `Observation.value`.
- Make `Observation.dimensions` nullable.
