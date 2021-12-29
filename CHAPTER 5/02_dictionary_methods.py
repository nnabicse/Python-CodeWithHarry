mydict = {"Fast": "In a Quick Manner", "Nurun Nabi": "M.Engg"
    , "marks": [1, 2, 5], "anotherdict":{"NNabi":"M.Engg"}}

print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(mydict)
updatedict = {"Nabi":"B.Sc Engg"}
mydict.update(updatedict)
print(mydict)

print(mydict.get('Nabi'))