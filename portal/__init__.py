from flask import Flask

app = Flask(__name__, static_url_path='/static', static_folder='portal/static')

from portal import routes