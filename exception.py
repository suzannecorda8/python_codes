# Prints all letters except 'e' and 'a'
i=0
name='suzannecorda'
while i<len(name):

    if name[i]=='e' or name[i]=='a':
        i=i+1
        continue
  
    print('letter:',name[i])
    i=i+1

