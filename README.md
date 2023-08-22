# GutHUB Actions Test

![CI](https://github.com/aretaon/GithubActionsTest/blob/badges/tests.svg)
![coverage](https://github.com/aretaon/GithubActionsTest/blob/badges/coverage.svg)

This is a testing repository for using [Github Actions](https://github.com/features/actions) and unittests.
The documentation is automatically generated from docstrings using doctest and sphinx. The build of the docs is performed in the actions' workflow.
Furthermore pytest and pytest-doctestplus are used for unit testing based on the docstrings. The results of the unit
tests are used for generating badges for passing tests and code coverage (using pytest-coverage) (see above).
