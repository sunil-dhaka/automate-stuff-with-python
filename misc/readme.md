**one wat to execute unix terminal commands in python**
- using `subprocess.call()` method
```py
import subprocess
# stdout etc are optional, when don't want to show output result
subprocess.call(['cd','dir-path'],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
subprocess.call(['ls','-la','dir-path'])
```