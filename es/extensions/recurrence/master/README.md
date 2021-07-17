# Recurrence

This extension adds fields for information on the recurrence of the contracting process.

## Usage

These fields should be used if, for example, another procurement procedure or qualification system for the same contract matter is likely to be re-launched, or re-established, in the foreseeable future. Note that this does not mean awarding multiple contracts within a single qualification system, framework agreement, or dynamic purchasing system; in these cases, these fields should not be used.

This information can be useful, for example, to companies deciding whether to invest into machinery necessary for a particular contract. With this information, they know that there will likely be an opportunity to win similar contracts in future years, which may make the investment more worthwhile.¹

## Legal context

The [Revised Agreement on Government Procurement](https://www.wto.org/english/docs_e/legal_e/rev-gpr-94_01_e.htm) (GPA) includes: "each notice of intended procurement shall include … c. for recurring contracts, an estimate, if possible, of the timing of subsequent notices of intended procurement".

The European Union is a [party](https://www.wto.org/english/tratop_e/gproc_e/memobs_e.htm) to the GPA, and as such its [Directive 2014/24/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.094.01.0065.01.ENG) (Public contracts — setting out clear ground rules) includes: "Part C: Information to be included in contract notices … 27. In the case of recurrent procurement, estimated timing for further notices to be published."

This extension's fields correspond to [eForms BT-94 (Recurrence) and BT-95 (Recurrence Description)](https://github.com/eForms/eForms).

## Ejemplo

```json
{
  "tender": {
    "hasRecurrence": true,
    "recurrence": {
      "dates": [
        {
          "startDate": "2020-01-01T00:00:00Z"
        },
        {
          "startDate": "2021-01-01T00:00:00Z"
        }
      ],
      "description": "The duration of this contract and recurrent contracts will not exceed three years."
    }
  }
}
```

## Footnotes

¹ Usage guidance is adapted from [eForms technical specifications](http://ec.europa.eu/growth/content/targeted-consultation-eforms-next-generation-public-procurement-standard-forms-0_en).

## Issues

Reporte issues para esta extensión en el [repositorio de extensiones ocds](https://github.com/open-contracting/ocds-extensions/issues), poniendo el nombre de la extensión en el título del issue.

## Registro de cambios

### 2020-04-24

- Agregar las propiedades `minProperties`, `minItems` y/o `minLength`.

The original draft extension can be found in the [archived trade profile repository](https://github.com/open-contracting-archive/trade/tree/master/draft_extensions/lot_RecurrentProcurement)
