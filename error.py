try:
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

