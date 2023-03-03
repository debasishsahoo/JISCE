import subprocess  
  
with open("output.txt", "wb") as f:  
    subprocess.check_call(["python", "temp.py"], stdout=f)  
