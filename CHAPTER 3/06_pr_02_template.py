letter = '''Dear <|Name|>, 
You are Selected!
Date: <|Date|>
'''

print(letter)

name = input('Enter Your Name: ')
letter = letter.replace('<|Name|>', name)
date = input('Enter Date')
letter = letter.replace('<|Date|>', date)

print(letter)