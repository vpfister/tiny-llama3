# tiny-llama3


tiny llama3-like built from scratch

see [naklecha/llama3-from-scratch](https://github.com/naklecha/llama3-from-scratch) on github.

## Developing

Run `make` for help

    make install             # Run `poetry install`
    make showdeps            # run poetry to show deps
    make lint                # Runs bandit and black in check mode
    make format              # Formats you code with Black
    make test                # run pytest with coverage
    make build               # run `poetry build` to build source distribution and wheel
make pyinstaller # Create a binary executable using pyinstaller
make jupyter # run the jupyter-lab server
