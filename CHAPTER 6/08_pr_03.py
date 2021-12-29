spam = ["make a lot of money", 'buy now', 'click this']

message = '''Hi, This is Nurun Nabi M.Engg
I would like to say you click this link to see
our latest products.'''

if ((spam[0] in  message) or (spam[1] in message) or (spam[2] in message)):
    print("Spam")
else:
    print('Inbox')