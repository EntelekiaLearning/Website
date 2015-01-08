#Entelekia

#####One place to find local opportunities and digital resources to help you learn about anything.

## Notes:
- This project is very young and an MVP is currently in the works.
- The website/webapp only works on Mac (using [brew](http://brew.sh/)) and *nix (using [apt](https://wiki.debian.org/Apt)) at the moment.

## Installation:
- Ensure you have Python with Pip installed:
    - mac: `$ brew install python` & `$ easy_install pip`
    - *nix: `$ apt-get install python python-pip`
- Ensure you have NodeJS & NPM installed:
    - mac: `$ brew install node`
    - *nix: `$ apt-get install nodejs`
- `git clone https://github.com/EntelekiaLearning/Website.git`
- change to the project's root directory and run:
```shell
$ sudo ./install.sh
$ ./run.sh
```
- Direct your browser to localhost:8000 to see `It works!` and localhost:5000/api/v1 to see `{"hello": "world!"}`
