Yasmin (Work in Progress)
======

##Background
Debugging data by console is a pain. Various tools to address this issue by providing powerful visualisations
library. However, as far as the author concerned, those libraries are either too complicated or language specific.

Yasmin is an extensible, visual debugger targeted especially at data structures learners
that tries to be easy to install, easy to adapt, and language agnostic.

Yasmin has three main goals:

1. To provide students learning data structure an easy way to test and learn their code through visualisations.
2. To help students working on any small projects do the same thing as above.


##How Yasmin (will) work
Yasmin (will) consists of three parts.

1. A special formatted `.json` file that represents a data supported by **yasmin**.
2. **recipe** contains javascript codes which visualize the **.json** data
3. **yasmin** is the core glue program in python, responsible of managing recipes and creating servers.

Here is a typical (possible) Yasmin workflow.

1. A programmer just implemented a Binary Search Tree in Java. He/she wants to visualise the JUnit into cool animations.
2. He/she downloaded `yasmin`, run it as a server in `localhost` and included `yasmin-java` to her/his project.
3. He/she then wrapped his/her implementation class, using `YasminBSTWrapper`.
4. When JUnit is run, several trees was created, inserted, etc. `YasminBSTWrapper` listens to these changes,
   converting them into `.json`
5. The `.json` is read by the server, cooked using **recipe** into beautiful visualisations, made possible by D3.js
6. The server should 


##Contributing
This project follows PEP8 and it is recommended to install it in development environment.

To start hacking things, fork this repository, git clone, and install `pystache` using `pip`.

Unit testing provided with `run_test.sh`.

The python code is written in `3.4`, but it should work on `3.2` above.

##Work In Progress
This project is a work in progress. Hence, things may changes, but in general the workflow should not differ
too much.

All commits on the `master` will be squashed together once this hits `0.1.0` after a thorough testing.

##License
MIT