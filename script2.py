import platform
import os
from datetime import datetime
import getpass

student_name = "Aritra Chowdhury"
software = "Python"

print("========================================")
print(f"   Open Source Audit — {student_name}")
print("========================================")

print("Software :", software)
print("Distro   :", platform.platform())
print("Kernel   :", platform.release())
print("User     :", getpass.getuser())
print("Home Dir :", os.path.expanduser("~"))
print("Date     :", datetime.now())

print("License  : Python is licensed under PSF License")
print("========================================")
