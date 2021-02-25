# testing input from a text file
f = open("test.txt", "r")
print(f.read())
print(f.readline())
f.close()

f = open("a.txt", "r")
print(f.read())
print(f.readline())
f.close()

f = open("b.txt", "r")
print(f.read())
print(f.readline())
f.close()

f = open("c.txt", "r")
print(f.read())
print(f.readline())
f.close()

f = open("d.txt", "r")
print(f.read())
print(f.readline())
f.close()

f = open("e.txt", "r")
print(f.read())
print(f.readline())
f.close()

f = open("f.txt", "r")
print(f.read())
print(f.readline())
f.close()

print('Successfull Read and Print')

# filename = "test.txt"

# with open(filename, 'r') as filehandle:
#     for line in filehandle:
#         print(line)