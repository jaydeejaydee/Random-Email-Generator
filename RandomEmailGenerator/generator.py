from random import choice, randint


def readFile(fn):
    rd = open (fn, "r")
    out = rd.readlines()
    rd.close()
    return [x.strip().lower() for x in out] 

words = readFile("words.txt")
names = readFile("names.txt")

def getFirstName():
    return choice(names).split()[0]

def getLastName():
    return choice(names).split()[1]

def getWord():
    return choice(words)


def randomOrder():
    order = 0
    while True:
        s = str(randint(10, 55555))
        if "6" in s or "7" in s or "8" in s or "9" in s or s.count("0") > 1 or s.count("1") > 1:
            continue
        order = s
        break
    return(order[:randint(2, 4)])


def randomEmail():
    try:
        special = "~!@#$%^&*()_+-={}//\\:<>?[];',."
        email = ""
        order = randomOrder()
        for c in order:
            if c == "0":
                email += getFirstName()
            if c == "1":
                email += getLastName()
            if c in "24" or c == str(randint(-10,15)):
                email += getWord()
            if c == "5":
                email += getLastName()
            if c == "3" or c == str(randint(-10,15)):
                email += str(randint(0, 9999))[:randint(1, randint(2, 4))]
        if len(email) <= 6 or len(email) > randint(randint(10, 15), randint(15, 30)):
            return randomEmail()
        return ''.join([i for i in email if i not in special]) + randomDomain()
    except:
        return randomEmail()
	

def randomDomain():
    choices = 'yahoo outlook live aol hotmail msn '
    choices *= 3
    choices += 'gmail ' * 12
    choices += 'mail icloud'
    return '@' + choice(choices.split()) + '.com'


for i in range(100):
    print(randomEmail())
