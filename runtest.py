import schedule
import time
from test import A


class B:
    def some_method(self):
        obj_a = A()
        schedule.every(3).seconds.do(test_method())
        while True:
            schedule.run_pending()
            time.sleep(1)
