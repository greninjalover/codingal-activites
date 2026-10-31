
from abc import ABC, abstractmethod

class SmartDevice(ABC):

    @abstractmethod
    def command(self):
        pass


class SmartLight(SmartDevice):

    def command(self):
        print("Smart Light: Turning the light on")


class SmartTV(SmartDevice):

    def command(self):
        print("Smart TV: Turning the TV on")


class SmartSpeaker(SmartDevice):

    def command(self):
        print("Smart Speaker: Playing music")


light = SmartLight()
tv = SmartTV()
speaker = SmartSpeaker()

devices = [light, tv, speaker]

for device in devices:
    device.command()
