# Item attributes

Adds an `attributes` array to the item object to list any
extra attribute that an item may have, at the tender, award or
contract stage.
The attributes can be features like the item's model, brand, manufacturer, among others, including its value and an
unique identifier for that attribute

## Example

```json
{
  "tender": {
    "items": [
      {
        "id": "10121503-001-1",
        "description": "Balanceado para Ganado Vacuno - Alta Producción en bolsas de 25 k",
        "quantity": 350,
        "attributes": [
          {
            "name": "Presentacion",
            "value": "BOLSA",
            "id": "1"
          }
        ]
      }
    ]
  }
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/751>
