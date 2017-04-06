from optical_forward_operator_emulator import optical_forward_operator_emulator
from sar_forward_operator_emulator import sar_forward_operator_emulator

class dummy_emulation_engine:

    def emulate_optical_forward_operator(self, optical_forward_operator):
        print ('Emulating an optical forward operator')
        return optical_forward_operator_emulator()

    def emulate_sar_forward_operator(self, sar_forward_operator):
        print ('Emulating a SAR forward operator')
        return sar_forward_operator_emulator()

    def get_optical_forward_operator_emulator(self, id):
        print ('Retrieving an existing optical forward operator emulator')
        return optical_forward_operator_emulator

    def get_sar_forward_operator_emulator(self, id):
        print ('Retrieving an existing SAR forward operator emulator')
        return sar_forward_operator_emulator