import os
import sys

userdata = open("account.txt", "w")
username = input("Enter username: ")
password = input("Enter password: ")
userdata.write("username=" + username + "\n")
userdata.write("password=" + password)
userdata.close()

install_instaloader = "python -m pip install instaloader"
install_pyfiglet = "python -m pip install pyfiglet"

print("\n" + install_instaloader)
os.system(install_instaloader)
print("\n" + install_pyfiglet)
os.system(install_pyfiglet)
os.system("mkdir output")

input("\nInstaPhantom is ready for use! Press \"Enter\" to continue.")
