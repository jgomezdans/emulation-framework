from dummy_optical_forward_operator_emulator import DummyOpticalForwardOperatorEmulator
from dummy_sar_forward_operator_emulator import DummySARForwardOperatorEmulator

class DummyEmulationEngine:

    def emulate_optical_forward_operator(self, dummy_optical_forward_operator):
        print ('Emulating an optical forward operator')
        return DummyOpticalForwardOperatorEmulator()

    def emulate_sar_forward_operator(self, dummy_sar_forward_operator):
        print ('Emulating a SAR forward operator')
        return DummySARForwardOperatorEmulator()

    def get_optical_forward_operator_emulator(self, id):
        print ('Retrieving an existing optical forward operator emulator')
        return DummyOpticalForwardOperatorEmulator

    def get_sar_forward_operator_emulator(self, id):
        print ('Retrieving an existing SAR forward operator emulator')
        return DummySARForwardOperatorEmulator