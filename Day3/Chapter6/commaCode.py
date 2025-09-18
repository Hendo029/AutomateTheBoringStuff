#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = []
def commaCode(arg):
    if len(arg) == 0:
        print('List is empty')
        return
    for i, j in enumerate(arg):
        if j == arg[-2]:
            print(j, end=' and ')
        elif j == arg[-1]:
            print(j)
        else:
            print(j, end=', ')

commaCode(spam)