## Development Environment

### 1. Python and Poetry Setup

This project uses [Poetry](https://python-poetry.org/) to manage dependencies and virtual environments.

Install Poetry (if not already installed):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Verify installation:

```
poetry --version
```

Set python version:

```
pyenv local 3.13.0
```

Install dependencies:

```bash
poetry install
```

Activate virtual environment:

```bash
poetry shell
```

### 2.Code Formatter and Linter

We use [Black](https://github.com/psf/black) and [Ruff](https://github.com/charliermarsh/ruff) for code formatting and linting. These tools are configured in the [pyproject.toml](pyproject.toml) file.

Run formatting manually:

```bash
poetry run black .
```

Run linting manually:

```bash
poetry run ruff check --fix .
```

### 3. Pre-commit Hooks

We use [pre-commit](https://pre-commit.com/) to run formatting and linting checks automatically before committing changes. This ensures consistent code formatting and reduces the likelihood of merge conflicts.

To install pre-commit hooks, run:

```bash
poetry run pre-commit install
```

To run pre-commit hooks manually, run:

```bash
poetry run pre-commit run --all-files
```

After installation, each `git commit` will automatically run the pre-commit hooks.

### 4. Pre-commit config file

The pre-commit config file is located at [.pre-commit-config.yaml](.pre-commit-config.yaml). This file specifies the hooks to run and their configurations.

Update hooks periodically

```
poetry run pre-commit autoupdate
```

### 5. Useful commands

| Action                    | Command                                 |
| ------------------------- | --------------------------------------- |
| Install dependencies      | `poetry install`                        |
| Enter virtual environment | `poetry shell`                          |
| Format code               | `poetry run black .`                    |
| Lint and autofix          | `poetry run ruff check --fix .`         |
| Install pre-commit hooks  | `poetry run pre-commit install`         |
| Run pre-commit manually   | `poetry run pre-commit run --all-files` |
| Run tests                 | `poetry run pytest`                     |
| Update pre-commit hooks   | `poetry run pre-commit autoupdate`      |
