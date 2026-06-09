---
title: "Automatización: diagnóstico territorial para PIPs"
subtitle: "Aplicación beta que automatiza el diagnóstico territorial para proyectos de inversión pública en Perú."
estado: "Disponible"
orden: 1
image: /images/app_diagnostico_territorial.png
app_url: "https://amarufo-diagterritorial.streamlit.app/"
repo_url: ""
dataset_url: ""
stack: ["Python", "Streamlit", "Geopandas", "Folium", "Matplotlib", "Pandas", "NumPy"]
description: "Aplicación que, dada la ubicación de un proyecto de inversión pública (PIP) en Perú, ejecuta un pipeline georreferenciado y entrega un documento Word listo para integrar en el expediente técnico, con mapas, tablas e indicadores producidos por más de 50 motores de análisis territorial y de riesgo."
keywords: [INVIERTEPE, Invierte IA, automatización, preinversión, Streamlit, Python, riesgos, Invierte.pe, territorial, MEF, IOARR]
---

Un formulador de proyectos de inversión pública (PIP) en Perú dedica entre **40 y 80 horas** a la sección de diagnóstico territorial del estudio de preinversión: búsqueda de datos en portales oficiales dispersos, descarga manual de datos,  shapefiles, geoprocesamiento, generación de mapas y redacción. Esta carga frena la formulación oportuna y desincentiva el rigor territorial.

Con el objetivo de acelerar y mejorar la formulación de PIPs, IOARRs, Memorias Descriptivas y otros estudios de preinversión, desarrollamos una aplicación que, dada la ubicación del proyecto (latitud, longitud y ubigeo), ejecuta un pipeline georreferenciado y entrega — en menos de 5 minutos — un documento Word de 40 páginas aprox. listo para integrar en el expediente técnico, con mapas, tablas e indicadores producidos por más de 50 motores de análisis territorial y de riesgo.


## Fuentes oficiales utilizadas

El pipeline integra capas y datos de:

- **INEI** — cartografía de distritos / provincias / departamentos, ENAHO,
  Censo 2017, proyecciones de población.
- **CENEPRED** — escenarios de riesgo (heladas, friajes, sismos, tsunamis,
  movimientos en masa, volcanes).
- **SENAMHI** — clima, monitoreo de aire, hidrología, erosión, radiación
  solar.
- **ANA** — fuentes de agua (ríos, lagunas, acuíferos, glaciares,
  unidades hidrográficas), SNIRH.
- **INGEMMET** — geomorfología, riesgo volcánico.
- **OEFA / MINAM** — botaderos, calidad de aire, fiscalización ambiental.
- **INDECI** — incendios urbanos (SINPAD-COEN).
- **MINEDU** — Censo Escolar, ESCALE.
- **MINCETUR** — recursos turísticos.
- **MIDAGRI**, **IGN**, **OSRM** — rutas, distancias y referencias agrarias.
- **WWF / HydroSHEDS**, **Global Solar Atlas**, **Global Wind Atlas** — capas
  internacionales complementarias.
- **Observatorio de Conflictos Sociales (PUCP)** — conflictos sociales.
- **Entre otras fuentes oficiales y no oficiales.**

## ¿Cómo usarlo?

Pasos:

1. Ingresar la ubicación del proyecto (latitud, longitud y ubigeo).
2. Hacer click en "Generar Diagnóstico Territorial".
3. Esperar 5 minutos.
4. Descargar el documento Word y el comprimido ZIP con mapas, tablas e indicadores.