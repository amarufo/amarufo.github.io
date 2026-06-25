---
title: "Dashboard - Idea proyecto Mancomunidad Lima Sur"
description: "Visualización de indicadores delictivos y de seguridad, propone una integración interoperable del sistema de información de la Mancomunidad Lima Sur."
categoria: "Formulación"
date: 2026-06-25
author: "Amaru Fernández Olmedo"
image: /images/dash_idea_mancomunidadlimasur.png
tags: [PIP, Invierte.pe, formulación, dashboard, seguridad ciudadana, interoperabilidad]
app_url: "https://mancomunidadlimasur-app.streamlit.app/"
---

El diseño de proyectos de inversión pública (PIP) modernos exige el uso intensivo de datos territoriales para sustentar de manera irrefutable la brecha y el planteamiento técnico. En esta línea, he desarrollado un **Dashboard interactivo en Streamlit** para la **Mancomunidad Municipal de Lima Sur** (Villa El Salvador, Villa María del Triunfo, San Juan de Miraflores, Pachacámac y Cieneguilla). El objetivo fundamental es consolidar y procesar analíticamente los registros delictivos georreferenciados de la PNP, la proyección demográfica del INEI y las capacidades logísticas-presupuestales declaradas en el RENAMU.

## Intención

El corazón del aplicativo es transformar datos crudos dispersos en indicadores estructurados de **Presión Criminal, Capacidad Operativa y Brecha de Inversión**. 

> El dashboard permite simular el dimensionamiento óptimo de una plataforma interoperable unificada, ayudando al formulador a sustentar la alternativa tecnológica frente al MEF.

## Estructura

El aplicativo web se encuentra estructurado mediante pestañas dinámicas que atienden a las exigencias metodológicas del diagnóstico de preinversión:

1. **Panorama General y Posicionamiento:** Compara la incidencia delictiva de la Mancomunidad frente a todo Lima Metropolitana, calculando de manera automatizada la participación porcentual y la tasa de delitos por cada 10,000 habitantes.
2. **Análisis Espacial Avanzado:** Utiliza librerías geoespaciales para mapear la concentración delictiva en celdas H3 (Hotspots) e identificar vectores delictivos que cruzan las fronteras distritales, justificando así una intervención a nivel de Mancomunidad y no como distritos aislados.
3. **Auditoría Logística y de Capacidades (RENAMU):** Consolida series temporales del personal de serenazgo, cámaras de videovigilancia, vehículos con GPS, y presupuesto PIM frente a los niveles de ejecución presupuestal para identificar ineficiencias o brechas críticas. `Esta data no es del todo correcta, por lo que el aplicativo incluye un módulo de auditoría interna que detecta inconsistencias y anomalías estadísticas en los registros municipales.`
4. **Arquitectura Tecnológica e Interoperabilidad:** Incluye diagramas interactivos en Mermaid que modelan la unificación de los sistemas de videovigilancia locales (Genetec, Milestone, Hikvision) hacia un único Centro de Comando unificado con analítica de IA y despacho automatizado.
