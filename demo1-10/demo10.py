def acronym(phrase):
    phrase = phrase.title()
    phrase = phrase.split()
    a = phrase[0]
    b = phrase[1]
    c = phrase[2]
    return a[0]+b[0]+c[0]

phrase=input()
print(acronym(phrase))