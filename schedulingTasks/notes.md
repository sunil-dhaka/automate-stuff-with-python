## cron tutorial
- https://towardsdatascience.com/create-your-first-cronjob-on-the-linux-server-74e2fdc76e78

## points
- Your computer’s clock can sched-
ule programs to run code at some specified time and
date or at regular intervals. For example, your pro-
gram could scrape a website every hour to check for
changes or do a CPU-intensive task at 4 am while you
sleep. Python’s time and datetime modules provide these
functions.

- The time.sleep() function will block—that is, it will not return and release
your program to execute other code—until after the number of seconds you
passed to time.sleep() has elapsed. For example, if you enter time.sleep(5) y,
you’ll see that the next prompt ( >>>) doesn’t appear until five seconds have
passed.
- Be aware that pressing ctrl -C will not interrupt time.sleep() calls
in IDLE. IDLE waits until the entire pause is over before raising the
KeyboardInterrupt exception. To work around this problem, instead of hav-
ing a single time.sleep(30) call to pause for 30 seconds, use a for loop to
make 30 calls to time.sleep(1).
- The webbrowser.open() function can launch a web browser from your pro­
gram to a specific website, rather than opening the browser application
with subprocess.Popen()
- The sole exception is that you don’t want passwords passed as command
line arguments, since the command line may record them as part of its com-
mand history feature. Instead, your program should call the input() function
when it needs you to enter a password.

## datetime
```py
import datetime
datetime.datetime.now()
datetime.datetime.fromtimestamp() # epoch time as input

```

- datetime objects can be compared with each other using comparison
operators to find out which one precedes the other. 
    - this time comparision can be used in a programme to keep it from executing. helps in scheduling tasks at specific time

- The datetime module also provides a timedelta data type, which represents a
duration of time rather than a moment in time.

- timedelta objects can be added or subtracted with datetime objects or
other timedelta objects using the + and - operators. A timedelta object can be
multiplied or divided by **integer or float(scalars)** values with the * and / operators.

- **Converting datetime Objects into Strings:** Use the strftime() method to display a datetime object as a string. (The
`f` in the name of the strftime() function stands for format.)

- **Converting Strings into datetime Objects:**  The strptime() function is the inverse
of the strftime() method. A custom format string using the same direc-
tives as strftime() must be passed so that strptime() knows how to parse
and understand the string. (The `p` in the name of the strptime() function
stands for parse.)
- The
string with the date information must match the custom format string
exactly, or Python will raise a ValueError exception.


|   strftime directives     |   Meaning  |
|---------------------------|------------|
|   %Y  |    Year with century, as in '2014'|
|   %y  |    Year without century, '00' to '99' (1970 to 2069)|
| %m |  Month as a decimal number, '01' to '12'|

- visit official datetime docs for full-list

A Unix epoch timestamp (used by the time module) is a float or integer
value of the number of seconds since 12 am on January 1, 1970, UTC.
A datetime object (of the datetime module) has integers stored in the
attributes year, month, day, hour, minute, and second.
A timedelta object (of the datetime module) represents a time duration,
rather than a specific moment.
Here’s a review of time functions and their parameters and return values:
The time.time() function returns an epoch timestamp float value of the
current moment.
The time.sleep(seconds) function stops the program for the amount of sec-
onds specified by the seconds argument.
The datetime.datetime(year, month, day, hour, minute, second) function
returns a datetime object of the moment specified by the arguments. If
hour, minute, or second arguments are not provided, they default to 0.
The datetime.datetime.now() function returns a datetime object of the cur-
rent moment.
The datetime.datetime.fromtimestamp(epoch) function returns a datetime
object of the moment represented by the epoch timestamp argument.
The datetime.timedelta(weeks, days, hours, minutes, seconds, milliseconds,
microseconds) function returns a timedelta object representing a duration
of time. The function’s keyword arguments are all optional and do not
include month or year.
The total_seconds() method for timedelta objects returns the number of
seconds the timedelta object represents.
The strftime(format) method returns a string of the time represented by
the datetime object in a custom format that’s based on the format string.
The datetime.datetime.strptime(time_string, format) function returns a
datetime object of the moment specified by time_string, parsed using the
format string argument.

## Popen from subprocess
- Your Python program can start other programs on your computer with the
Popen() function in the built-in subprocess module. (The P in the name of
the Popen() function stands for process.)

- poll()
- wait()

- The first string in
this list will be the executable filename of the program you want to launch;
all the subsequent strings will be the command line arguments to pass to
the program when it starts. In effect, this list will be the value of sys.argv
for the launched program.

- open using `default application`
```py
>>> import subprocess
>>> subprocess.Popen(['see', 'hello.txt'])
# for linux only 'see' 
# for windows 'start' and mac it is 'open'
```