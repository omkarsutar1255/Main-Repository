class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def isdance(self):
        return f"yes I dance {self.dance} no of times"


class Grandson(Son):
    dance = 6
    guitar = 1

    def isdance(self):
        return f"jackson yeah!" \
               f"yes I dance very awsomely {self.dance} no of times"


omkar = Dad()
avdhut = Son()
akshay = Grandson()

print(akshay.isdance())  # check from Grandson class
print(akshay.basketball)  # check from Son class then Dad class
print(akshay.guitar)  # this variable is in Grandson class
print(omkar.guitar)  # This variable is not in Dad class


class ElectronisDevice:
    microcontroller = 1
    Transfromer = 1
    Battery = 1
    Fuse = 1
    Relays = 1
    Switches = 1
    Motors = 1
    Circuit_Breaker = 1


class PocketGadgets:
    circuit_board = 1
    antenna = 1
    battery = 1
    Switches = 2


class Phones:
    LCD = 1
    keyboard = 1
    microphone = 1
    speaker = 1
    Switches = 3


ED = ElectronisDevice()
PG = PocketGadgets()
PN = Phones()
print(ED.Switches)
print(PG.Switches)
print(PN.Switches)
