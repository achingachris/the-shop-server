# testing input from a text file
# f = open("test.txt", "r")
# print(f.read())
# print(f.readline())
# f.close()

filename = "test.txt"

with open(filename, 'r') as filehandle:
    for line in filehandle:
        print(line)