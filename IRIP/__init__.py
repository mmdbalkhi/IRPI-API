from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
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

    # apply the blueprints to the app
    from IRIP import v1

    app.register_blueprint(v1.bp)

    app.add_url_rule("/v1/random", endpoint="find_random")
    app.add_url_rule("/v1/find/<img_name>", endpoint="find_by_name")

    return app
