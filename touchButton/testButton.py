import Adafruit_GPIO.GPIO as GPIO
import time
import threading

class TouchButton(object):
    PRESSED = 1
    RELEASED = 0
    CLICK = 2
    DOUBLE_CLICK = 3
    LONG_PRESSED = 4

    def __init__(self, io, ucc = None, gnd = None):
        self._io = io
        self._clickTime = 0.3
        self._longPressTime = 1.0
        self._doubleClickBetweenTime = 0.2
        self._relasetime = time.time()
        self._isDoubleClick = False
        self._callback = {}
        self._gpio = GPIO.get_platform_gpio()
        self._gpio.setup(io, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self._gpio.add_event_detect(self._io, GPIO.RISING, self._risingListenFunc_)
        

    def readStatusNow(self):
        if (self._gpio.input(self._io) == GPIO.HIGH):
            return TouchButton.PRESSED
        else:
            return TouchButton.RELEASED
    
    def addeventDetect(self, mode = CLICK, callback = None,\
                       clickTime = None, longPressTime = None, doubleClickBetweenTime = None):
        self._callback[mode] = callback
        if clickTime:
            self._clickTime = clickTime
        if longPressTime:
            self._longPressTime = longPressTime
        if doubleClickBetweenTime:
            self._doubleClickBetweenTime = doubleClickBetweenTime
        
    
    def _risingListenFunc_(self, channel):
        #self._gpio.remove_event_detect(self._io)
        #self._gpio.add_event_detect(self._io, GPIO.FALLING, self._fallingListenFunc_)
        if time.time() - self._relasetime <= self._doubleClickBetweenTime:
            return
        self._risingtime = time.time()
        while  self.readStatusNow() == self.PRESSED:
            if time.time() - self._risingtime >= self._longPressTime:
                self._callback[TouchButton.LONG_PRESSED]()
                return
        
        self._relasetime = time.time()

        while self.readStatusNow() == self.RELEASED:
            if time.time() - self._relasetime >= self._doubleClickBetweenTime:
                self._callback[TouchButton.CLICK]()
                return

        self._callback[TouchButton.DOUBLE_CLICK]()
        



    
    

    
    def _fallingListenFunc_(self, channel):
        print("raise")
        self._gpio.remove_event_detect(self._io)
        self._gpio.add_event_detect(self._io, GPIO.RISING, self._fallingListenFunc_)
        self._releasedTime = time.time()
        if self._releasedTime - self._pressedTime <= self._clickTime:
            if self._isDoubleClick:
                self._isDoubleClick = False
                self._callback[TouchButton.DOUBLE_CLICK]()
            else:
                print("raise waiting")
                time.sleep(self._doubleClickBetweenTime)
                if not self._isDoubleClick:
                    self._callback[TouchButton.CLICK]()
        else:
            self._callback[TouchButton.LONG_PRESSED]()
        


def clickfunc():
    print("click")

def doubleclickfunc():
    print("double")
    
def longfunc():
    print("long")

if __name__ == "__main__":
    button = TouchButton(2)
    button.addeventDetect(TouchButton.CLICK, clickfunc)
    button.addeventDetect(TouchButton.DOUBLE_CLICK, doubleclickfunc)
    button.addeventDetect(TouchButton.LONG_PRESSED, longfunc)
    time.sleep(100)

    
        

    
