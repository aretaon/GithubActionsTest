# GitHUB Actions Test

![CI](https://github.com/aretaon/GithubActionsTest/blob/badges/tests.svg)
![coverage](https://github.com/aretaon/GithubActionsTest/blob/badges/coverage.svg)

This is a testing repository for using [Github Actions](https://github.com/features/actions) and unittests for automatic testing and deployment of the documentation as HTML.
It is automatically generated from docstrings using doctest and sphinx. The build of the docs is performed in the actions workflow.
Furthermore pytest and pytest-doctestplus are used for unit testing based on the docstrings. The results of the unit
tests are used for generating badges for passing tests and code coverage (using pytest-coverage) (see above). These badges are saved in a separate badges branch that is referenced in this README file.

## Documentation
The final documentation can be found at https://aretaon.github.io/GithubActionsTest/.
