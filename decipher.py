#x is 5
#ma tanghao
#decipher
try:
    #readfile
    infile = open('MYSTERY.IN','r')
    x = -5
    message = ''
    #decipher
    for row in infile.readlines():
        for letter in row:
            message   += chr(ord(letter)+x) #shift each letter by x


    infile.close()
    #count number of words
    counts = {}
    wordlist=message.split(' ')
    
    for word in wordlist:
        lword=word.lower()
        if counts.has_key(lword):
            counts[lword] += 1
        else:
            counts[lword] = 1
    #delete irrelevant words(mostly prepositions)
    triviallist=['and','to','the','of','a','our','in','this','can','will','we','for','as','is','on','are','singaporeans','singaporean']
    for word in triviallist:
        del counts[word]

    #find the max for 3 times
    top=''
    for i in range(3):
        maxs = ['',0]
        for key in counts.keys():
            if maxs[1]<counts[key]:
                maxs[0]=key
                maxs[1]=counts[key]
            
        top+=maxs[0]+' '
        #delete the max ,do again
        del counts[maxs[0]]
               
    #output

    try:
        outfile=open('RESULT.OUT','w')
        outfile.write(top)
        outfile.close()
    except:
        print('cannot load file')
except :
    print('cannot loadfile!')
