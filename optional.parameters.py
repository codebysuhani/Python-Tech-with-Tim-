def func(x):
    print(x)

func("hello")

def func1(x, text):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')

func1('tanu', '5')


def func1(x, text='2'):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print(text)

func1('tanu', '78')
