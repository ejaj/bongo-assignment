# bongo-assignment
Python Code Test

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ejaj/bongo-assignment.git
$ cd bongo-assignment
```
Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

## For Testing
 ```sh
(env)$ pytest -vv
```