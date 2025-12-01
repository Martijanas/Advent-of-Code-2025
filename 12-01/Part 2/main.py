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

                    if start == 0:
                        start = 100 - int(stripped_line[1:])
                        print("Dial point is at: ", start)
                        print(password)
                        continue

                    start = start - int(stripped_line[1:])

                    if start < 1:
                        if diff == 0:
                            start = 0
                            password = password + 1
                        else:
                            start = 100 - diff
                            password = password + 1

                    print("Dial point is at: ", start)
                    print(password)

                elif int(stripped_line[1:]) > 99:

                    x = int(stripped_line[1:]) // 100

                    new_number = int(stripped_line[1:]) - x*100

                    diff = abs(new_number - start)

                    if start == 0:
                        start = 100 - new_number
                        password = password + x
                        print("Dial point is at: ", start)
                        print(password)
                        continue

                    start = start - new_number

                    if start < 0:
                        start = 100 - diff

                        if start != 0:
                            password = password + 1

                    if start == 0:
                        password = password + 1

                    password = password + x

                    print("Dial point is at: ", start)
                    print(password)

            elif stripped_line.startswith('R'):

                if int(stripped_line[1:]) < 100:

                    diff = abs(int(stripped_line[1:]) - abs(100 - start))
                    start = start + int(stripped_line[1:])

                    if start > 99:
                        start = 0 + diff
                        password = password + 1

                    print("Dial point is at: ", start)
                    print(password)

                elif int(stripped_line[1:]) > 99:

                    x = int(stripped_line[1:]) // 100

                    new_number = int(stripped_line[1:]) - x*100

                    diff = abs(new_number - abs(100 - start))
                    start = start + new_number

                    if start > 99:
                        start = 0 + diff

                        if start != 0:
                            password = password + 1

                    if start == 0:
                        password = password + 1

                    password = password + x

                    print("Dial point is at: ", start)
                    print(password)

        print(password)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")