# Day 8: Dictionaries and Maps

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input().strip())
    phonebook = {}
    
    for i in range(n):
        name, num = input().strip().split(" ")
        phonebook[name] = num

    while True:
        try:
            entry = input().strip()
            if entry in phonebook:
                print(entry, "=", phonebook[entry], sep =" ")
            else:
                print("Not found")
        except EOFError:
            break
    
