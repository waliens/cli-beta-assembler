from unittest import TestCase

from simulator.machine import twos_comp_16bits


class TestMachineUtil(TestCase):
    def testTwosComp16bits(self):
        self.assertEqual(-1, twos_comp_16bits(0xFFFF))
        self.assertEqual(-2, twos_comp_16bits(0xFFFE))
        self.assertEqual(-32768, twos_comp_16bits(0x8000))
        self.assertEqual(1, twos_comp_16bits(0x0001))
        self.assertEqual(2, twos_comp_16bits(0x0002))
        self.assertEqual(32767, twos_comp_16bits(0x7FFF))