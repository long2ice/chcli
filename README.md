# chcli

![pypi](https://img.shields.io/pypi/v/chcli.svg?style=flat)
![license](https://img.shields.io/github/license/long2ice/chcli)
![workflows](https://github.com/long2ice/chcli/workflows/pypi/badge.svg)
![workflows](https://github.com/long2ice/chcli/workflows/ci/badge.svg)

A Terminal Client for ClickHouse with AutoCompletion and Syntax Highlighting.

This project is inspired by [mycli](https://github.com/dbcli/mycli).

## Features

`chcli` is written using [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) and [antlr4](https://pypi.org/project/antlr4-python3-runtime/) with [grammar](https://github.com/ClickHouse/ClickHouse/tree/master/utils/grammar).

- Auto-completion as you type for SQL keywords as well as tables, views and columns in the database.
- Syntax highlighting using `Pygments`.
- Pretty prints tabular data.

## Install

You can install just by pip.

```shell script
> pip install chcli
```

## Usage

```shell script
> chcli --help
Usage: chcli [OPTIONS]

  A Terminal Client for ClickHouse with AutoCompletion and Syntax
  Highlighting.

Options:
  -v, --version       Show the version and exit.
  -h, --host TEXT     ClickHouse server host.  [default: 127.0.0.1]
  -p, --port INTEGER  ClickHouse server port.  [default: 9000]
  -u, --user TEXT     ClickHouse server user.  [default: default]
  --password TEXT     ClickHouse server password.  [default: ]
  --help              Show this message and exit.
```

## License

This project is licensed under the [Apache-2.0](https://github.com/long2ice/chcli/blob/master/LICENSE) License.
