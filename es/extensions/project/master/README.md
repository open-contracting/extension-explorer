# Proyecto

Planning processes can relate to different types of projects, including:

- An infrastructure project, as defined by the [Open Contracting for Infrastructure Data Standards Toolkit](https://standard.open-contracting.org/infrastructure/latest/en/projects/#what-is-a-project) (OC4IDS), like the construction of a bridge
- A programme of work, which can include many infrastructure projects, like the construction of a highway of which the bridge is a part
- A public-private partnership project, as described by [OCDS for PPPs](https://standard.open-contracting.org/profiles/ppp/latest/en/)

This extension adds a `planning.project` object to describe the **infrastructure** or **public-private partnership** (PPP) project to which a planning process is related. The identifier of the project ought to be disclosed in `planning.project.id`.

The `planning.budget.projectID` field ought to not be used to disclose the identifier of an infrastructure or PPP project. Rather, this field is used to disclose the identifier of a programme of work as it appears in a budget, like a national or state budget. Since such programmes of work can include many infrastructure projects, it is necessary to disclose their identifiers separately.

This extension must be used with the [Location](https://extensions.open-contracting.org/en/extensions/location/master/) extension.

## Ejemplo

A buyer announces a planning process for the design of a bridge.

This planning process is part of an infrastructure project, which covers the design, construction and supervision of the bridge. Information about the infrastructure project is disclosed in the `planning.project` object. For example, the `planning.project.sector` field describes the project's sector, using the [OC4IDS projectSector codelist](https://standard.open-contracting.org/infrastructure/latest/en/reference/codelists/#projectsector).

A separate OC4IDS dataset describes infrastructure projects in greater detail. In the planning process, `planning.project.id` and `planning.project.uri` reference the project's identifier and URI in that OC4IDS dataset.

The planning process and infrastructure project are funded through a programme of work to upgrade the nation's highways. The name and identifier of the programme of work as it appears in the national budget are disclosed in the `budget.project` and `budget.projectID` fields.

*Note: Planning processes related to public-private partnership projects are modelled in the same way. Information about the PPP project is disclosed in `planning.project`, not `planning.budget.project` or `planning.budget.projectID`.*

```json
{
  "ocid": "ocds-213czf-0000",
  "id": "1",
  "date": "2024-01-01T00:00:00Z",
  "tag": [
    "planning"
  ],
  "planning": {
    "project": {
      "id": "oc4ids-bu3kcz-0000",
      "title": "State Highway 1 Clutha River Bridge",
      "description": "Design, construction and supervision of a new bridge crossing for State Highway 1 over the Clutha River.",
      "totalValue": {
        "amount": 113000000,
        "currency": "NZD"
      },
      "uri": "http://example.com/projects/oc4ids-bu3kcz-0000.json",
      "sector": {
        "id": "transport.road",
        "description": "Road transport, including roads, highways, streets, tunnels and bridges.",
        "scheme": "oc4idsProjectSector"
      },
      "additionalClassifications": [
        {
          "id": "03.04.05",
          "description": "Bridges for road transport.",
          "scheme": "My local scheme"
        }
      ],
      "locations": [
        {
          "description": "Balclutha, Otago",
          "geometry": {
            "type": "Point",
            "coordinates": [
              169.745,
              -46.2359
            ]
          }
        }
      ]
    },
    "budget": {
      "project": "National Highway Upgrade",
      "projectID": "001-001-002"
    }
  },
  "tender": {
    "id": "1",
    "title": "Bridge design"
  }
}
```

## Registro de cambios

### 2024-03-28

- Recommend use of the 'oc4idsProjectSector' classification scheme for project sector.
- [Abandon in-file translations](https://github.com/open-contracting/standard/pull/1665).

### 2021-04-15

- Add infrastructure project example.

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

### 2020-04-16

- Eliminar guía relacionada al objeto `planning.budget`. Ver [#701](https://github.com/open-contracting/standard/issues/701).

### 2018-05-03

- Add additional guidance on the use of OCDS fields in the context of this extension.

### 2017-12-29

- Remove the repetition of OCDS fields in this extension.

### 2017-07-08

- Add multilingual support for `Project.title` fields.
- Remove multilingual support for non-existent `Project.source` and `Project.project` fields.
- Restaura los campos `Budget.project` y `Budget.projectID`.
- Remove obsolete `mergeStrategy` properties.

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.
