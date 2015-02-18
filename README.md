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
    - *nix: `$ apt-get install nodejs nodejs-legacy npm`
    - win: `> choco install nodejs.install`
- Ensure you have necessary npm modules installed:
    - all: `npm install -g bower grunt-cli`
- `$ git clone https://github.com/EntelekiaLearning/Website.git && cd Website`
- `$ sudo ./install.sh && ./run.sh` (remove `sudo` if on Windows)

...then open your browser to `localhost:5000/` to see the homepage (with `front end works` from JavaScript in the console) and `localhost:5000/api/v1/test` to see `{"status": 1}`