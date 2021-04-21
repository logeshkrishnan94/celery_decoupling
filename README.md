# Experiments

Module Structure:

celery_module - Module containing task, celery app (needed to initiate celery worker) and config
    __init__.py (created to avoid celery app import issue)
    celery_app.py (app initiation, broker and backend, task registration)
    celery_task_class.py (Task class definition)
    config.py (models for task registration)

celery_test.py (client test function to send input, get output)

Notes:

1. Inherited task object from celery, super().__init__() to intialize Task class,  