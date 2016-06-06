#Image capture engine

import pyscreenshot as ImageGrab
import time

class CaptureEngine:
    """
        Class responsible of taking picture of the screen every two seconds
    """

    def __init__(self):
       self.delay = 2 # time between screen shots
       self.names = ("screenshot1", "screenshot2", "screenshot3")


    def start(self, nb_iter):
        """
            Launch the scan loop
        """
        round = 0
        counter = 0
        while round < nb_iter:
            print("Saving screenshot in "+self.names[counter] )
            im = ImageGrab.grab_to_file( self.names[counter] )
            print("Screenshot done")
            time.sleep(self.delay)
            ++round
            counter = (counter+1)%3





if __name__ == "__main__":
    test_engine = CaptureEngine()
    test_engine.start(20)


