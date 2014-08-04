#!/usr/bin/env python
import os

import codecs

# compile jinja templates
from jinja2 import Environment, PackageLoader, FileSystemLoader
import jinja2

def include_file(name):
    return jinja2.Markup(loader.get_source(env, name)[0])

loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), ''))

env = Environment(loader=loader)
env.globals['include_file'] = include_file
template = env.get_template('index.html')
html = template.render(appname=u'Error example')

# minify using html_minify
from htmlmin.minify import html_minify
# ----------------------------------------
# HERE THE TypeError happens...
# ----------------------------------------
html = html_minify(html)

# save to file
file = codecs.open("../index.min.html", "w", "utf-8")
file.write(html)
file.close()
