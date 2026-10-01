---
title: "Dashboard de control de obras con BIM"
subtitle: "Valor ganado, modelo IFC 4D, financiamiento con préstamos a distintas tasas, personal y metrados de una obra, en una sola pantalla."
estado: ["Dashboard", "Solicitar"]
orden: [0]
solicitar : true
image: /images/dashboard_obras/animacion.webp
# app_url: ""
# repo_url: ""
# dataset_url: ""
stack: ["Python", "Dash", "Plotly", "IfcOpenShell", "IFC4X3", "Pandas", "EVM", "BIM 4D/5D"]
description: "Dashboard profesional para controlar una obra durante 12 meses: valor ganado (PMBOK), modelo BIM IFC en 3D vinculado al cronograma, deuda con préstamos a distintas tasas, control de personal, metrados y evaluación económica."
keywords: [dashboard de obra, BIM, IFC, valor ganado, EVM, curva S, Plotly Dash, IfcOpenShell, financiamiento, metrados, control de personal, Invierte.pe]
---

Este dashboard reúne en **una sola página** lo que normalmente está repartido entre el cronograma, el presupuesto, el modelo BIM y la tesorería de una obra. El proyecto de demostración es un **puente vehicular de 120 m** (4 tramos de 30 m) ejecutado en **12 meses**, con datos ficticios.

Una barra de tiempo fija en la parte superior controla la **fecha de corte**: al mover el mes (o pulsar *reproducir*), todo el tablero se recalcula como si estuviéramos parados en esa fecha, desde el modelo 3D hasta la deuda pendiente.

![Resumen del proyecto: ficha, avance físico, alertas e indicadores clave](/images/dashboard_obras/01_resumen.webp)

## Modelo BIM (IFC) y estado en el tiempo

El puente se modeló en **IFC4X3**: **92 elementos** con su cantidad de volumen, área y longitud, y un código de actividad que los enlaza con el cronograma. Con ello el modelo se vuelve **4D**: cada elemento aparece *no iniciado*, *en ejecución*, *terminado* o *atrasado* según la fecha de corte.

![Evolución mensual del modelo IFC, de octubre de 2025 a septiembre de 2026](/images/dashboard_obras/02_bim_4d_evolucion.webp)

El visor permite colorear por estado o por tipo de elemento IFC, cambiar entre vista 3D, elevación, planta y cimentación, y descargar el archivo `.ifc`.

![Modelo IFC coloreado por tipo de elemento](/images/dashboard_obras/03_modelo_ifc_por_tipo.webp)

![Vista de la cimentación: pilotes y zapatas](/images/dashboard_obras/04_modelo_ifc_cimentacion.webp)

![Sección de modelo BIM con estado de elementos, avance por componente y evolución](/images/dashboard_obras/05_bim_4d_seccion.webp)

## Valor ganado (PMBOK)

Curva S con valor planificado (PV), ganado (EV) y costo real (AC); índices **SPI** y **CPI** con semáforo; **EAC, ETC, VAC y TCPI**; y la fecha de fin proyectada por el método del tiempo ganado. En la demo el proyecto termina en plazo, pero con un **sobrecosto de 5 %** (CPI 0.95), producto de una estación lluviosa que retrasó la cimentación y obligó a acelerar la superestructura.

![Sección de valor ganado: curva S, indicadores, ejecución mensual y tendencia de SPI y CPI](/images/dashboard_obras/06_valor_ganado.webp)

## Cronograma

Diagrama de Gantt de 20 actividades con lo planificado frente a lo real, el porcentaje de avance de cada una y la línea de la fecha de corte.

![Diagrama de Gantt con plan y ejecución real](/images/dashboard_obras/07_cronograma_gantt.webp)

## Financiamiento con préstamos a distintas tasas

Cinco fuentes con **TEA entre 0 % y 17.5 %**: préstamo bancario, línea de crédito, leasing de maquinaria, factoring de valorizaciones y adelanto directo. Cada una con su propio sistema de amortización (cuota constante, capital constante, pago al vencimiento o proporcional al avance). El tablero muestra el saldo por fuente, el servicio de la deuda, la **TEA ponderada por saldo**, el costo financiero y el **flujo de caja** mensual.

![Sección de financiamiento: saldo por fuente, servicio de deuda, tasas y flujo de caja](/images/dashboard_obras/08_financiamiento.webp)

## Control de personal y seguridad

Personal por categoría frente a lo planificado, horas-hombre, ausentismo, costo de planilla, registro de trabajadores activos e indicadores de seguridad (**índices de frecuencia y severidad**, días sin accidentes, charlas e inspecciones).

![Sección de personal y seguridad y salud en el trabajo](/images/dashboard_obras/09_personal_seguridad.webp)

## Metrados y presupuesto por partida

47 partidas con su metrado del expediente, el **metrado extraído del modelo BIM**, la diferencia entre ambos, lo ejecutado a la fecha, el valor ganado, el costo real y el CPI de cada una.

![Sección de metrados: expediente frente a modelo BIM y presupuesto analítico](/images/dashboard_obras/10_metrados.webp)

## Evaluación económica

VAN, TIR y relación beneficio/costo **sociales** a 20 años con tasa de descuento de 8 %, que se **actualizan con el costo proyectado (EAC)** del mes de corte, más un análisis de sensibilidad. Es la conexión entre el control de la obra y la decisión de inversión.

![Evaluación económica: flujo descontado, cascada de valor presente y sensibilidad del VAN](/images/dashboard_obras/11_evaluacion_economica.webp)

## Cómo está hecho

- **Python + Dash + Plotly** para la interfaz, con un tema oscuro propio y una sola página con navegación por secciones.
- **IfcOpenShell** para crear, leer el modelo IFC4X3 y conectarse con software de modelado BIM; la geometría se triangula desde el propio IFC y se dibuja en Plotly.
- Cálculos en módulos independientes (valor ganado, préstamos, personal, metrados, evaluación) con **93 pruebas automáticas** que verifican identidades del EVM, cronogramas de deuda, consistencia entre datos y modelo, y todos los callbacks del tablero para cada mes.

> Todos los datos del ejemplo son ficticios y sirven para demostrar el alcance de la herramienta. Si quieres una versión adaptada a una obra o cartera de proyectos reales (con tu cronograma, presupuesto y modelo BIM), escríbeme desde la página de contacto.
