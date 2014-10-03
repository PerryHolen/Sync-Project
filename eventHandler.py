#Perry Holen
#Event Handler that creates a changelog for the specified directory




import sys
import time
from time import strftime

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

'''
Extend FileSystemEventHandler to be able to write custom on_any_event method
'''
class MyHandler(FileSystemEventHandler):


    def on_created(self, event):

        srcPathSplit = event.src_path.split("\\")
        fileName = srcPathSplit[-1]
        if (fileName[0]!="~"):
            log = ["A" , event.src_path.encode("ascii") , 
                    strftime("%Y-%m-%d %H:%M:%S")]

            print log

# Git Testing
        #More Testing stuff for branches

    def on_deleted(self, event):

        srcPathSplit = event.src_path.split("\\")
        fileName = srcPathSplit[-1]
        if (fileName[0]!="~"):
            log = ["R" , event.src_path.encode("ascii") , 
                    strftime("%Y-%m-%d %H:%M:%S")]

            print log


    def on_modified(self, event):

        srcPathSplit = event.src_path.split("\\")
        fileName = srcPathSplit[-1]
        if (fileName[0]!="~"):
            log = ["M" , event.src_path.encode("ascii") , 
                    strftime("%Y-%m-%d %H:%M:%S")]

            print log


    def on_moved(self, event):

        srcPathSplit = event.src_path.split("\\")
        fileName = srcPathSplit[-1]
        destPathSplit = event.dest_path.split("\\")
        destName = destPathSplit[-1]

        if (fileName[0]!="~" and destName[0]!="~"):
            log = ["C" , event.src_path.encode("ascii") , 
                    event.dest_path.encode("ascii"), 
                    strftime("%Y-%m-%d %H:%M:%S")]

            print log


watch_directory = sys.argv[1]       # Get watch_directory parameter

event_handler = MyHandler()

observer = Observer()
observer.schedule(event_handler, watch_directory, True)
observer.start()

'''
Keep the script running or else python closes without stopping the observer
thread and this causes an error.
'''
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()