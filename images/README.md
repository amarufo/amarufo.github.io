# amaru_fo — Centro de Recursos del Formulador de Inversión Pública

Centro de recursos para el formulador de proyectos de inversión pública en el Perú (Invierte.pe), potenciado con herramientas de ciencia de datos y automatización.

🖥️ https://amarufo.github.io 
🖥️ https://inviertepe.com
👤 Wilbert Amaru Fernández Olmedo


## Arquitectura del sitio

| Sección         | URL           | Contenido                                                         |
|-----------------|---------------|-------------------------------------------------------------------|
| Inicio (Bolsón) | `/`           | Accesos directos, normativa clave, herramientas, últimas entradas |
| Recursos        | `/recursos/`  | Normativa, metodologías, anexos, aplicativos del MEF              |
| Métodos         | `/metodos/`   | Guía de métodos cuantitativos                                     |
| Proyectos       | `/herramientas/` | Portafolio (colección Markdown)                                   |
| Blog            | `/blog/`      | Artículos técnicos (posts Markdown)                               |
| Sobre mí        | `/sobre-mi/`  | Perfil + contacto                                                 |

---

## Cómo publicar contenido (100% Markdown)

### Un artículo de blog
1. Crea un archivo en `_posts/` con el nombre `AAAA-MM-DD-titulo.md`.
2. Añade el Front Matter y escribe en Markdown:

```markdown
---
title: "Título del artículo"
description: "Resumen de máx. 160 caracteres para Google y redes."
categoria: "Formulación"
date: 2026-05-20
author: "Amaru Fernández Olmedo"
image: /images/mi-imagen.png
tags: [IOARR, PIP, Python]
---

Contenido en Markdown...
```

3. `git push`. El artículo aparece solo en `/blog/` y en "Últimas entradas" del Home.

### Un proyecto
1. Crea un archivo en `_projects/` (ej. `mi-app.md`).
2. Front Matter con `app_url`, `dataset_url`, `repo_url`, `stack`, etc.
3. `git push`. Aparece solo en `/herramientas/` y en "Proyectos destacados".

### Recursos del Home (sin tocar HTML)
Edita `_data/recursos.yml` para añadir o cambiar tarjetas de normativa, metodologías,
aplicativos y herramientas. El menú se edita en `_data/navegacion.yml`.

---

## SEO automático

- **jekyll-seo-tag** genera `<title>`, `description`, Open Graph y Twitter Cards desde el Front Matter.
- **jekyll-sitemap** genera `sitemap.xml` en cada build.
- `robots.txt` apunta al sitemap.
- URLs limpias (`permalink: pretty`).

---

## Desarrollo local

```bash
bundle install
bundle exec jekyll serve
# http://localhost:4000
```

## Despliegue

Push a la rama principal del repositorio `amarufo.github.io`. GitHub Pages construye y publica automáticamente.
