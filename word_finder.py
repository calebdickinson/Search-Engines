def find_line_number(filename, word):
    with open(filename, 'r') as file:
        lines = file.readlines()
        found = False
        for i, line in enumerate(lines):
            if word in line:
                print(f"Line {i + 1}: {line.rstrip()}")
                found = True
        if not found:
            print(f"The word '{word}' was not found in the file.")

filename = 'ChatWRD/lovecraft2.txt'  #filename = your filepath. I only tested this code on .txt files.
word = 'the'  #word = 'your string'. Any string can be used here. 
find_line_number(filename, word)
