from flask import Flask

from IRIP import v1

from .typying import Callable


def create_app(test_config=None) -> Callable:
    """Create and configure an instance of the Flask application.

    Args:
        test_config (str, optional): test configs. Defaults to None.

    Returns:
        Callable: a flask app
    """
    app = Flask(__name__, static_folder="img", instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    app.register_blueprint(v1.bp)

    return app
