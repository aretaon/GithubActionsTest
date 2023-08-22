# GutHUB Actions Test

![CI](https://bc2-silicon.biozentrum.uni-wuerzburg.de/jub29yk/actRunner-Test/raw/branch/badges/tests.svg)
![coverage](https://bc2-silicon.biozentrum.uni-wuerzburg.de/jub29yk/actRunner-Test/raw/branch/badges/coverage.svg)

This is a testing repository for using [Github Actions](https://github.com/features/actions) and unittests.
The documentation is automatically generated from docstrings using doctest and sphinx. The build of the docs is performed in the actions' workflow.
Furthermore pytest and pytest-doctestplus are used for unit testing based on the docstrings. The results of the unit
tests are used for generating badges for passing tests and code coverage (using pytest-coverage) (see above).