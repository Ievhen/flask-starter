from flask import Blueprint, redirect, render_template


route_blueprint = Blueprint('route',__name__)


@route_blueprint.route('/')
@route_blueprint.route('/index')
def index():
    return render_template('index.html')
