def write_to_file():
    user_input = input("Enter text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(user_input + '\n')
    print("Data successfully written to output.txt.")
def append_to_file():
    additional_input = input("Enter additional text to append: ")
    with open('output.txt', 'a') as file:
        file.write(additional_input + '\n')
    print("Data successfully appended.")

def read_file():
    print("\nFinal content of output.txt:")
    with open('output.txt', 'r') as file:
        print(file.read())

write_to_file()
append_to_file()
read_file()