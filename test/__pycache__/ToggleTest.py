from machine import Pin
from TestingSuite import PicoTestBase
from lib.thing import Thing

class ToggleTest(PicoTestBase):
    def test_toggle(self):
        print(f"Testing toggle")
        s = Thing()
        pin = Pin("LED", Pin.OUT)
        pin.toggle()
        assert pin.value() == 1, "toggle value does not match expected (1)"

    def test_toggle2(self):
        print(f"Testing toggle")
        pin = Pin("LED", Pin.OUT)
        pin.toggle()
        assert pin.value() == 0, "toggle value does not match expected (0)"