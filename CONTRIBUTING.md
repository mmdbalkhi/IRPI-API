# How to contribute to IRIP

Thank you for considering contributing to IRIP!

## Support questions

Please don't use the issue tracker for this. The issue tracker is a tool
to address bugs and feature requests in IRIP itself. Use one of the
following resources for questions about using IRIP or issues with your
own code:

- Ask on [github discuss](https://github.com/mmdbalkhi/IRIP/discussions)

## Reporting issues

Include the following information in your post:

- Describe what you expected to happen.
- If possible, include a [minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) to help us
  identify the issue. This also helps check that the issue is not with
  your own code.
- Describe what actually happened. Include the full traceback if there
  was an exception.
- List your Python and Flask versions. If possible, check if this
  issue is already fixed in the latest releases or the latest code in
  the repository.

## Send Your own Image

If you are a photographer, your can send your own images for repo and we use your images in API. Thanks!

## Submitting patches

If there is not an open issue for what you want to submit, prefer
opening one for discussion before working on a PR. You can work on any
issue that doesn't have an open PR linked to it or a maintainer assigned
to it. These show up in the sidebar. No need to ask if you can work on
an issue that interests you.

Include the following in your patch:

- Use [Black](https://black.readthedocs.io) to format your code. This and other tools will run
  automatically if you install [pre-commit](https://pre-commit.com) using the instructions
  below.
- Include tests if your patch adds or changes code. Make sure the test
  fails without your patch.
- Update any relevant docs pages and docstrings. Docs pages and
  docstrings should be wrapped at 72 characters.
- Add an entry in `CHANGES.rst`. Use the same style as other
  entries. Also include `.. versionchanged::` inline changelogs in
  relevant docstrings.

### First time setup

- Download and install the [latest version of git](https://git-scm.com/downloads).
- Configure git with your [username](https://docs.github.com/en/github/using-git/setting-your-username-in-git) and [email](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address).

```sh
$ git config --global user.name 'your name'
$ git config --global user.email 'your email'
```

-Make sure you have a [GitHub account](https://github.com/join).

- Fork Flask to your GitHub account by clicking the [Fork](https://github.com/mmdbalkhi/IRIP-API/fork) button.
- [Clone](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#step-2-create-a-local-clone-of-your-fork) the main repository locally.

```sh
$ git clone https://github.com/mmdbalkhi/IRIP-API
$ cd IRIP-API
```

- Add your fork as a remote to push your work to. Replace
  `{username}` with your username. This names the remote "fork", the
  default mmdbalkhi remote is "origin".

```sh
$ git remote add fork https://github.com/{username}/IRIP-API
```

- Create a virtualenv.

#### MacOs/Linux

```sh
$ python3 -m venv env
$ . env/bin/activate
```

#### Windwons

```batch
> py -3 -m venv env
> env\Scripts\activate
```

- Upgrade pip and setuptools.

```sh
$ python -m pip install --upgrade pip setuptools
```

- Install the development dependencies, then install Flask in editable
  mode.

```sh
$ pip install -r requirements/dev.txt
```

- Install the pre-commit hooks.

```sh
$ pre-commit install
```

### Start coding

- Create a branch to identify the issue you would like to work on. If
  you're submitting a bug or documentation fix,

```sh
$ git fetch origin
$ git checkout -b your-branch-name origin/main
```

If you're submitting a feature addition or change, branch off of the "main" branch.

```sh
$ git fetch origin
$ git checkout -b your-branch-name origin/main
```

- Using your favorite editor, make your changes, [committing as you go](https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes).
- Include tests that cover any code changes you make. Make sure the test fails without your patch. Run the tests as described below.
- Push your commits to your fork on GitHub and
  [create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request). Link to the issue being addressed with
  `fixes #123` in the pull request.

```sh
$ git push --set-upstream fork your-branch-name
```

### Running the tests

Run the basic test suite with pytest.

```sh
$ pytest
```

This runs the tests for the current environment, which is usually
sufficient. CI will run the full suite when you submit your pull
request. You can run the full test suite with tox if you don't want to
wait.

```
$ tox
```

### Running test coverage

Generating a report of lines that do not have test coverage can indicate
where to start contributing. Run `pytest` using `coverage` and
generate a report.

```sh
$ pip install coverage
$ coverage run -m pytest
$ coverage html
```

Open `htmlcov/index.html` in your browser to explore the report.

Read more about [coverage](https://coverage.readthedocs.io).

### Building the docs

Build the docs in the `docs` directory using Sphinx.

```sh
$ cd docs
$ make html
```

Open `_build/html/index.html` in your browser to view the docs.

Read more about [Sphinx](https://www.sphinx-doc.org/en/stable).

> __**Note**__ This file Based on The Flask contributing guide
