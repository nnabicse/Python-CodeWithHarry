def strip_func(string,word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "         N.Nabi.MEngg"

n = strip_func(this, ".")
print(n)