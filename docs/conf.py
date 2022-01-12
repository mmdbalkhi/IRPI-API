# -- Project information -----------------------------------------------------

project = 'IRIP API'
copyright = '2022, mmdbalkhi'
author = 'mmdbalkhi'
license = 'gpl-3'

# -- General configuration ---------------------------------------------------

extensions = [
]
utodoc_typehints = "description"
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "flask": ("https://flask.palletsprojects.com/", None),
}

issues_github_path = "mmdbalkhi/IRPI-API"
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']