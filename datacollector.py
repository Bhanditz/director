from datatools import listBuilder, filmEnter, dictAdd
import io, codecs, json

directors=["Chaplin, Charles", "Eastwood, Clint", "Kurosawa, Akira",
"Scorsese, Martin", "Coen, Ethan"]
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
    orderlist = sorted(elmt["films"], key=lambda k: k['year'])
    elmt['films'] = orderlist
    print elmt['name']



with io.open('data.json','w', encoding = 'utf-8') as f:
    data = json.dumps(json_master, ensure_ascii=False).decode('iso-8859-1')
    f.write(data)









