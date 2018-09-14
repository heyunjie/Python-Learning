###############            string       #############################
fruit = 'banana'
letter = fruit[0]
print(letter) # b
print(fruit[0:2])  # ban
print(fruit[:2])
print(fruit[2:])

# len()
len(fruit)

# traversal
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# Example: counting letter number in a word
word = input('The word')
count = 0
for letter in word:
    if letter == 'a':
        count = count +1
print('the total number of a in %s is %d'%(word,count))

# in:判断是否是substring
print('a' in 'banana')

# comparison between strings, 比首字母先后
word = 'apple'
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# dir() list available methods for an object
S = 'Hello World'
dir(S)
C = S.capitalize()  # object.method(...) in Python  ==   ## method(object,...) in R
print(C)


# frequently used methods in string
#1    .upper()
word = 'banana'
new_word = word.upper()

#2   .find()
index1 = word.find('a')          # 1st a
index2 = word.find('a',index1)   # 2nd a ;  index1 : search after index1

#3   .strip()
line = '    Here    we go'
line.strip()     #remove white space

#4   .startwith()
word.startwith('b') #TRUE
word.startwith('n') #FALSE


# Parsing strings
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
sppos = data.find(' ',atpos)
sub_string = data[atpos+1,sppos-1]
print(sub_string)

# Practise
data = 'X-DSPAM-Confidence:0.8475'
stpos = data.find(':')
num = data[stpos+1:]
num_float = float(num)
print('the number is %.4lf'%num_float)

#####################      files         ###############################
# open files
fhand = open('mbox.txt')
print(fhand)    #it gives a handle to the data

#1.For loops used to
fhand = open('mbox.txt')
print(fhand)    #it gives a handle to the data
count = 0
for line in fhand:
    count =  count +1
print('Line count:',count)
# search file: two methods
# if
for line in fhand:
    line = line.rstrip()    # removes the newline at the end
    if line.startswith('From:'):
        print(line)
# if not
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)


#2. make the whole text into a string including both texts and new lines
fhand = open('mbox-short.txt')
inp = fhand.read() # inp is a string
print(len(inp))


# try, except, and open
fname = input('Please input the file name')
try:
    fhand = open(fname)
except:
    print('The file doesnt exist')
    exit()
count = 0
for line in fhand:
    line = line.rstrip
    print(line)
    count = count + 1

# write files
fout = open('mbox.txt','w')
line1 = 'This here is a wattle,\n'
fout.write(line1)
fout.close()

# Debuging
s = '1\t2\t3\n4'
print(repr(s))  ## repr shows all invisible parts in objects

# Exercise:
#1.Write a program to read through a file and print the contents of the file (line by line) all in upper case.
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)

#2.Write a program to prompt for a file name, and then read through the file and look for lines of the form:
fname = input('please input the file name')
try:
    fhand = open(fname)
except:
    print('The file doesnt exist')
spam = 0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence'):
        line = line.rstrip()
        stpos = line.find(':')
        spam = spam + float(line[stpos+1:])
        count = count + 1
print('Average spam confidence is %lf'%(spam/count))

#####################         lists                  #######################
# list traversing
numbers = [17, 123]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

# list operation
a = [1,2,3]
b = [4,5,6]
c = a + b

# A list can also contain other lists
['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

## list methods
# .apend : append 1 new element
t = ['a','b','c']
t = t.append('d')  # t = [a,b,c,d]

# .extend : append many new elements
t = ['a','b','c']
t = t.extend(['d','e'])  # t = [a,b,c,d,e]

# .sort :  arranges the elements of the list from low to high
t = ['d', 'c', 'e', 'b', 'a']
t.sort() #[a,b,c,d,e]

# Deleting elements
## .pop : delete one elements in a list using index
t = ['a','b','c','d','e']
t.pop(1) # t.pop(1) = 'b'
         # t = ['a','c','d','e'] after deleting

## .remove: delete one element in a list using element name
t = ['a','b','c','d','e']
t.remove('b')

## del operator
t = ['a','b','c','d','e']
del t[1:3]

# split & joint
## .split() : breaks a string into individual letters
s = 'Roya is a genius'
s = s.split()
print(s)

## .split(delimiter)
s = 'spam-spam-spam'
s = s.split('-')
print(s)

## .join()
t = ['Roya','is','a','genius']
delimiter = ' '
t = delimiter.join(t)  ##insert ' ' into t as gaps
print(t)

# Exercise:  print out the day of the week from those lines that start with "From "
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        print(words[2])

##################        dictionaries       ###############################
# create a dictionary
eng2Deu = dict()
eng2Deu['one'] = 'ein'
print(eng2Deu)

eng2Deu = {'one':'ein','two':'zwei','three':'drei'}
print(eng2Deu)
print(eng2Deu['one'])
vals = eng2Deu.values()   ## vals is the dictionary values of eng2Deu: ein, zwei,drei

# use dictionary to count letters
words = "banana"
d = dict()
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] = d[word] + 1
print(d)

# .get()
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(counts.get('jan', 0))  #if jan is in counts, return 100, or return 0(the default value)
print(counts.get('tim', 'the value doesnt exist'))

# use dict in counting words in text
fname = input('please input the file name')
try:
    fhand = open(fname)
except:
    print('the file doesnt exist')
    exit()
count = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        count = count.get(word,0) + 1
#        if word not in count:
#            count[word] = 1
#        else:
#            count[word] = count[word] + 1


print(count)
# for loop & dictionary
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10 :
        print(key, counts[key])

#文本处理: .punctuation()
import string
string.punctuation()
line.translate(str.maketrans(fromstr, tostr, deletestr))


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) + 1
print(count)


## Exercise 1: summarize mbox-short.txt, then get {'Fri': 20, 'Thu': 6, 'Sat': 1}
import string
fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.rstrip()
        words = line.split()
        if len(words) > 2:
            word = words[2]
            counts[word] = counts.get(word,0) + 1
print(counts)

#Exercise 2: Write a program to read through a mail log, build a histogram using a dictionary
#to count how many messages have come from each email address, and print the dictionary.
import string
fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.rstrip()
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word,0) + 1
print(counts)

########################     Tuples              ##########################
# tuple is a sequence of values much like a list.
t = ('a','b','c','d')
t1 = ('a',)    # t1 is a tuple
t2 = ('a')     # t2 is a string
t3 = tuple('lupins')
print(t3)      # ('l','u','p','i','n','s')

# tuple is immutable, unlike list, you cannot alter things in it
t[0] = 'A'  #ERROR

#tuples and assignments
(x,y) = (1,'fred')

# .items(): from tuples to list;  tuples and dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
tups = d.items()   # dict_items([('csev', 2), ('cwen', 4)]) is a list of 2 tuples
for (k,v) in d.items():
    print(k,v)

# sorted():
c = {'a':10,'c':1,'b':22}
sorted(c.items())

#comapring tuples
(0,1,20000) < (0,2,1) # TRUE
# comparing rule: comparing the first element from each sequence.
# If they are equal, it goes on to the next element, and so on, until it finds elements that differ.

# Make a histogram for text words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
lst = list()
for v,k in counts.items:
        newsetup = (k,v)
        lst.append(newsetup)
lst = sorted(lst,reverse = True)
for k,v in lst[:10]:
    print(k,v)
#
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)
print(res)

#This program counts the distribution of the hour of the day for each of the messages.
#You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character.
#Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
fhand = open('mbox-short.txt')
count = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.rstrip()
        words = line.split()
        if len(words) > 4:
            word = words[5]
            word.split()
            hour = word[:2]
            count[hour] = count.get(hour,0) + 1
print(sorted(count.items()))
