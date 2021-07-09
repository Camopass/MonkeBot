def split_list(l, item):
    if item in l:
        i = l.index(item)
        return [l[:i], l[i+1:]]
    else:
        return [l]
