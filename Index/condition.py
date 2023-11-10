message = input('enter message')

match message:
    case 'HELLO':
        print('HI')
    case 'bye':
        print('GOOD NIGHT')
    case 'ok':
        print('cool')
    case other:
        print('nothing to say about')
        
