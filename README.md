# Professional_Connection
## Prerequisite of this project for better work environment:
* Pycharm 
* Feel flexible with Pycharm Git

## Installing pip environment
[Create Virtualenv in Pycharm][create-env-link]
    

## Load all initial data
```commandline
python3 manage.py loaddata */fixtures/*.json
```
## Make all users password hashable
```commandline
python3 manage.py make_hash
```

[create-env-link]: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html