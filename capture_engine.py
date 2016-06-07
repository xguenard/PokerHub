#Image capture engine

import time

import image
import pyscreenshot


class CaptureEngine:
    """
        Class responsible of taking picture of the screen every two seconds
    """

    def __init__(self):

       self.delay = 2 # time between screen shots
       self.names = ("screenshot1.jpg", "screenshot2.jpg", "screenshot3.jpg")

    def start(self, nb_iter):
        """
            Launch the scan loop
        """

        for step in range(1, nb_iter + 1):

            print("Taking screenshot # " + str(step))
            im = pyscreenshot.grab()

            print("Saving screenshot in " + self.names[step%3])
            im.save(self.names[step%3])

            print("Screenshot saved\n")

            time.sleep(self.delay)
            step+=1


if __name__ == "__main__":
    test_engine = CaptureEngine()
    test_engine.start(20)