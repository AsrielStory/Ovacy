import random
import eel

sg = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "z", "p", "q", "r", "s", "t", "v", "w", "x", "y", "ch", "sh"]
gl = ["a", "e", "i", "o", "u", "y"]

eel.init('web')

@eel.expose
def generator():
    o = bool(random.randint(0, 1))
    k = 0
    word = []
    for i in range(random.randint(3, 9)):
        if o == 0:
            word.append(random.choice(sg))
            if 50 <= random.randint(0, 100) <= 60:
                word.append(random.choice(sg))
            o = 1
        else:
            word.append(random.choice(gl))
            o = 0
    word_str = ''
    word_ram = ''.join(word).title()
    for i in word_ram:
        word_str += "<div class='word_str'>" + i + "</div>"
    return word_str

eel.start('index.html', mode='chrome', size=(800, 600))