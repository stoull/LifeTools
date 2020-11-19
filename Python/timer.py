import time
import sys


def countdown(count_time):
	c_time = count_time
	while count_time:
		mins, secs = divmod(count_time, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end='\r')
		time.sleep(1)
		count_time -= 1
	print(f"{c_time}s is over!")


def timer():
 for h in range(0, 24):
  for m in range(0, 60):
   for s in range(0, 60):
    time.sleep(1)
    print ("Elapsed time : %s:%s:%s" % (h, m, s), end="\r")

if __name__ == '__main__':
	inputs = sys.argv[1:]
	if inputs.count("countdown"):
		time_seconds = int(sys.argv[2])
		countdown(time_seconds)
	else:
		timer()