# flow-pytest-docker-compose-wait-mssql
This is just a quick working example to wait for mssql container, before launching integration tests with the `pytest-docker-compose`  python module.  
Official documentation here: https://pypi.org/project/pytest-docker-compose/
## Prerequisites
- python
- pip
- all python packages
- docker
- docker-compose

## Run
Just run `pytest` in the root directory of this repo:
- the test will be discovered under /flow-pytest-docker-compose-wait-mssql/integration-tests
- the resources from the docker-compose file will be spun-up using the `pytest-docker-compose` module
- the one and only test will wait for the DB to come online before asserting if it's up

<br>

### Side note:
Never store the DB passwords like this^^

