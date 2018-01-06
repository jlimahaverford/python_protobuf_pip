# python_protobuf_pip
A simple example, using protobuf to generate simple python classes, housed in a pip-installable package.

Why do it?

* Have a workflow that depends on using *pip* and *venv* to manage small interrelated projects?
* Want a simple shared repo that defines your data model?

How to do it?

* Define your model using in protobuf.
* Compile to python.
* Use a simple setup.py that indicates the protobuf dependency.
* Push your code.
* Install into your virtual environment using pip + git.

Demo:

```
JonathanLimaMBP:~ jonathanlima$ cd Projects/playground/
JonathanLimaMBP:playground jonathanlima$ source venv/bin/activate
(venv) JonathanLimaMBP:playground jonathanlima$ pip install -e git+https://github.com/jlimahaverford/python_protobuf_pip.git#egg=python_protobuf_pip

    Obtaining python_protobuf_pip from git+https://github.com/jlimahaverford/python_protobuf_pip.git#egg=python_protobuf_pip
      Updating ./venv/src/python-protobuf-pip clone
    Collecting protobuf (from python_protobuf_pip)
      Using cached protobuf-3.5.1-py2.py3-none-any.whl
    Requirement already satisfied: setuptools in ./venv/lib/python3.6/site-packages (from protobuf->python_protobuf_pip)
    Requirement already satisfied: six>=1.9 in ./venv/lib/python3.6/site-packages (from protobuf->python_protobuf_pip)
    Installing collected packages: protobuf, python-protobuf-pip
      Running setup.py develop for python-protobuf-pip
    Successfully installed protobuf-3.5.1 python-protobuf-pip

(venv) JonathanLimaMBP:playground jonathanlima$ cd ~/Projects/python_protobuf_pip/
(venv) JonathanLimaMBP:python_protobuf_pip jonathanlima$ python script.py 

    player_one_id: 0
    player_one_character: CAPTAIN_FALCON
    player_two_id: 1
    player_two_character: DONKEY_KONG
    player_one_wins: true

(venv) JonathanLimaMBP:python_protobuf_pip jonathanlima$ which python

    /Users/jonathanlima/Projects/playground/venv/bin/python
```