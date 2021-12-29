dictionary = {"AAM":"Mango",
              "Jam":"Beans",
              "Kola":"Banana"
              }
print("Options Are: ",dictionary.keys())
user = input("Enter The Bengali Word: ")
print("The Meaning of Your Word is: ",dictionary.get(user))