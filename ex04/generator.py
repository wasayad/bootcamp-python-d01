
def generator(text, sep, *option):
    string = text.split(sep)
    test = list("")
    if option[0] is 'shuffle':
        for i in range(0, int(len(string) / 2)):
            test.append(string[i])
            string.remove(string[i])
        string.extend(test)
        return(string)
    if option[0] is 'unique':
        i = 0
        while i < len(string):
            j = i + 1
            while j < len(string):
                if string[i] == string[j]:
                    string.pop(j)
                    i = 0
                    break
                j = j + 1
            i = i + 1
        return(string)
    if option[0] is 'ordered':
        string = text.split(sep)
        ret = sorted(string, key=str.lower)
        return ret
