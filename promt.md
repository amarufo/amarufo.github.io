# Prompt Maestro — Auditoría y Rediseño de Servicios de la Página Web

## 0. Rol y contexto

Eres un agente de desarrollo trabajando sobre el repositorio de la página web profesional de Amaru, economista especializado en formulación de estudios de preinversión bajo el sistema INVIERTE.PE (Perú). La página debe presentar y **vender** sus servicios reales — no ser un portafolio genérico de plantilla.

Trabajas bajo las convenciones habituales del proyecto:
- Fases con **checkpoint de aprobación obligatorio** — no avanzas a la siguiente fase sin luz verde explícita del usuario.
- `/clear` entre fases para no arrastrar contexto innecesario.
- Marcador `[PENDIENTE]` para cualquier dato, cifra, testimonio o copy que no tengas confirmado — nunca lo inventas ni lo aproximas.
- Ningún cambio de fondo (estructura, contenido, promesas de servicio) sin aprobación explícita.

## 1. Portafolio de servicios priorizado

Este orden refleja validación de mercado y riesgo legal/regulatorio real, no solo potencial de ingresos. Úsalo como guía de qué destacar primero en la arquitectura de la página.

### Nivel 1 — Ingreso base (ya validado, mantener visible y con más detalle)
- Elaboración de estudios de preinversión: fichas técnicas simplificadas, de baja y mediana complejidad, estandarizadas, y estudios a nivel de perfil.
- Formatos 5A, 7A, 6B; presupuestos; backup documentado del proyecto (bases de datos, documentación).
- Términos de referencia para componentes sociales (capacitación, asistencia técnica, documentos de gestión).
- Obras por Impuestos, bajo el marco reformado (Ley N° 32460, D.S. N° 038-2026-EF).

### Nivel 2 — Diagnóstico territorial + banco de proyectos (el mayor punto de apalancamiento actual)

Dos públicos distintos, mismo motor de datos y mismo pipeline:

**a) Formuladores (B2B):** diagnóstico territorial premium (demografía, cartografía, brechas de infraestructura, series históricas) entregado listo para pegar en fichas técnicas INVIERTE.PE.

**b) Autoridades recién electas** (gobernadores regionales y alcaldes del período 2027-2030, tras las elecciones del 4 de octubre de 2026): banco de proyectos priorizados según brechas para arrancar su Programación Multianual de Inversiones desde el primer día de gestión. Este mercado se repite cada 4 años, encaja directamente con el expertise de Amaru, y tiene mucha menor fricción legal/ética que vender a candidatos en campaña — es un contrato de consultoría normal con un gobierno local, no un gasto de campaña declarable.

**Punto clave para el copy de la página:** gran parte de la data cruda que alimenta estos diagnósticos ya es abierta y gratuita (SIGRID del CENEPRED, Banco de Inversiones del MEF, INEI, ENAPRES, RENAMU). El valor que se vende NO es "acceso exclusivo a datos" — eso sería engañoso — sino velocidad de síntesis, formato listo para usar, y aplicación experta de la metodología de priorización de brechas de INVIERTE.PE. La página debe comunicar esto explícitamente.

### Nivel 3 — Automatización y productos digitales

**ESTO ES UNA IDEA, DÉJALO COMO EN PROGRESO. TODAVÍA NO SE SABE COMO IMPLEMENTAR CORRECTAMENTE**

- `invierte-ia` (plataforma Streamlit), Explorador de Normativa, Guía Interactiva de Métodos Cuantitativos.
- Generador automático de anexos y plantillas inteligentes.
- Suscripción a sistema de información centralizada para consultores (fuentes públicas ya organizadas y actualizadas).

### Nivel 4 — Información para actores políticos (tratar con cautela; ventana corta y acotada)

- El plazo de inscripción de listas para las Elecciones Regionales y Municipales 2026 venció el 19 de junio de 2026. El Plan de Gobierno (que incluye diagnóstico) es un requisito ya cumplido por los partidos inscritos y de acceso público y gratuito vía el portal del JNE. **No presentar este servicio como "ayuda para inscribirse"** — ese mercado ya cerró para este ciclo.
- Sí queda una ventana de campaña activa hasta el 4 de octubre de 2026, donde partidos o candidatos podrían querer material de respaldo (propuestas sectoriales trabajadas, comparativos entre distritos, banco de ideas de proyectos) para debates o medios. Información financiera, presupuestal de la entidad pública donde está postulando el candidato: ¿qué ingresos tuvo la entidad pública? ¿cuánto se gasta en proyectos de inversión? ¿qué proyectos están en ejecución? ¿qué proyectos están en cartera? ¿cómo va la ejecución de los proyectos? ¿qué brechas de infraestructura existen? ¿qué proyectos se priorizan según la metodología INVIERTE.PE? 
- Las elecciones generales (presidencia/congreso) ya se resolvieron en julio de 2026 — no incluir contenido dirigido a ese público ahora; ese submercado no vuelve a abrirse por varios años.

## 2. Principios no negociables (aplican a TODA la implementación)

1. **Ningún dato personal identificable ni perfilamiento individual de electores**, bajo ninguna sección de la página. Las opiniones/convicciones políticas de una persona identificable son datos sensibles bajo la Ley N° 29733 y requieren consentimiento expreso y por escrito — fuera de alcance para cualquier producto de este sitio. Todo lo que se ofrezca debe ser agregado/estadístico (por distrito, por segmento poblacional), nunca por persona.
2. Todo dato territorial o estadístico mostrado debe citar su fuente pública (INEI, ENAPRES, RENAMU, SIDPOL, SIGRID, Banco de Inversiones, planes de gobierno del JNE).

## 3. Fases de trabajo (con checkpoint obligatorio)

### FASE 0 — Auditoría del repo actual (solo lectura, sin cambios)
Objetivo: entender qué existe antes de proponer nada.
- Mapear estructura de carpetas, stack (framework, hosting, CMS si aplica), páginas/rutas actuales.
- Listar qué servicios ya están presentados en la página y con qué nivel de detalle.
- Identificar deuda técnica visible (enlaces rotos, contenido desactualizado, falta de responsive, SEO básico ausente, etc.) sin corregir nada todavía.

**DETENTE. Espera aprobación explícita antes de continuar a la Fase 1.**

### FASE 1 — Arquitectura de información propuesta
Objetivo: proponer, no construir.
- Proponer el árbol de páginas/secciones nuevo, integrando el portafolio de servicios de la Sección 1.
- Para cada sección nueva especificar: propósito, público objetivo, tipo de contenido (texto, tabla, mapa interactivo, PDF de muestra, formulario de contacto), y qué `[PENDIENTE]` de información se necesita de Amaru (tarifas, casos reales anonimizados, capturas de `invierte-ia`, etc.).
- Marcar explícitamente qué secciones usarán datos "de ejemplo" (dummy o ya públicos) vs. datos reales de clientes.

**DETENTE. Espera aprobación explícita antes de continuar a la Fase 2.**

### FASE 2 — Diseño de página(s) de muestra ("ejemplo de producto")
Objetivo: maquetar cómo se ve un entregable, sin usar datos reales de clientes ni datos personales de terceros.
- Diseñar 1-2 páginas de ejemplo: "así se ve un diagnóstico territorial" y "así se ve un banco de proyectos priorizado", con datos públicos o sintéticos, claramente etiquetados como ejemplo.
- Incluir link o botón de descarga de un PDF de muestra (puede ser un placeholder marcado `[PENDIENTE]` si el PDF real todavía no existe).

**DETENTE. Espera aprobación explícita antes de continuar a la Fase 3.**

### FASE 3 — Implementación incremental
Objetivo: construir, sección por sección, con revisión entre cada una.
- Implementar una sección a la vez, en el orden aprobado en la Fase 1.
- Ejecutar `/clear` entre cada sección.
- Usar `[PENDIENTE]` para cualquier dato o copy que falte; nunca inventar cifras, testimonios o casos.

**DETENTE después de cada sección. Espera aprobación antes de pasar a la siguiente.**

### FASE 4 — QA final
- Verificar el checklist de la Sección 2 (principios no negociables) contra el sitio completo.
- Verificar que todas las fuentes de datos estén citadas visiblemente.
- Entregar lista final de `[PENDIENTE]` restantes para que Amaru los complete.

## 4. Nota de cierre para el agente

Si en cualquier fase detectas que una sección propuesta implicaría recolectar, comprar o procesar datos personales identificables de votantes, candidatos o terceros más allá de lo públicamente disponible, **detente y señálalo explícitamente** en vez de continuar. Esa es una decisión que le corresponde a Amaru, no al agente.