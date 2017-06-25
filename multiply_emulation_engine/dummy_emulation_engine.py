from multiply_emulation_engine import dummy_optical_forward_operator_emulator
from multiply_emulation_engine import dummy_sar_forward_operator_emulator

class DummyEmulationEngine:

    def emulate_optical_forward_operator(self, dummy_optical_forward_operator):
        print ('Emulating an optical forward operator')
        return dummy_optical_forward_operator_emulator.DummyOpticalForwardOperatorEmulator()

    def emulate_sar_forward_operator(self, dummy_sar_forward_operator):
        print ('Emulating a SAR forward operator')
        return dummy_sar_forward_operator_emulator.DummySARForwardOperatorEmulator()

    def get_optical_forward_operator_emulator(self, id):
        print ('Retrieving an existing optical forward operator emulator')
        return dummy_optical_forward_operator_emulator.DummyOpticalForwardOperatorEmulator()

    def get_sar_forward_operator_emulator(self, id):
        print ('Retrieving an existing SAR forward operator emulator')
        return dummy_sar_forward_operator_emulator.DummySARForwardOperatorEmulator()