import sys

if (len(sys.argv) < 2):
    exit()
i = 2
old_str = sys.argv[1]
while i < len(sys.argv):
    old_str = old_str + " " + sys.argv[i]
    i += 1
new_str = old_str[::-1]
new_str = new_str.swapcase()
print(new_str)
