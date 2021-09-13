import subprocess

print(subprocess.Popen("echo Hello World", shell=True,
                       stdout=subprocess.PIPE).stdout.read())

input("...")
