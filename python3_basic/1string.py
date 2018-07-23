#Print Welcome Message
message = """Assassain Creed
Nothing is true, everthing is permitted"""
print(message)
print(len(message))

print(message[10:15])
#first bracket include the letter, but the second does not

print(message[:10])

print(message.lower())
print(message.upper())
print('Count how many e inside the "message" ')
print(message.count('e'))

print(message.find('true'))

new_message=message.replace("Nothing is true, everthing is permitted", "We work in dark and serve the light")
print(new_message)

greet = 'Bonsoir'
name  = 'Monsieur'
greet_msg = greet + ',' + name + ' Jacob'
greet_msg_format = '{}, {} Jacob'.format(greet, name)
greet_msg_f= f'{greet.upper()}, {name} Jacob'

print(greet_msg)
print(greet_msg_format)
print(greet_msg_f)

print(dir(message))
print(help(str))
print(help(str.upper))
