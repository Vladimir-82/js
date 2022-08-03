"Baby shark lyrics generator"

NAMES = ['Baby', 'Mommy', 'Daddy', 'Grandma', 'Grandpa', "Let's go hunt"]
def baby_shark_lyrics():
    print(*map(lambda x: 3 * (x + ' shark,' + 6 * ' doo' + '\n') + x + ' shark!\n'.strip(), NAMES))
    print('Run away,…')

baby_shark_lyrics()