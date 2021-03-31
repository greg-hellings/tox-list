# Tox List composite action

This action will run `tox -l` in the root of your repository, convert the result output to
JSON, and set it as output for the step. Internally, if you have not already installed tox,
it will create a virtualenv and install tox into it.

## Inputs

### tox-args

A string of additional arguments to pass to tox. This can be useful if you want to limit the
number of outputs tox generates, etc.

## Outputs

### tox-envs

A JSON-formatted array of listed tox environments. This can be passed to a subsequent step to
dynamically generate the fan-out matrix in your testing steps

## Example usage

```yaml
jobs:
  collect:
    outputs:
      envs: ${{ steps.envs.outputs.tox-envs }}
    steps:
      - uses: actions/checkout@v2
      - uses: greg-hellings/tox-list@v1
        id: envs

  test:
    needs:
      - collect
    strategy:
      matrix:
        tox-env: ${{ fromJson(needs.collect.outputs.envs }}
    steps:
      - uses: actions/checkout@v2
      - uses: greg-hellings/tox-run@v1
        with:
          tox-env: ${{ matrix.tox-env }}
```
