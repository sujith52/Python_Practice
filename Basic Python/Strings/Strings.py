str1 = 'the normal string '
str2 = "the double intend string"
str3 = '''
multilined string bro !
hello
halo
'''
str4 = """the quotes string 'sujith' and 'kumaar' """
print(str1,str2,str4,str3)

string1 = 'Hello world'
print('String with single quote', string1)

string2 = "sujith kuamr 'Software developer !'"
print(string2)

strs = "Sujith"
real_str = "H" + strs[1:] +"gavatha"
print(real_str)

main1 = "sujith"
main2 = "sreejas"
full = main1 + " : "+main2
print(full)

join1 = "lathas"
join2 = "sreejas"
fulls = " ".join([join1,join2])
print(fulls)

print(len("Length of the string"))

# string interpolation !!!!💀
name = "sujith"
age = 22

format_string1 = "my name is %s and i am %d old bro !" %(name,age)
format2 = "my name is {} and {} old bros".format(name,age)
format3 = f"my name is {name} and i am handsome and i am {age} old tammudu !" #f string method my fav
print(format_string1)
print(format3)
print(format2)

original = "i dont know what i am doing AbbAA !"
print(f"lower cases is : {original.lower()}")
print(f"upper case is {original.upper()}")

print(original[1:15])
print(original[1::2])
dummy = "alalalal"
print(dummy[::2])

sunstr = "what"
print(sunstr in original)
sunstrs = "whats"
print(sunstrs in original)

print(original.split("A")) #A is delimiter removing the words after the word !

spaced = "      hello world     "
print(spaced)
print(spaced.strip())

localtxt = "hello, world\nWelcome to the python! Welcome Welcome Welcome"
print(localtxt.split())
print(localtxt.splitlines())

print(f"reversed string is : {localtxt[::-1]}")

print(localtxt.replace("Welcome", "You dont welcome here !",2))

text = "i love python java and everything !"
print(text.find("suijth"))

try:
    print(text.index("sujith"))
except ValueError:
    print('the substring was not found in here bro !')

print(f"the word a appears {text.count("t")} times in the scentence!")

print(text.startswith("i"))
print(text.startswith("love"))
print(text.endswith("bro"))
print(text.endswith("!"))

print(f"Hello my name is {name} and this is the concepts of the \n python \t bye !!")
