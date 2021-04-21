## Activate virtualenv

```virtualenv venv3 --python=python3```\
```source venv3/bin/activate```\
```pip install -r requirements.txt```

# Celery multiple tasks example

Module Structure:

celery_module - Module containing task, celery app (needed to initiate celery worker) and config

    celery.py (app initiation, broker and backend, task registration)

    celery_task_class.py (Task class definition)
    
    config.py (models for task registration)

test - Module containing celery_test, template class and celery_app

    celery_app.py (app initiation, broker and backend, task registration, model config)

    celery_task_class.py (Template class definition) 

## To run the example

* Start redis server for backend and broker using docker

```docker run -d -p 6379:6379 redis```

```redis-cli```

```ping``` -> PONG

* Run the following command from the root folder to start the celery worker

```celery -A celery_module worker --loglevel=INFO --pool threads```


## Changes made to run test with a template class

* Deleted the __init__ file and renamed celery_app to celery.py inside main celery module

* Created seperate folder for test and moved the celery.py and task_class inside

* Renamed celery.py to celery_app.py(import issue) and moved the config class inside celery_app.py

* Deleted all the attributes inside template class except name attribute and dummy run method

* Run the following command from the test folder to get the predictions

```python celery_test.py```
