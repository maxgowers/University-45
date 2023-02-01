#www.101computing.net/python-typing-text-effect/
import time,os,sys,random
import MoinMoin

def type(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def choice(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")

def newLine():
  print("")

type("University 45: New Student Enrollment\n")
newLine()
time.sleep(1)
first = input("First Name: ")
last = input("Last Name: ")
home = input("Home Town: ")
username = first[0] + last

newLine()
type(f"{first} {last}, you have been enrolled sucessfully.\n")

type(f"Username: {username}\n")
type(f"Student ID: {str(random.randint(100000000,150000000))}")

time.sleep(3)
clearScreen()

type(f"{username} is logging into 45Chat...")

newLine()
type("New message from: System Admin")
newLine()
type(f"Welcome to 45Chat, {username}.\n")
type("This platform is to be used to communicate with peers, form groups, and recieve information about assignments. Please be sure to read the [[www.google.com|Terms and Conditions]].")