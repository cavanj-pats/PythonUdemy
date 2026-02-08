#challenge_Stopwatch.py
#2026-02-08

import time

class Stopwatch:
    def __init__(self):
        self._start_time=None
        self._elapsed_time = 0

    def start(self):
        if self._start_time is None:
            self._start_time = time.time()

    def stop(self):
        if self._start_time is not None:
            tp =  time.time() - self._start_time
            self._elapsed_time += tp
            self._start_time is None


    def reset(self):
        self._start_time = None
        self._elapsed_time = 0


    def get_elapsed_time(self):
        return self._elapsed_time

    def display_time(self):
        return time.ctime()
    


sw = Stopwatch()
sw.start()

#print(f"Current Time: {time.ctime()}",  end = "\r" )
time.sleep(2)

sw.stop()
print(sw.get_elapsed_time())
sw.start()
time.sleep(4)
sw.stop()
print(sw.get_elapsed_time())



