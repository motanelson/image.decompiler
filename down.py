import os
down="https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-6.html"
print("\033c\033[47;31m\nfile: down.html")
os.system("curl "+down+" -o down.html")