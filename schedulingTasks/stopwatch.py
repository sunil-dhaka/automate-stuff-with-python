from os import stat
import time,sys

def stopwatch():
    print('Press ENTER to start stopwatch. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
    
    user_input=input()
    start_time=time.time()
    lap_counter=0
    times_=[start_time]
    print('Stopwatch Started.')
    while(True):
        try:
            user_input=input()
            curr_time=time.time()
            times_.append(curr_time)
            lap_counter+=1
            print(f'Lap: #{lap_counter} {round(times_[-1]-times_[0],2)} ({round(times_[-1]-times_[-2],2)})')
        except KeyboardInterrupt:
            print('Stop Stopwatch.')
            sys.exit()
if __name__=="__main__":
    stopwatch()