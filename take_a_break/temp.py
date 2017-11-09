
import time
import sys
import webbrowser

start_time = time.ctime()
max_time = 20 * 60	# 20 minutes
break_count = 0

while(True):
	time.sleep(max_time)
	webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
	break_count = break_count + 1

while (break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", 2)
	break_count = break_count + 1

