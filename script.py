# This is a script for a tool that aims to filter lines from a text file by keyword
# It reads input.txt, keeps lines containing "PCR", and writes them to output.txt
# Author: Ian Anglin

# Step 1: Set the keyword we want to find

# Step 2: Open input.txt and read all the lines 

# Step 3: Check each line. If it contains the keyword, save it with its line number

# Step 4: Write the saved lines to output.txt

# Step 5: Print how many matches were found

print("Script is running!")
with open("output.txt", "w") as out:
    with open("input.txt") as f:
        for line_number, line in enumerate(f, start = 1):
            if "PCR" in line:
                print (f"line {line_number}: {line.strip()}")
                out.write (f"line {line_number}: {line.strip()}\n")
print ("Done. Output written to output.txt")

            
