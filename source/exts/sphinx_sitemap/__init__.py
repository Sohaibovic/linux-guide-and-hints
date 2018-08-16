# Copyright (c) 2013 Michael Dowling <mtdowling@gmail.com>
# Copyright (c) 2017 Jared Dillard <jared.dillard@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

import xml.etree.ElementTree as ET
from sphinx.writers.html import HTMLTranslator


def setup(app):
    """Setup connects events to the sitemap builder"""
    app.add_config_value(
        'site_url',
        default=None,
        rebuild=False
    )
    app.connect('html-page-context', add_html_link)
    app.connect('build-finished', create_sitemap)
    app.sitemap_links = []


def add_html_link(app, pagename, templatename, context, doctree):
    """As each page is built, collect page names for the sitemap"""
    app.sitemap_links.append(pagename + ".html")


def create_sitemap(app, exception):
    """Generates the sitemap.xml from the collected HTML page links"""
    if app.builder.config.site_url is None:
        print("sphinx-sitemap error: site_url is not set in conf.py. Sitemap "
              "not built.")
        return
    if (not app.sitemap_links):
        print("sphinx-sitemap error: No pages generated for sitemap.xml")
        return

    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:schemaLocation", "http://www.sitemaps.org/schemas/sitemap/0.9 \
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd")

    for link in app.sitemap_links:
        url = ET.SubElement(root, "url")
        ET.SubElement(url, "loc").text = app.builder.config.site_url + link

    filename = app.outdir + "/sitemap.xml"
    ET.ElementTree(root).write(filename,
                               xml_declaration=True,
                               encoding='utf-8',
                               method="xml")
    print("sitemap.xml was generated in %s" % filename)
