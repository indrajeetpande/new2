name, char=input('enter name and char separated by comma').split(',')
print(f'length of name is{len(name)}')
print(f'character count: {name.strip().lower().count(char.strip().lower())}')