import numpy as np

def run():
    mp = int(input('Digite el numero que desea averiguar los multiplos: '))
    print(np.arange(mp,(int(input('Digite el tamaño del array: '))+1)*mp,mp))

if __name__ == '__main__':
    run()