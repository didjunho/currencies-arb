"""REST API for comments."""
import flask
import currencies

from currencies.config import DATA_FOLDER
from currencies.config import CURRENCIES

@currencies.app.route('/api/get/', methods=["GET", "POST"])
def get_all_info():
    """Return context."""
    context = {}
    f = open(DATA_FOLDER + 'data_time.txt', 'r')
    context['updated'] = f.readlines()
    for tag in CURRENCIES:
        f = open(DATA_FOLDER + 'data_' + tag + '.txt', 'r')
        context[tag] = f.readlines()
    return flask.make_response(flask.jsonify(**context), 201)
