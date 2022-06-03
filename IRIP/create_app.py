from flask import Flask
from flask import jsonify
from flask import Response

from .typing import Callable
from .typing import Tuple
from IRIP import v1


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

    @app.errorhandler(500)  # pragma: no cover
    def internal_server_error(e: int) -> Tuple[Response, int]:
        """handle 500 http error

        Args:
            e (int): http error from the server

        Returns:
            Json: error details
        """
        return (
            jsonify({"status": "failed", "msg": "500 Internal Server Error"}),
            e,
        )

    app.register_blueprint(v1.bp)

    return app
