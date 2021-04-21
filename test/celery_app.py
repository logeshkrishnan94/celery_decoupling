from __future__ import absolute_import

from celery import Celery
from celery.app.registry import TaskRegistry
from celery_task_class import templateClass

class Config(object):

    models = [
        {
            "problem": "add"
        },
        {
            "problem": "sub"
        }
    ]

app = Celery("celery_module",
            broker="redis://", 
            backend="redis://")

registry = TaskRegistry()
for model in Config.models:
    app.tasks.register(templateClass(problem=model["problem"]))

if __name__ == '__main__':
    app.start()

#decoupling task call and worker
