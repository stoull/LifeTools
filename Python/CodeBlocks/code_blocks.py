import logging
import threading
import sys

class ProcessIndicate:
    """docstring for Decorators"""
    def __init__(self):
        self._stop = False

    def _loading_progress(self):
        i = 0
        # sys.stdout.write("Task is runing... ")
        while self._stop == False:
            if (i % 4) == 0:
                sys.stdout.write('\b-')
            elif (i % 4) == 1:
                sys.stdout.write('\b\\')
            elif (i % 4) == 2:
                sys.stdout.write('\b|')
            elif (i % 4) == 3:
                sys.stdout.write('\b/')
            sys.stdout.flush()
            time.sleep(0.4)
            i+=1
        print("Done!")

    def end(self):
        self._stop = True

    def start(self):
        processing_loading_thread = threading.Thread(target=self._loading_progress, daemon=False)
        processing_loading_thread.start()


if __name__ == "__main__":

    def run_tasks():
        time.sleep(10)

    a_indicate = ProcessIndicate()
    a_indicate.start()
    run_tasks()
    a_indicate.end()