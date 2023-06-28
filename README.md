# Pandas helpers

Tools to simplify pandas-based data processing

![Tests](https://github.com/jakeantmann/pandas_helpers/actions/workflows/tests.yml/badge.svg)

## Initialise dev

- Clone repo
- Run `source ./config/dev-init.sh` from within the root repo directory. This updates pip, installs all required packages (including those required for dev), and installs pre-commit.
  - Note: Some pre-commit hooks are shell scripts, so use linux when developing this package.

## TODO

### Write unit tests for every method and property, including for the indexers and accessors

- [ ] `is_col_test`, `_decide_if_call`
- [ ] `BaseCol.__getitem__`, `Col`, `CallCol`
- [ ] Dunder properties
- [ ] Accessor attrs
  - [ ] `cat`
  - [ ] `dt`
  - [ ] `str`
  - [ ] `sparse`
  - [ ] `plot`
- [ ] Regular properties
- [ ] Indexer properties
- [ ] Dunder methods
- [ ] Regular methods

### Packaging

- Organise package contents
  - Remove `_sandbox.py`. This should be replaced by unit tests, and some examples can be added to the readme
- Reintroduce and pass pre-commit checks
- Use PipTools (since this is a library)
- Add changelog
- Publish to PyPi

### Future work

- See whether the tests can be run on many versions of pandas
