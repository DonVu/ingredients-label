import os

from flask import Flask , render_template, request, redirect, url_for

from werkzeug.utils import secure_filename

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )



    UPLOAD_FOLDER = 'ingredients-label/static/img'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    DATABASE = 'ingredients-label/static/database/ingredients.db'
    app.config['DATABASE'] = DATABASE


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return redirect(url_for('label.index'))


    from . import label
    app.register_blueprint(label.bp)

    return app
