class UI(object):
    def __init__(self):
        global rpigpio
        import RPi.GPIO as rpigpio

        rpigpio.setmode(rpigpio.BCM)

        # Layout of GPIOs for Raspberry demo
        self._buttons = [16, 6, 5, 24, 27]
        self._LEDs = [20, 13, 12, 25, 22]

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


ui = UI()

while True: # Run forever
    print(ui.getButtonState())
