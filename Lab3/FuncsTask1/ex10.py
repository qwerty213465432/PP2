def unq(list):
    unqlist = []
    for item in list:
        if item not in unqlist:
            unqlist.append(item)
    return unqlist


oglist = []
unq(oglist)
