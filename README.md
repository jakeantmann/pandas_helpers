# Pandas helpers

Tools to simplify pandas-based data processing

![Tests](https://github.com/jakeantmann/pandas_helpers/actions/workflows/tests.yml/badge.svg)

## Initialise dev

- Clone repo
- Run `source ./config/dev-init.sh` from within the root repo directory. This updates pip, installs all required packages (including those required for dev), and installs pre-commit.
  - Note: Some pre-commit hooks are shell scripts, so use linux when developing this package.

## TODO

- [x] `Col.__call__(df)` should raise an error if it does not return a Series
- [ ] CallCol should raise an error if does not return a series

### Write unit tests for every method and property, including for the indexers and accessors

- [x] `_is_col_test`
- [x] `_decide_if_call`
- [x] `_get_series`
- [ ] `BaseCol.__getitem__` should act like standard df indexer
- [ ] `Col.__call__` should raise an error if it does not return a Series
- [ ] `CallCol.__call__` should raise an error if it does not return a Series
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

- [ ] Organise package contents
  - [ ] Add some examples from the analysis folder to the README
- [ ] Reintroduce and pass pre-commit checks
- [ ] Use PipTools (since this is a library) (UNSURE)
- [ ] Add changelog
- [ ] Publish to PyPi

### Future work

- See whether the tests can be run on many versions of pandas
