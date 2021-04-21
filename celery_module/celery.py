from __future__ import absolute_import

from celery import Celery
from celery.app.registry import TaskRegistry
from celery_module.celery_task_class import baseclass
from celery_module.config import Config

app = Celery("celery_module",
            broker="redis://", 
            backend="redis://")

registry = TaskRegistry()
for model in Config.models:
    app.tasks.register(baseclass(problem=model["problem"]))

if __name__ == '__main__':
    app.start()
    app.autodiscover_tasks()
