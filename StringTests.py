def FirstAndLast(string):
    aos = string.split();
    res = "";
    for a in aos : 
        res += a[1:len(a) -1];
    return res;