# **Trabajo Integrador Programación II**  
## **Vinoteca Virtual**

### **Descripción**  
Este es un trabajo integrador realizado para la materia _"Programación II"_ de la **Tecnicatura en Desarrollo Web** en la **Universidad Nacional de Entre Ríos**.  

El proyecto consiste en un aplicativo que expone servicios web para realizar consultas sobre una base de datos de una vinoteca virtual, almacenada en un archivo `.JSON`.  

---

## **Servicios disponibles**  

El aplicativo, desarrollado con el framework **Flask**, ofrece los siguientes servicios:  

1. **[Lista de bodegas](http://localhost:5000/api/bodegas)**  
   _Consulta el listado completo de bodegas, incluyendo las cepas y la cantidad de vinos que estas ofrecen._  

2. **[Lista de cepas](http://localhost:5000/api/cepas)**  
   _Obtén un listado de todas las cepas, junto con los vinos y bodegas que las producen._  

3. **[Lista de vinos](http://localhost:5000/api/vinos)**  
   _Consulta un listado de vinos, las bodegas que los producen, las cepas disponibles y las partidas registradas._  

> **Nota:** Si se añade `/id` al final de los servicios, se pueden realizar consultas específicas para cada uno de ellos.  

---

## **Ejemplos de uso**  

### **Consultar una bodega específica por ID:**  
- **[ID bodega](http://127.0.0.1:5000/api/bodegas/a0900e61-0f72-67ae-7e9d-4218da29b7d8)**  

  **Respuesta esperada:**  
  ```json
  {
    "id": "a0900e61-0f72-67ae-7e9d-4218da29b7d8",
    "nombre": "Casa La Primavera Bodegas y Viñedos",
    "cepas": [
      "Chardonnay",
      "Malbec",
      "Cabernet Suavignon",
      "Merlot"
    ],
    "vinos": [
      "Profugo",
      "Oveja Black",
      "Sin Palabra"
    ]
  }

### **Consultar una cepa específica por ID:**  
- **[ID cepa](http://127.0.0.1:5000/api/cepas/33ccaa9d-4710-9942-002d-1b5cb9912e5d)**

  **Respuesta esperada:**
  ```json
  {
    "id": "33ccaa9d-4710-9942-002d-1b5cb9912e5d",
    "nombre": "Chardonnay",
    "vinos": [
      "Profugo (Casa La Primavera Bodegas y Viñedos)",
      "Oveja Black (Casa La Primavera Bodegas y Viñedos)",
      "Sin Palabra (Casa La Primavera Bodegas y Viñedos)",
      "Sottano (Bodega Sottano)"
    ]
  }

### **Consultar un vino específico por ID:**  
- **[ID vino](http://127.0.0.1:5000/api/vinos/4823ad54-0a3a-38b8-adf6-795512994a4f)**
 
  **Respuesta esperada:**
  ```json
  {
    "id": "4823ad54-0a3a-38b8-adf6-795512994a4f",
    "nombre": "Abducido",
    "bodega": "La Iride",
    "cepas": [
      "Cabernet Suavignon",
      "Malbec"
  ],
    "partidas": [
      2024,
      2023,
      2022
    ]
  }

 ## **Filtros avanzados**  

También es posible buscar y ordenar los vinos utilizando parámetros como `anio`, `orden` y `reverso`.  

- **[Filtrar vinos por año](http://127.0.0.1:5000/api/vinos?anio=2020&orden=nombre&reverso=no)**  

  **Respuesta esperada:**  
  ```json
  [
    {
      "id": "ea3d6c45-e747-2e86-ddf8-0746cc13f21c",
      "nombre": "Familia Gascon",
      "bodega": "Escorihuela Gascon",
      "cepas": [
        "Cabernet Suavignon",
        "Malbec",
        "Merlot"
      ],
      "partidas": [2020, 2021]
    },
    {
      "id": "205db14f-c0c0-a286-0a5e-0daa7a3f37f0",
      "nombre": "Sin Palabra",
      "bodega": "Casa La Primavera Bodegas y Viñedos",
      "cepas": [
        "Chardonnay",
        "Cabernet Suavignon",
        "Malbec",
        "Merlot"
      ],
      "partidas": [2022, 2021, 2020]
    }
  ]

## **Sobre el proyecto**
Este trabajo es una introducción a la programación con Python, y busca ayudar a estudiantes a:

- Familiarizarse con la manipulación de archivos JSON.
- Comprender los principios de la creación de clases y buenas prácticas en programación orientada a objetos.
- Aprender a construir aplicaciones web básicas utilizando Flask.

**Cualquier contribución o feedback será bienvenido. ¡Gracias por tu interés en este proyecto!**
