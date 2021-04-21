from celery import Task

class baseclass(Task):
    def __init__(self, problem):
        super().__init__()
        self.problem = problem

        self.name = problem

    def get_task(self):
        if self.problem == "add":
            return "addition"

        elif self.problem == "sub":
            return "subraction"
    
    def repeat(self, times):
        name = self.get_task()
        return name*times

    def run(self, times):
        return self.repeat(times)
