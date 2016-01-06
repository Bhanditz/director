from datatools import listBuilder, filmEnter, dictAdd

directors=["Chaplin, Charles", "Eastwood, Clint", "Kurosawa, Akira"]
json_master=[]


dirdum=[]
produm=[]
edidum=[]
wridum=[]
actdum=[]


listBuilder(dirdum, directors, 'director')
listBuilder(produm, directors, 'producer')
listBuilder(edidum, directors, 'editor')
listBuilder(wridum, directors, 'writer')
listBuilder(actdum, directors, 'actor')



for elmt in dirdum:
    if elmt == '-':
        continue
    if type(elmt) == str:                       #finds director name
        entry = {"name": 0, "nofilms": 0, "films": []}  #makes new dict
        entry['name'] = elmt                    #puts director name in dict
    else:
        filmEnter(elmt, 'director', dirdum, entry, json_master, True)

dictAdd(actdum, json_master, 'actor')
dictAdd(produm, json_master, 'producer')
dictAdd(edidum, json_master, 'editor')
dictAdd(wridum, json_master, 'writer')

for elmt in json_master:
    count = len(elmt['films'])
    elmt['nofilms'] = count
    print elmt['name']


'''                                       #makes film entry
        filmentry = {"title":elmt[0], "year":elmt[1], "credits":['director']}
        entry["films"].append(filmentry)
        next_index = dirdum.index(elmt) +1
        if type(dirdum[next_index]) == str:     #sees when another director comes up
            json_master.append(entry)           #adds dict to mast director list
    print entry, '\n'

cont = False
dirindex = 0
tempfilms=0
filmin = True
for elmt in produm:
    failno=0
    if elmt == '-':
        continue
    if type(elmt) == str:
        cont = True
        for item in json_master:
            if item["name"] == elmt:
                dirindex = json_master.index(item)
                tempfilms = len(json_master[dirindex]["films"])
                break
    if cont == True:
        for film in json_master[dirindex]["films"]:
           # print elmt , film["title"], elmt[0] == film["title"]
            if elmt[0] == film["title"]:
                if 'producer' in film["credits"]:
                    break
                film["credits"].append('producer')
                failno=0
                break
            failno=failno+1
        #have a fail value here
    if failno == tempfilms: #need a better fail conditional
        filmEnter(elmt, 'producer', produm, json_master[dirindex], json_master)

    next_index = produm.index(elmt) +1
    if type(produm[next_index]) == str:
        cont = False

    '''








