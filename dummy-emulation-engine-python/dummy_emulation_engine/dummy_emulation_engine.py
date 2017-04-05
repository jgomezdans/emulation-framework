from optical_forward_operator_emulator import optical_forward_operator_emulator
from sar_forward_operator_emulator import sar_forward_operator_emulator

class dummy_emulation_engine:

    def emulate_optical_forward_operator(self, optical_forward_operator):
        return optical_forward_operator_emulator()

    def emulate_sar_forward_operator(self, sar_forward_operator):
        return sar_forward_operator_emulator()

    def get_optical_forward_operator_emulator(self, id):
        return optical_forward_operator_emulator

    def get_sar_forwad_operator_emulator(self, id):
        return sar_forward_operator_emulator