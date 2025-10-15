sen=str(input("enter a sentence: "))
let=str(input("enter a letter: "))
for i in range(0,100000):
    e=sen[i]
    if let == e:
        break
    print(e)