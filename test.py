from mointor import Mointor
import time
from touchButton.testButton import TouchButton

mointor = Mointor()

def clickfunc():
    mointor.println("click")

def doubleclickfunc():
    mointor.println("double")
    
def longfunc():
    mointor.println("long")


if __name__ == "__main__":
    mointor.setfont("consola.ttf")
    mointor.println("hello world!")
    mointor.println("second line")
    start = time.time()
    for i in range(10):
        mointor.println(f"the {i} line!!!")
#        time.sleep(0.005)
    end = time.time()
    mointor.println(f"use time: \n{end-start}s")
    a = '''
    1234
    5678
    '''
    print(a.strip().count('\n'))

    button = TouchButton(2)
    button.addeventDetect(TouchButton.CLICK, clickfunc)
    button.addeventDetect(TouchButton.DOUBLE_CLICK, doubleclickfunc)
    button.addeventDetect(TouchButton.LONG_PRESSED, longfunc)

    time.sleep(100)
    