source "https://rubygems.org"

# Meta-gem oficial de GitHub Pages — fija Jekyll y sus plugins en versiones
# compatibles con el entorno de producción de GitHub Pages.
gem "github-pages", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-feed"
end

# webrick ya no viene incluido en Ruby >= 3.0; requerido para jekyll serve.
gem "webrick", "~> 1.8"

# wdm: solo necesaria en Windows (monitor de cambios de archivos).
# En Linux el equivalente es rb-inotify (incluido por listen automáticamente).
gem "wdm", "~> 0.1", platforms: [:windows]

# tzinfo-data: zona horaria embebida; solo necesaria en Windows y JRuby.
# En Linux el sistema provee las zonas vía tzdata.
gem "tzinfo-data", platforms: [:windows, :jruby]
