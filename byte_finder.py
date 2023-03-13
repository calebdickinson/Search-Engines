def find_line_number(filename, byte_position):
    with open(filename, 'rb') as file:
        lines = file.readlines()
        position = 0
        for i, line in enumerate(lines):
            if position + len(line) >= byte_position:
                line_number = i + 1
                print(f"Line {line_number}: {line.decode().rstrip()}")
                return
            position += len(line)
        print(f"The byte position {byte_position} is not within the file.")

filename = 'ChatWRD/lovecraft2.txt'  #filename = your filepath. I only tested this code on .txt files.
byte_position = 200  #byte_position = your int. Any integer can be used here, signifying the position of the byte.
find_line_number(filename, byte_position)
