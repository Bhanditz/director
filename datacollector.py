from datatools import listBuilder, filmEnter

directors=["Kurosawa, Akira", "Eastwood, Clint"]
json_master=[]


dirdum=[]
produm=[]

listBuilder(dirdum, directors, 'director')
listBuilder(produm, directors, 'producer')




for elmt in dirdum:
    if elmt == '-':
        continue
    if type(elmt) == str:                       #finds director name
        entry = {"name": 0, "nofilms": 0, "films": []}  #makes new dict
        entry['name'] = elmt                    #puts director name in dict
    else:
        filmEnter(elmt, 'director', dirdum, entry, json_master)
        '''                                       #makes film entry
        filmentry = {"title":elmt[0], "year":elmt[1], "credits":['director']}
        entry["films"].append(filmentry)
        next_index = dirdum.index(elmt) +1
        if type(dirdum[next_index]) == str:     #sees when another director comes up
            json_master.append(entry)           #adds dict to mast director list
        '''

cont = False
dirindex = 0
for elmt in produm:
    if elmt == '-':
        continue
    if type(elmt) == str:
        cont = True
        for item in json_master:
            if item["name"] == elmt:
                dirindex = json_master.index(item)
        continue
    if cont == True:
        for film in json_master[dirindex]["films"]:
            if elmt[0] == film["title"]:
                film["credits"].append('producer')
            else:
                filmEnter(elmt, 'producer', produm, json_master[dirindex], json_master)
    next_index = produm.index(elmt) +1
    if type(produm[next_index]) == str:
        cont = False

    '''
    if type(elmt) == list:
        for item in json_master:
            for film in item['films']:
                if elmt[0] == film['title']:
                    film['credits'].append('producer')
'''








