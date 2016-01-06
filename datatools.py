def listBuilder(poplst, dirlist, role):
    '''
    Builds a list, which will be used to make the dictionary. Searches imdb
    text files for directors and the roles the played in movies.
        poplst is the list that will hold directors and their movies
        dirlist is the list of directors we're interesd in
        role is either director, producer, editor, writer, or actor
    '''
    filestr = role+"s-list/"+role+"s.list"
    with open(filestr) as fileobject:
        cont = False
        for line in fileobject:     #goes line by line in file
            for elmt in dirlist:    #loops through names of directors
                if elmt in line:    #locates a director
                    if '(I)\t' in line:
                        name_sep = line.split('(I)\t')
                    if '\t\t' in line:
                        name_sep = line.split("\t\t")     #split director name
                    else:
                        name_sep = line.split('\t')
                    #print name_sep
                    title_sep = name_sep[1].split("(",1) #split title
                    poplst.append(name_sep[0])          #add director name
                    cont = True
                    skip = checkYear(title_sep)         #check if first
                    if skip == True:                    #   title is trash
                        continue
                    dummy=[title_sep[0][:-1], int(title_sep[1][:4])]
                    poplst.append(dummy)               #add [first title, year]
            if cont== True:         #works for lines other than the first one
                if line == '\n':
                    cont = False    #skips line b/c it's the end of a director
                else:
                    title_sep = line[:-1].split("\t\t\t") #split title
                    skip = checkYear(title_sep)
                    if skip == True:
                        continue
                    year_sep = title_sep[1].split("(",1)
                    #print year_sep
                    dumentry = [year_sep[0][:-1], int(year_sep[1][:4])]
                    poplst.append(dumentry)             #add [title, year]
    poplst.append('-')      #'-' indicates end of list

def checkYear(title_sep):
    if len(title_sep) == 1:
        return True
    if "TV" in title_sep[1]:
        return True
    if "Himself" in title_sep[1]:
        return True
    if "????" in title_sep[1]:
        return True
    if "#" in title_sep[1]:
        return True
    if"archive footage" in title_sep[1]:
        return True
    else:
        return False


def filmEnter(lst, credit, dum, entry, master, tf):
    filmentry = {"title": lst[0], "year": lst[1], "credits": [credit]}
    entry["films"].append(filmentry)
    if tf == True:
        next_index = dum.index(lst) +1
        if type(dum[next_index]) == str:
            master.append(entry)


def dictAdd(dum, master, role):
    cont = False
    dirindex = 0
    tempfilms = 0
    for elmt in dum:
        failno=0
        if elmt == '-':     #end of list
            continue
        if type(elmt) == str:   #looks for name of director
            cont= True
            for item in master: #run through each entry in dict
                if item["name"] == elmt:    #looks for director match
                    dirindex = master.index(item)
                    tempfilms = len(master[dirindex]["films"])
                    templst=[]
                    for titles in master[dirindex]['films']:
                        templst.append(titles['title'])
                    print templst
                    #cont = True
                    break
        if cont == True:
            if len(elmt[0]) == 1:
                continue
            if elmt[0] in templst:
                for film in master[dirindex]["films"]:
                    if elmt[0] == film['title']:
                        if role in film['credits']:
                            break
                        film['credits'].append(role)
                        break
               # print elmt[0], master[dirindex]['name']
               # find = master[dirindex]["films"].index(elmt[0])
               # master[dirindex]["films"][find]['credits'].append('role')
            else:
                filmEnter(elmt, role, dum, master[dirindex], master, False)



            '''
            for film in master[dirindex]["films"]: #runs through directors films
                if elmt[0] == film["title"]:
                    if role in film["credits"]:
                        break
                    film['credits'].append(role)
                    #print elmt[0], film['credits']
                    failno = 0
                    break
                failno = failno +1


        print "fail:", failno
        print "total:", tempfilms
        print '---------------------------------'
        if failno == tempfilms:
            #print elmt, "new film", role
            print '--------------------------------------',role
            filmEnter(elmt, role, dum, master[dirindex], master)
        next_index = dum.index(elmt)+1
        if type(dum[next_index]) == str:
            cont = False
'''





