import os


version = "3.3.0"  # major.minor.patch
commands = ["open calc", "say hello", "kill ousama", "exit", "help"]

print(f"you are running {version}")

usr_input = input("enter command: ")
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
if usr_input == "exit":
    print("exiting...")
    exit()
if usr_input == "help":
    print("available commands:")
    for command in commands:
        print(f"- {command}")
