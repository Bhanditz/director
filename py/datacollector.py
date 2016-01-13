from datatools import listBuilder, filmEnter, dictAdd
import io, codecs, json

directors=["Chaplin, Charles", "Eastwood, Clint", "Kurosawa, Akira",
"Scorsese, Martin", "Coen, Ethan", "Kubrick, Stanley", "Welles, Orson",
"Allen, Woody", "Spielberg, Steven","Hitchcock, Alfred (I)", "Bergman, Ingmar",
"Godard, Jean-Luc", "Fellini, Federico", "Tarantino, Quentin",
"Keaton, Buster (I)", "Coppola, Sofia", "Ephron, Nora", "Heckerling, Amy",
"Lang, Fritz (I)", "Renoir, Jean", "Herzog, Werner (I)",
"von Trier, Lars", "Rodriguez, Robert (I)", "Hawks, Howard", "Wong, Kar-wai"]

female=["Ephron, Nora", "Heckerling, Amy", "Coppola, Sofia"]

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
listBuilder(actdum, female, 'actresse') #add actress credits



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
    orderlist = sorted(elmt["films"], key=lambda k: k['year'])
    elmt['films'] = orderlist
    print elmt['name']

for elmt in json_master:
    count=[0,0,0,0,0]
    for film in elmt['films']:
        if 'director' in film["credits"]:
            count[0]+= 1
        if 'writer' in film["credits"]:
            count[1]+= 1
        if 'editor' in film["credits"]:
            count[2]+= 1
        if 'producer' in film["credits"]:
            count[3]+= 1
        if 'actor' in film["credits"]:
            count[4]+= 1
    rolecount=["dirno", "wrino","edino","prono","actno"]
    for i in range(len(rolecount)):
        elmt[rolecount[i]]=count[i]

clearlst=[]
cleardir=directors

for elmt in json_master:        #gets rid of doubles
    if elmt["name"] in cleardir:
        cleardir.remove(elmt['name'])
        if "(I)" in elmt['name']:
            ridI=elmt['name'].split("(",1)
            elmt['name']= ridI[0][:-1] #gets rid of (I)
        clearlst.append(elmt)

json_master=clearlst


with io.open('data.json','w', encoding = 'utf-8') as f:
    data = json.dumps(json_master, ensure_ascii=False).decode('iso-8859-1')
    f.write(data)
