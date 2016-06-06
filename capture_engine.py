#Image capture engine

import pyscreenshot as ImageGrab

if __name__ == "__main__":
    im = ImageGrab.grab()
    im.show()
