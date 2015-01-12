#Entelekia

#####One place to find local opportunities and digital resources to help you learn about anything.

## Notes:
- This project is very young and a M.V.P. is currently in the works.
- The website/webapp only works on Mac (using [brew](http://brew.sh/)) and *nix (using [apt](https://wiki.debian.org/Apt)) at the moment.

## Installation:
- Ensure you have Python with Pip installed:
    - mac: `$ brew install python` & `$ easy_install pip`
    - *nix: `$ apt-get install python python-pip`
- Ensure you have NodeJS & NPM installed:
    - mac: `$ brew install node`
    - *nix: `$ apt-get install nodejs`
- `$ git clone https://github.com/EntelekiaLearning/Website.git && cd Website`
- `$ sudo ./install.sh && ./run.sh`

...then open your browser to `localhost:5000/` to see the homepage (with `test dynamic content!` from JavaScript in the console) and `localhost:5000/api/v1/test` to see `{"status": 1}`