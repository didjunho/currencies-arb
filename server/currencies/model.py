"""currencies model (database) API."""
import sqlite3
import flask
import currencies


def dict_factory(cursor, row):
    """Convert database row objects to a dictionary.

    This is useful for building dictionaries which are then used to
    render a template.  Note that this would be
    inefficient for large queries.
    """
    output = {}
    for idx, col in enumerate(cursor.description):
        output[col[0]] = row[idx]
    return output
