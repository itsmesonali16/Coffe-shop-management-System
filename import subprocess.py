#! C:/Users/DELL/AppData/Local/Programs/Python/Python37/python.exe
import subprocess
 
# if the script don't need output.
#subprocess.call("mainaftlog.php")
 
# if you want output
proc = subprocess.Popen("mainaftlog.php", shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout()
