TypeError-Example
=================

Example files for issue #74 @ cobrateam/django-htmlmin

### Problem description
The problem is at `templates/render.py` (Line 25), 
where Jinja2 loaded template is minified before saved to file.

The hebrew chars are in `index.html` (Line 4). 
If line is removed `html_minify()` works.