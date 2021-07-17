# Competitive

Adds a field to the tender object in a framework agreement call-off to indicate if it is competitive or direct.

## Example

```json
{
  "tender": {
    "id": "2421-1016-CM20",
    "procuringEntity": {
      "name": "I.MUNICIPALIDAD DE CONCEPCION | DIRECCION DE SALUD MUNICIPAL DE CONCEPCION",
      "id": "CL-MP-3413"
    },
    "competitive": false
  },
  "awards": [
    {
      "id": "42133251",
      "title": "JERINGAS DAS CONCEPCION",
      "description": "2239-16-LR15 Órtesis, Prótesis, Endoprótesis e Insumos de Salud. FINANCIAMIENTO: 215.22.04.005.001 SP 28 SE SOLICITA LA ACEPTACIÓN DE ESTA ORCOM A TRAVÉS DE LA PLATAFORMA MERCADO PUBLICO ANTES DE REALIZAR LA ENTREGA DEL BIEN O SERVICIO",
      "status": "active",
      "date": "2020-06-23T15:40:44Z",
      "value": {
        "amount": 7526475.0,
        "currency": "CLP"
      },
      "suppliers": [
        {
          "name": "Tecnika S.A. | Tecnika S.A.",
          "id": "CL-MP-27291"
        }
      ],
      "items": [
        {
          "id": "111570611",
          "description": "Aparatos de inyección hipodérmica o accesorios(1391678 )JERINGA HIPODERMICA CONTROLADA VENOTEK 10ML LUER LOCK CON AGUJA 21GX1 1/2 100 UNIDADES 1418179",
          "quantity": 500.0,
          "unit": {
            "value": {
              "amount": 4228.0,
              "currency": "CLP"
            }
          }
        }
      ]
    }
  ],
  "relatedProcesses": [
    {
      "id": "1",
      "relationship": [
        "framework"
      ],
      "title": "Órtesis, Prótesis, Endoprótesis e Insumos de Salud",
      "scheme": "ocid",
      "identifier": "ocds-70d2nz-2239-16-LR15"
    }
  ]
}
```

## Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

## Changelog

This extension was originally discussed in <https://github.com/open-contracting/standard/issues/784>.
