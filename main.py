version = "3.0.0"  # major.minor.patch
commands = ["open calc", "say hello", "kill ousama"]


print(f"you are running {version}")

usr_input = input("what do you want to do: ")
if usr_input in commands:
    print(f"commiting command {usr_input}...")
else:
    print("invalid command")