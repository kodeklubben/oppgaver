print('Hei, jeg er en datamaskin.')
print('Jeg er derfor kjempeflink i matematikk.')
print('Skal jeg vise deg?')
aar=2016
faar=int(input('Når er du født: '))
alder=aar-faar
print('Jeg regnet ut at alderen din er: ')
print(alder)

spm=input('Stemmer det at du er så gammel? ')
if spm=='ja':
    print('Der ser du, jeg er kjempeflink i matematikk')
else:
    alder-=1
    print('Da er du nok '+str(alder)+' år gammel')
