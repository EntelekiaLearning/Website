#Entelekia

#####One place to find local opportunities and digital resources to help you learn about anything.

## Notes:
- This project is very young and a M.V.P. is currently in the works.
- The website/webapp works on Mac (using [brew](http://brew.sh/)), *nix (using [apt](https://wiki.debian.org/Apt)), and Windows (using [chocolatey](https://chocolatey.org/) with [git bash](http://git-scm.com/download/win)).

## Installation:
- Ensure you have Python with Pip installed:
    - mac: `$ brew install python` & `$ easy_install pip`
    - *nix: `$ apt-get install python python-pip`
    - win: `> choco install python pip`
- Ensure you have NodeJS & NPM installed:
    - mac: `$ brew install node`
    - *nix: `$ apt-get install nodejs`
    - win: `> choco install nodejs.install`
- Ensure you have Neo4j installed:
    - mac: `$ brew install neo4j && neo4j start`
    - *nix: follow instructions at http://neo4j.com/docs/stable/server-installation.html#linux-install
    - win: `> choco install neo4j-community -Version 2.1.7`
- `$ git clone https://github.com/EntelekiaLearning/Website.git && cd Website`
- `$ sudo ./install.sh && ./run.sh` (remove `sudo` if on Windows)

...then open your browser to `localhost:5000/` to see the homepage (with `front end works` from JavaScript in the console) and `localhost:5000/api/v1/test` to see `{"status": 1}`