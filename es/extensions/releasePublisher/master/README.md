## Extensión de publicador de release

### Descripción

Includes the information about the publisher at release level for the cases in that a release-package or record-packages
contains releases from different publishers.

### Campos

- release.publisher: Información que se usa únicamente para identificar el publicador de este release

### Ejemplo

```javascript
{
    "publisher": {
        "name": "SECRETARÍA DE LA FUNCIÓNN PÚBLICA / SECRETARIA DE HACIENDA Y CRÉDITO PÚBLICO", 
        "uri": "http://www.gob.mx/contratacionesabiertas/"
    }, 
    "license": "https://datos.gob.mx/libreusomx", 
    "publishedDate": "2018-02-14T19:23:19.405517Z", 
    "uri": "https://api.datos.gob.mx/v1/", 
    "records": [
        {
            "ocid": "ocds-07smqs-1303516", 
            "releases": [
                {
                    "publisher": {
                        "uri": "http://www.gob.mx/sfp", 
                        "uid": "27511", 
                        "name": "SECRETARÍA DE LA FUNCIÓN PÚBLICA"
                        }, 
                    "language": "es"
                    ....
                }, 
                {
                    "publisher": {
                        "uri": "http://www.gob.mx/shcp", 
                        "uid": "00000", 
                        "name": "SECRETARÍA DE HACIENDA Y CRÉDITO PÚBLICO"
                        }, 
                    "language": "es"
                    ....
                }
            ]
        }
    ]
}
```
