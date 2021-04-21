from celery import Task

class templateClass(Task):
    def __init__(self, problem):
        super().__init__()
        self.name = problem

    def run(self):
        return 0
