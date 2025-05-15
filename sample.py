fileName = r"C:\Users\ADMIN\Downloads\sample.txt"
with open(fileName,"r") as file:
    lines  = file.readlines()
print("\n--- Sample lines from the file ---")
for i in range(min(10, len(lines))):  
 print(f"{i+1}: {lines[i].strip()}")
searchPhrase = input("Enter the search phrase: ").lower()

count = 0

for line in lines:
    if searchPhrase in line.lower():
        print(line.strip())
        count += line.lower().count(searchPhrase)
print(f"Total occurrences of '{searchPhrase}': {count}")
