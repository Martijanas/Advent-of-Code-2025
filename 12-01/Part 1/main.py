filename = 'text.txt'

start = 50
password = 0

try:
    with open(filename, 'r') as file:
        
        for line in file:
            
            stripped_line = line.strip()

            if not stripped_line:
                continue
            
            if stripped_line.startswith('L'):

                if int(stripped_line[1:]) < 100:

                    diff = abs(int(stripped_line[1:]) - start)
                    start = start - int(stripped_line[1:])

                    if start < 0:
                        start = 100 - diff

                    if start == 0:
                        password = password + 1

                    print("Dial point is not at: ", start)

                elif int(stripped_line[1:]) > 99:

                    x = int(stripped_line[1:]) // 100

                    new_number = int(stripped_line[1:]) - x*100

                    diff = abs(new_number - start)
                    start = start - new_number

                    if start < 0:
                        start = 100 - diff

                    if start == 0:
                        password = password + 1

                    print("Dial point is not at: ", start)

            elif stripped_line.startswith('R'):

                if int(stripped_line[1:]) < 100:

                    diff = abs(int(stripped_line[1:]) - abs(100 - start))
                    start = start + int(stripped_line[1:])

                    if start > 99:
                        start = 0 + diff

                    if start == 0:
                        password = password + 1

                    print("Dial point is not at: ", start)

                elif int(stripped_line[1:]) > 99:

                    x = int(stripped_line[1:]) // 100

                    new_number = int(stripped_line[1:]) - x*100

                    diff = abs(new_number - abs(100 - start))
                    start = start + new_number

                    if start > 99:
                        start = 0 + diff

                    if start == 0:
                        password = password + 1

                    print("Dial point is not at: ", start)

        print(password)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")