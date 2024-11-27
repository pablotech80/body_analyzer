# **Body Analyzer API** 🚀

<img src="./logo.JPG" alt="Logo" width="250" />

[![Version](https://img.shields.io/badge/version-1.0.0--beta-blue)]()
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-yellow)]()  
[![Deployed on Heroku](https://img.shields.io/badge/Heroku-Live-purple)](https://your-heroku-app.herokuapp.com)  
> **API para análisis biométrico diseñada para profesionales de la salud, nutricionistas y entrenadores personales.**

---

## **Índice**
1. [Descripción](#descripción)
2. [Características principales](#características-principales)
3. [Requisitos](#requisitos)
4. [Instalación y uso](#instalación-y-uso)
5. [Pruebas locales](#pruebas-locales)
6. [Endpoints disponibles](#endpoints-disponibles)
7. [Diagrama de flujo (Mermaid)](#diagrama-de-flujo-mermaid)
8. [Producción](#producción)
9. [Notas finales](#notas-finales)
10. [Contribuciones](#contribuciones)


---

## **Descripción**

La API **Body Analyzer** permite realizar cálculos biométricos avanzados y recomendaciones nutricionales iniciales a partir de datos básicos del usuario. Está diseñada como una herramienta backend que puede integrarse con un formulario web o una aplicación para capturar los datos de entrada.

Es ideal para:
- **Entrenadores personales**: Configuración inicial de planes de entrenamiento y objetivos.
- **Nutricionistas**: Recomendaciones dietéticas personalizadas.
- **Profesionales de la salud**: Evaluaciones rápidas y precisas.

Puedes probar la versión **beta** en producción aquí:
🌐 [**Body Analyzer API en Heroku**](https://your-heroku-app.herokuapp.com)

---

## **Características principales**

1. **Cálculos avanzados:**
   - **IMC**: Detecta si el IMC alto se debe a masa muscular o exceso de grasa.
   - **Porcentaje de grasa corporal**: Estimaciones basadas en fórmulas probadas.
   - **TMB y calorías diarias**: Ajustadas según el objetivo.

2. **Objetivos personalizables:**
   - Perder grasa.
   - Mantener peso.
   - Ganar masa muscular.

3. **Recomendaciones de macronutrientes**: Proporciones de proteínas, carbohidratos y grasas según el objetivo.

4. **Fácil integración**: Diseñada para ser integrada en una web o aplicación.

---

## **Requisitos**

- **Python 3.13+**
- Librerías necesarias (instaladas automáticamente desde el archivo `pyproject.toml`).

---

## **Instalación y uso**

### **1. Clona el repositorio**
```bash
git clone https://github.com/tu_usuario/body_analyzer.git
cd body_analyzer
```
### **2. Instala las dependencias**
```bash
pip install .
```
O, si prefieres usar el Makefile:
```bash
make install
```
### **3. Ejecuta la API localmente**
```bash
python src/body_analyzer/main.py
```
La API estará disponible en http://127.0.0.1:5000

---

## **Pruebas locales**

Puedes probar la API localmente con Postman, cURL o cualquier herramienta que soporte solicitudes HTTP. 
Aquí tienes un ejemplo para el endpoint principal:

Ejemplo de solicitud con cURL

```bash
curl -X POST http://127.0.0.1:5000/informe_completo \
-H "Content-Type: application/json" \
-d '{
  "peso": 90,
  "altura": 165,
  "edad": 44,
  "genero": "h",
  "cuello": 41,
  "cintura": 99,
  "cadera": 105,
  "objetivo": "perder grasa"
}'
```

### Respuesta esperada

```bash
{
  "interpretaciones": {
    "ffmi": "Muy cerca del máximo potencial.",
    "imc": "El IMC es alto, pero puede estar influenciado por una alta masa muscular.",
    "porcentaje_grasa": "Alto",
    "ratio_cintura_altura": "Alto riesgo",
    "rcc": "N/A"
  },
  "resultados": {
    "agua_total": 46.4,
    "calorias_diarias": 1762.69,
    "ffmi": 24.28,
    "imc": 33.06,
    "macronutrientes": {
      "carbohidratos": 176.27,
      "grasas": 39.17,
      "proteinas": 176.27
    },
    "masa_muscular": 66.105,
    "peso_saludable": {
      "max": 67.79,
      "min": 50.37
    },
    "porcentaje_grasa": 26.55,
    "ratio_cintura_altura": 0.6,
    "rcc": "N/A",
    "sobrepeso": 22.21,
    "tmb": 1836.14
  }
}
```

---
## **Endpoints disponibles**

_Método / Ruta / Descripción_

* GET	/	Verifica que el servidor esté corriendo.


* POST	/informe_completo / Genera un informe completo biométrico.
* POST	/calcular_imc / Calcula el índice de masa corporal (IMC).
* POST	/calcular_peso_grasa_corporal / Calcula la grasa corporal en kilogramos.
* POST	/calorias_diarias	/ Calcula las calorías diarias recomendadas.
* POST	/macronutrientes	/ Calcula el reparto de macronutrientes.
* Y más en el archivo endpoints.py
---

## **Diagrama de flujo**


[![](https://mermaid.ink/img/pako:eNptkUtOwzAQhq9ied1eIAskRCsEElBRYIG8GewhsYg90dhGgqYHYsGKI-RiOE7UglSv5h9_895JTQZlJWuGrhEPK-VFfo8hAVsSy-VZv_bvwzcIA5GCuN7e3fbifHM1cdkozBO01sxMLyal7fDjJ-yPo-AXxIw6Ui82TBoDOIs-0gT_cxX8Ej0yCMaQ2ggmt_FiyQ1fka0e690fPqYMRz0PEBnrMV6TQz82Qh6D6JAD-dzaJxjIaeahT7e8ZiYupbqEIULRysuFdMgOrMk73I2hSsYGHSpZZdMAvymp_D5zkCJtP7yWVeSEC8mU6kZWr9CGrFKXl4crC_kQ7uDtwD8THTUaG4lvppOVy-1_AZSnoCA?type=png)](https://mermaid.live/edit#pako:eNptkUtOwzAQhq9ied1eIAskRCsEElBRYIG8GewhsYg90dhGgqYHYsGKI-RiOE7UglSv5h9_895JTQZlJWuGrhEPK-VFfo8hAVsSy-VZv_bvwzcIA5GCuN7e3fbifHM1cdkozBO01sxMLyal7fDjJ-yPo-AXxIw6Ui82TBoDOIs-0gT_cxX8Ej0yCMaQ2ggmt_FiyQ1fka0e690fPqYMRz0PEBnrMV6TQz82Qh6D6JAD-dzaJxjIaeahT7e8ZiYupbqEIULRysuFdMgOrMk73I2hSsYGHSpZZdMAvymp_D5zkCJtP7yWVeSEC8mU6kZWr9CGrFKXl4crC_kQ7uDtwD8THTUaG4lvppOVy-1_AZSnoCA)


---

## **Producción**

La API está desplegada en Heroku en su versión beta: 🌐 Body Analyzer API en Heroku
https://bioanalyze-f0d59edaef22.herokuapp.com

Pruebas en producción
Puedes usar las mismas rutas y datos mencionados en las secciones anteriores, pero reemplaza http://127.0.0.1:5000 con la URL de Heroku.

---

## **Notas finales**

Versiones futuras:
* Implementación de autenticación.
* Integración con bases de datos.
* Creación de un frontend para facilitar el uso de la API.

---

## **Contribuciones**

¡Este proyecto está abierto a contribuciones! Si deseas colaborar:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios:
   ```bash
   git checkout -b feature/nueva-funcionalidad
    ```
3. Realiza tus modificaciones y realiza commits descriptivos:
    ```bash
   git commit -m "Añadida nueva funcionalidad para calcular ..."
    ```
4. Envía un pull request explicando tus cambios.

Por favor, asegúrate de seguir las mejores prácticas de código y, si es posible, agrega pruebas unitarias para cualquier nueva funcionalidad.

---