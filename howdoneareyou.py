
filename = "testfile.py" # Will use the code to find the path in this part

count = 0
completion = 0
str1 = "maison"
str2 = "maison"

print(str1==str2)

def remove(string):
    return string.replace(" ","")

with open(filename) as f:
    content = f.readlines()

for line in content:
    line = remove(line)
    print(line)
    if line == "#done\n" or line == "#Done\n":
        completion = completion + 1
        count = count + 1
    elif line == "#todo\n" or line == "#Todo\n":
        count = count + 1

percent = (completion * 100) / count
print("We are done at:",percent)
print("we had",count,"task to do")

if percent<75:
    print("We have some way to go")
elif percent > 75 or percent == 75:
    print("We are almost done, one last push")
elif percent==100:
    print("we are done motherfucker")