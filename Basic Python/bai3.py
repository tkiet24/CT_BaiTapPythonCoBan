inputStr = input("Enter a text: ")
print(f"Length of {inputStr} is {len(inputStr)}\n")
print(f"{inputStr} in uppercase is {inputStr.upper()}")
print(f"{inputStr} in uppercase is {inputStr.lower()}")

reverseStr = inputStr[::-1]
print(f"{inputStr} in reverse is {reverseStr}\n")