"""
currencies index (main) view.

URLs include:
/
"""
import hashlib
import uuid
import shutil
import tempfile
import os
import flask
import arrow
import currencies

@currencies.app.route('/', methods=['GET', 'POST', 'HEAD'])
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("index.html", **context)