import subprocess,sys,time

def countDown(alarm_file,total_time=1): # in minutes
    total_time=total_time*60 # convert into seconds
    while(total_time>0):
        total_time-=1
        time.sleep(1)
    
    print('playing alarm for 10 secs.')
    alarm_=subprocess.Popen(['see',alarm_file])
    while(alarm_.poll() is None):
        time.sleep(1)
    print('alarm stopped')

if __name__=="__main__":
    if len(sys.argv)>1:
        file=sys.argv[1]
        try:
            total_time=sys.argv[2]
        except Exception:
            total_time=1
    else:
        print('give alarm file.')
        sys.exit()

    countDown(file,total_time)