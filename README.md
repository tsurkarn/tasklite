# TaskLite

A tiny command-line to-do list manager, written in Python, used as a
practice repository for a "how open source collaboration works" workshop.

## What it does

TaskLite stores tasks in a local `tasks.json` file and lets you add,
list, complete, and remove them from the command line.

## Setup

```bash
git clone https://github.com/<your-username>/tasklite.git
cd tasklite
python3 src/tasklite.py list
```

No external dependencies — just Python 3.

## Usage

```bash
python3 src/tasklite.py add "Buy milk"
python3 src/tasklite.py list
python3 src/tasklite.py done 0
python3 src/tasklite.py remove 0
```

## Running tests

```bash
pip install pytest
pytest
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
Check the [Issues](../../issues) tab for things to work on — issues
labeled `good first issue` are a good place to start.
