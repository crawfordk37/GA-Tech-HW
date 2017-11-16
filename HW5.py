##Crawford Kennedy, 17ckennedy@woodward.edu, CS1301
##I worked on the homework assignment alone, using only this semester's course materials
def defineTAs(t):
    finalTAList = []
    string = ''
    k = 0;
    for item in t[0]:
        TAList = [x[k] for x in t]
        string = str(TAList[2]) + ': ' + str(TAList[0]) + ', ' + str(TAList[1])
        finalTAList.append(string)
        k += 1
    return tuple(finalTAList)
def offset(tuple_1, tuple_2, index_1):
    l = []
    tupleNum = 1
    index = index_1
    while(index != 0):
        l.append(index)
        if tupleNum == 1:
            index = tuple_1[index]
            tupleNum = 2
        else:
            index = tuple_2[index]
            tupleNum = 1
    l.append(index)
    return tuple(l)
def heroEgos(d):
    titleList = []
    for k in d:
        newList = d.get(k)
        for item in newList: 
            if k in item:
                titleList.append(item)
    return tuple(titleList)
def createActors(directors, movies):
    finalDictionary = {}
    for director in directors:
        show = directors.get(director)
        for movie in movies:
            if movie == show:
                finalDictionary[movies.get(movie)] = (movie, director)
    return finalDictionary
def updateNetworks(networks, tv_shows):
    network = {}
    for k in networks:
        for l in tv_shows:
            if l[0] == k:
                newList = networks.get(k)
                index = 0
                deleted = 0
                for item in newList:
                    if l[1] in item:
                        del newList[index]
                        deleted = 1    
                    else:
                        index += 1
                if deleted == 0:
                    newList.append(l[1])
                networks[k] = newList
    for l in tv_shows:
        equal = 0
        for k in networks:
            if k == l[0]:
                equal += 1
        if equal == 0:
            for k in network:
                if k == l[0]:
                    equal += 1
            if equal == 0:
                network[l[0]] = l[1]
            else:
                network[l[0]] = [network.get(l[0]), l[1]]
                
    networks.update(network)
    return networks
def artistMishap(artists):
    for k in artists:
        records = artists.get(k)
        if records % 2 != 0:
            if records % 7 == 0:
                records += 7
            if records % 5 == 0:
                records = records/5
            elif records % 3 == 0:
                records -= 3
        if records % 2 == 0:
            if records % 7 == 0:
                records -= 7
            elif records % 5 == 0:
                records += 5
            if records % 3 == 0:
                records = records*3
            records = records**2
        artists[k] = records
    minumum = 100
    maximum = 0
    finalList = [0, 0]
    for k in artists:
        records = artists.get(k)
        if records > maximum:
            maximum = artists.get(k)
            finalList[1] = (k, artists.get(k))
        if records < minumum:
            minimum = artists.get(k)
            finalList[0] = (k, artists.get(k))
    return finalList
