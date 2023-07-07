import subprocess


# Call external programs from python scripts
# Useful for automation scripts

# These helper methods are considered legacy
# Create an instance of the Popen class
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

# subprocess.run # This is a newer and preferred method
try:
    completed = subprocess.run(["python3", "Python_Standard_Library/other.py"], 
                            capture_output=True,
                            text=True,
                            check=True) # On True, the output will not be printed on terminal
    print("args: ", completed.args)
    print("returncode: ", completed.returncode) # Any none 0 = error
    print("stderr: ", completed.stderr)
    print("stdout: ", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)

try:
    completed = subprocess.run(["false"], 
                            capture_output=True,
                            text=True,
                            check=True) # On True, the output will not be printed on terminal
    print("args: ", completed.args)
    print("returncode: ", completed.returncode) # Any none 0 = error
    print("stderr: ", completed.stderr)
    print("stdout: ", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)