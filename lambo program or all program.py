s="Hey there ! what should this string be ?"
print("Length of s=%d"%len(s))
print("The first occurance of the letter a=%d"%s.index("a"))
print("a occour %d times"%s.count("a"))
print("The First Five character are '%s'"%s[:5])
print("The Next Five character are '%s'"%s[5:5])
print("The thirteenth character is '%s'"%s[12])
print("The character with odd index are '%s'"%s[1::2])
print("The Last Five character are '%s'"%s[:-5])
print("String in uppercase: %s" %s.upper())
print("String in Lowercase: %s" %s.upper())
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
if s.endswith("ome"):
    print("String starts with 'ome'. Good!")
print("Split the words of the string:%s" %s.split(""))
