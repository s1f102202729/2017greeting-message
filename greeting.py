

from datetime import datetime

def greet():
    mes = 'Hello, ' + name + '-san!'
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'

    print(message)
    print(mes)


greet('Inoue')
