FSME
====

Design for FSIntra2013 - awesome Metro Design for the Fachschafts Intranet.
Pretty every view of [FSIntra](https://github.com/contradictioned/FSIntra2013) should be covered.


Brief overview of used stuff:

- [Gumby](http://gumbyframework.com)
- [Sass](http://sass-lang.com)
- [Compass](http://compass-style.org)
- [jQuery](http://jquery.com)
- [Redactor.js](redactorjs.com)
- [Selectize](http://brianreavis.github.io/selectize.js/)
- [Selectize-scss](https://github.com/herschel666/selectize-scss)
- Pixel Kit [Modern Touch](http://pixelkit.com/previews/flat-ui-kit/) (as source of inspiration)


For convenience, we use jinja2 to generate templates and a webserver to put things together.
To run the webserver install [Jinja2](http://jinja.pocoo.org) and [Pylons](http://www.pylonsproject.org).
Then run `server.py` and you will find the pages at `localhost:8077`.

**Note:** minification of hand-crafted javascripts (`js/selectnice.js`) is not yet done.