import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program ran on "+time.ctime())
while(break_count < total_breaks) :
    time.sleep(60 * 60 * 2)
    webbrowser.open("https://video2.timewarnercable.com/ondemand/featured")
    break_count = break_count + 1


