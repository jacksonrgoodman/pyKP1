
def game_quit():
    print('\nAre you sure youi want to quit?\n')
    choice = input('> ').lower()
    confirm = ['yes', 'y', 'quit', 'exit']
    deny = ['no', 'n', 'cancel']
    if choice in ['yes', 'y', 'quit', 'exit']:
        quit()
    elif choice in ['no', 'n', 'cancel']:
        return
    else:
        return
