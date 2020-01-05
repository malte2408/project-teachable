from picamera import PiCamera

class UI(object):
    def __init__(self):
        global rpigpio
        import RPi.GPIO as rpigpio

        rpigpio.setmode(rpigpio.BCM)

        # Layout of GPIOs for Raspberry demo
        self._buttons = [7, 6, 21, 23, 9, 28, 2, 16] # [16, 6, 5, 24, 27]
        self._LEDs = [0, 5, 26, 22, 8, 27, 3, 15] # [20, 13, 12, 25, 22]

        for pin in self._buttons:
            rpigpio.setup(pin, rpigpio.IN, pull_up_down=rpigpio.PUD_DOWN)
        for pin in self._LEDs:
            rpigpio.setwarnings(False)
            rpigpio.setup(pin, rpigpio.OUT)

    def setLED(self, index, state):
        return rpigpio.output(self._LEDs[index],
                              rpigpio.LOW if state else rpigpio.HIGH)

    def getButtonState(self):
        return [rpigpio.input(button) for button in self._buttons]


class Picture(object):
    def __init__(self, frame):
        pass


ui = UI()
camera = PiCamera()

while True:
    print(ui.getButtonState())
    for index, button in enumerate(ui.getButtonState()):
        ui.setLED(index, button)
        if button > 0:
            camera.capture(str(index) + '.jpg')
