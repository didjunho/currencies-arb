"""REST API for comments."""
import flask
import currencies
import json

from currencies.config import DATA_FOLDER
from currencies.config import CURRENCIES

@currencies.app.route('/api/get/', methods=["GET", "POST"])
def get_all_info():
    """Return context."""
    context = {}
    f = open(DATA_FOLDER + 'data_time.txt', 'r')
    context['updated'] = json.loads(f.readlines()[0])
    for tag in CURRENCIES:
        f = open(DATA_FOLDER + 'data_' + tag + '.txt', 'r')
        context[tag] = json.loads(f.readlines()[0])
    return flask.make_response(flask.jsonify(**context), 201)
