input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

try: 
    file1 = open(input_file, "r")
    lines = file1.readlines()
    line_count = len(lines)
    first_two_lines = lines[:2]
    file1.close()
 
    file2 = open(output_file, "w") 
    file2.writelines(first_two_lines) 
    file2.close()
 
    print("---------------------------------------------")
    print("Total number of lines:", line_count)
    print("---------------------------------------------")
    print("First two lines:")
    print("---------------------------------------------")

    for line in first_two_lines:
        print(line, end="")

    print("---------------------------------------------")
    print("First two lines written to:", output_file)
    print("---------------------------------------------")

except FileNotFoundError:
    print("---------------------------------------------")
    print("Input file not found!")
    print("---------------------------------------------")
