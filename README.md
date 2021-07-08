# tabletop-board-backend
Service to find players for your tabletop game

[![CircleCI](https://circleci.com/gh/skonik/tabletop-board-backend.png?branch=develop&style=shield)](https://app.circleci.com/pipelines/github/skonik/tabletop-board-backend/25/workflows/e5444e78-9030-458b-9dba-b5761cbf5a34) [![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/release/python-390/) [![CircleCI](https://img.shields.io/github/issues-pr-closed/skonik/tabletop-board-backend?style=plastic
)](https://github.com/skonik/tabletop-board-backend/pulls?q=is%3Apr+is%3Aclosed)

## Get it up and running

1. `$ make dev.build` - build docker images;
2. `$ make dev.up` - run docker containers;
3. `$ make dev.migrate` - apply migrations;


## Additional commands

* `$ make dev.logs` - view backend logs;
* `$ make dev.ps` - view running services(an alias to docker-compose ps);
* `$ make dev.restart` - restart backend;
* `$ make dev.lint` - run linters;
* `$ make dev.test` - run tests;
* `$ make dev.down` - down all the services;