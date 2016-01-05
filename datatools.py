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
                    name_sep = line.split("\t\t")       #split director name
                    title_sep = name_sep[1].split("(",1) #split title
                    poplst.append(name_sep[0])          #add director name
                    dummy=[title_sep[0], int(title_sep[1][:4])]
                    poplst.append(dummy)               #add [first title, year]
                    cont = True
            if cont== True:         #works for lines other than the first one
                if line == '\n':
                    cont = False    #skips line b/c it's the end of a director
                else:
                    title_sep = line[:-1].split("\t\t\t") #split title
                    if len(title_sep) == 1:
                        continue
                    if "TV" in title_sep[1]:
                        continue
                    if "????" in title_sep[1]:
                        continue
                    year_sep = title_sep[1].split("(",1)
                    dumentry = [year_sep[0][:-1], int(year_sep[1][:4])]
                    poplst.append(dumentry)             #add [title, year]
    poplst.append('-')      #'-' indicates end of list


def filmEnter(lst, credit, dum, entry, master):
    filmentry = {"title": lst[0], "year": lst[1], "credits": [credit]}
    entry["films"].append(filmentry)
    next_index = dum.index(lst) +1
    if type(dum[next_index]) == str:
        master.append(entry)

