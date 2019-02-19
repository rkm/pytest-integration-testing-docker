
# PyTest Integration Testing with Docker

Example of using Docker for PyTest integration testing. This is just an investigation, any comments appreciated!

### Option 1

Use one of the pip packages below to automatically spin up Docker dependencies inside test fixtures.

Advantages:

- No need to pollute the CI config. Can completely define dependencies in the Python tests 

Disadvantages:

- Still need to either configure the CI provider to use Docker, or provide some external Docker host to run on (i.e. Azure) 

### Option 2

Configure the dependencies in the Travis build and set the appropriate environment variables to access them from the tests.


Advantages:

-  

Disadvantages:

- Difficult to change CI providers since dependencies are specified in a vendor-specific file

## Useful Reading

- https://hharnisc.github.io/2016/06/19/integration-testing-with-docker-compose.html
- https://mike42.me/blog/how-to-set-up-docker-containers-in-travis-ci
- https://github.com/AndreLouisCaron/pytest-docker

## TODO

- Note on CI_DEV_LOCAL
- Investigate:
    - pytest-docker-fixtures
    - pytest-docker-compose 
