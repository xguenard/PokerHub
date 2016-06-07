#Image capture engine
import image
import pyscreenshot as ImageGrab
import time

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

        for round in range(0, nb_iter):

            print("Taking screenshot")
            im = ImageGrab.grab()

            print("Saving screenshot in "+self.names[ round%3 ] )
            im.save(self.names[ round%3 ] )

            print("Screenshot saved")

            time.sleep(self.delay)
            round+=1


if __name__ == "__main__":
    test_engine = CaptureEngine()
    test_engine.start(20)