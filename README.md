# tabletop-board-backend
Service to find players for your tabletop game

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