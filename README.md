FSME
====

Design for FSIntra2013 - awesome Metro Design for the Fachschafts Intranet.


Brief overview of used stuff:

- [Gumby](http://gumbyframework.com)
- [Sass](http://sass-lang.com)
- [Compass](http://compass-style.org)
- [jQuery](http://jquery.com)
- [Redactor.js](dactorjs.com)
- [Sortable](http://rubaxa.github.io/Sortable/)
- Pixel Kit [Modern Touch](http://pixelkit.com/previews/flat-ui-kit/) (as source of inspiration)


For convenience, we use a jinja2 to generate templates and a webserver to put things together.
To run the webserver install jinja2 and pyramid pylons [Jinja2](http://jinja.pocoo.org) [Pylons](http://www.pylonsproject.org) and execute 'server.py'

What to do:

- evaluate select2 (customizing capabilities)
- replace selectize.js by select2.js
- Getränke styles
- fix buges everywhere
    + left: 2px in protololl_change (remove?)
- test cross browser compatibiliy
- maybe change line-height for forms
- refactor sass
    + its messy by now
    + move repetetive styles to more general place
    + abstract repetetive directives to mixins
    + move colors to funtions
    + file names are not comprehensible
