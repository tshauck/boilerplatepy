# Boilerplatepy

> :hotsprings: :snake:

[Boilerplate](https://github.com/zulily/boilerplate/),
the inspiration for Boilerplatepy, is a simple tool to facilitate
building and running go programs.

Boilerplatepy borrows the concepts from Boilerplate, but is instead
aimed at easy building and running python packages.

The concepts as explained by the README.md:

> Boilerplate revolves around 3 concepts, each of which are used to set up your
> new project:

> * `repository`: the name of the source control repository _(e.g. github.com)_
> * `namespace`: the name of the organization/group in the repository _(e.g.
  zulily)_
> * `project`: the name of the binary _(e.g. fizzbuzz)_

Boilerplatepy, unlike Boilerplate, cannot build a static binary and give you
utmost confidence that your executable will run on a compatable platform.

But, it can give you a fair amount of confidence that you'll be able to
quickly develop, run, and test against a deployable environment from your development
machine.

It is also probably not suitable as a basis for open source packages as it
is intented work within the constraint of a single target platform.

## Quick Start

Install:

    $ pip install boilerplatepy

Given the inputs:

    $ boilerplatepy -project="fizzbuzz" -repository="github.com" -namespace="tshauck"

Boilerplatepy will construct a python project that looks like:

    $ tree
    .
    ├── Dockerfile
    ├── Makefile
    ├── build
    │   └── Dockerfile
    ├── fizzbuzz
    │   ├── __init__.py
    │   └── main.py
    ├── requirements.txt
    └── setup.py

This project can then be built.

    $ cd fizzbuzz; make fizzbuzz

A `fizzbuzz` wheel will be built.

    $ ls dist
    fizzbuzz-0.0.0-py2-none-any.whl

It is then easy to build the docker image, and run it.

    $ make dockerize
    ( ... )
    $ docker run -t tshauck/fizzbuzz:82e1daa # tag is the git sha
    In github.com/tshauck/fizzbuzz

## Other `make` options

- `make deps`: Build the wheels from the `requirements.txt` and place them in
  the hosts `./wheelhouse/`.
- `make lint`: Run `pylint` on the files and print a colorized report
- `make test`: Run `python setup.py test`.
