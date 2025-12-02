filename = 'text.txt'

invalidIDs = 0

def repeatDigits(number):
    
    num = str(number)    
    length = len(num)
    
    if length < 2 or length % 2 != 0:
        return 0

    if num.startswith('0'):
        return 0

    half_length = length // 2
    
    first_half = num[:half_length]
    
    expected = first_half * 2
    
    if expected == num:
        return number
    else:
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