malid3
======

malid3 is a web app designed in Python using the Flask framework for manually tracking changes made to music files. The general layout and functions were based off of the [Flaskr tutorial](http://flask.pocoo.org/docs/tutorial/introduction/), with extra columns added to the database and JQuery implementation to allow for easy navigation among options.

![malid3_add_overhaul](https://cloud.githubusercontent.com/assets/6787907/3452244/130645e8-01ae-11e4-823f-2621c7742754.png)
![malid3_add_overhaul2](https://cloud.githubusercontent.com/assets/6787907/3452243/1305fd22-01ae-11e4-9284-ed279f040bae.png)

Quickstart
======

If you already have git, pip, and virtualenv:
```sh
$ git clone https://github.com/brycematsuda/malid3.git
$ cd malid3
$ virtualenv venv
$ . venv/bin/activate
```

To run:
```sh
(venv)$ malid3.py
```
and go to http://localhost:5000 in your browser. 
The login info for now is the default set by the tutorial (user: admin / password: default).

Project Setup
======
#### Download this repository from github.
```sh
$ git clone https://github.com/brycematsuda/malid3.git
```
If you don't have git,
```sh
$ sudo apt-get install git
```
For more information, see https://help.github.com/articles/set-up-git .

#### Install Pip
Install pip, which is a [package management](http://en.wikipedia.org/wiki/Package_management_system) system for Python, similar to gem or npm for Ruby and Node, respectively. 

```sh
$ easy_install pip
```

#### Now install [virtualenv](https://pypi.python.org/pypi/virtualenv) to create an isolated environment for development. 

This is standard practice. Always, always, ALWAYS use virtualenv. If you don't, you will eventually run into problems with compatibility between different dependencies. Just do it.

```sh 
$ pip install virtualenv
```

#### Activate your virtualenv.

```sh
$ virtualenv venv --distribute --no-site-packages
$ source venv/bin/activate
```

> You know that you are in a virtual env, as the actual "env" is now show before the $ in your terminal - (env). To exit the virtual environment, use the command `deactivate`, then you can reactivate by navigating back to the directory and running - `source env/bin/activate`.

Note: --no-site-packages may not be needed, you will get a message saying
"The --no-site-packages flag is deprecated; it is now the default behavior."

Note: You should NOT have spaces in the path to this directory! Otherwise you
may encounter errors such as
```sh
Error [Errno 2] No such file or directory while executing command ".
```

Credits
=======
Most of the setup documentation was taken from [flaskr-tdd](https://github.com/mjhea0/flaskr-tdd) and [WTFisThisRegister](https://github.com/nouyang/WTFisThisRegister).
