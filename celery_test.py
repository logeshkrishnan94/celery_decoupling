import time
from celery_module.celery import app
from celery_module.celery_task_class import baseclass

def run_test():
    task1 = app.tasks["addition"]
    task2 = app.tasks["subraction"]

    result1 = task1.delay(times=3)
    result2 = task2.delay(times=4)

    # waiting for the task to complete
    while result1.ready() is not True:
        time.sleep(1)

    while result2.ready() is not True:
        time.sleep(1)

    prediction1 = result1.get(timeout=1)
    prediction2 = result2.get(timeout=1)
    print("The task returned this prediction: {}".format(prediction1))
    print("The task returned this prediction: {}".format(prediction2))

run_test()

# normal 
cls_obj = baseclass(problem="add")
res = cls_obj(3)
print(res)

#if __name__ == '__main__':
    
