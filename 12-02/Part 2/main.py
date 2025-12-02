filename = 'text.txt'

invalidIDs = 0

def repeatDigits(number):

    num = str(number)    
    length = len(num)

    if num.startswith('0'):
        return 0
    
    if length < 2:
        return 0

    for x in range(1, (length // 2) + 1):
        if length % x == 0:

            first_digits = num[:x]
            expected = first_digits * int(length // x)

            if expected == num:                
                return number
            
    return 0

try:
    with open(filename, 'r') as file:        
        
        content = file.read()

        range_line = content.replace('\n', ',').strip(',')

        all_ranges = range_line.split(',')
        
        for range_str in all_ranges:
            
            cleaned_range_str = range_str.strip() 

            if not cleaned_range_str:
                continue


            try:
                start_str, end_str = cleaned_range_str.split('-')
                
                start_id = int(start_str)
                end_id = int(end_str)
                
                print(f"Processing range: {start_id} to {end_id}")
                
                for x in range(start_id, end_id + 1):
                    invalidIDs = invalidIDs + repeatDigits(x)
                
            except ValueError:
                print(f"Skipping malformed range: {cleaned_range_str}")

        print(invalidIDs)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")