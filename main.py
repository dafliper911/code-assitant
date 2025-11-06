import os


version = "3.2.0"  # major.minor.patch
commands = ["open calc", "say hello", "kill ousama"]

print(f"you are running {version}")

usr_input = input("what do you want to do: ")
if usr_input in commands:
    print(f"commiting command {usr_input}...")
else:
    print("invalid command")
if usr_input == "open calc":
    os.system("calc.exe")
if usr_input == "say hello":
    print("hello user!")
if usr_input == "kill ousama":
    print("ousama bin laden was sucsessfully assasinated")