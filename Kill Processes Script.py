import os, signal

def process():
    name = input("Enter process name: ")
    try:
        
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
            fields = line.split()
            
            pid = fields[0]
            
            os.kill(int(pid), signal.SIGKILL)
        print("Process successfully terminated")
        
    except:
        print("Error encountered while running script")
process()