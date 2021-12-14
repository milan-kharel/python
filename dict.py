#A dictionary is like a list, but more general. In a list, the index positions have to
#be integers; in a dictionary, the indices can be (almost) any type

#word = 'brontosaurus'
#d = dict()
#for c in word:
#    d[c] = d.get(c, 0) + 1
#print(d)


#dictionaries and files
#fname = input('Enter the file name: ')
#try:
#    fhand = open(fname)
#except:
#    print('File cannot be opened:', fname)
#    exit()   
#counts = dict()
#for line in fhand:
#    words = line.split()
#    for word in words:
#        if word not in counts:
#           counts[word] = 1
#        else:
#            counts[word] += 1   
#print(counts)


#advanced text parsing
import string
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
