import unittest   # The test framework
import rover

class RoverShould(unittest.TestCase):
    def test_move_up(self):
        self._rover = rover.Rover()
        self.assertEqual(self._rover.execute("M"), "1:2:N")

    def test_makeNoMovementWhenPassedEmptyArrayOfCommands(self):
        self._rover = rover.Rover()
        self.assertEqual(self._rover.execute(""), "1:1:N")

    def test_rotateRight(self):
        self._rover = rover.Rover()
        self.assertEqual(self._rover.execute("R"), "1:1:E")
        self._rover = rover.Rover()
        self.assertEqual(self._rover.execute("RR"), "1:1:S")
        self._rover = rover.Rover()
        self.assertEqual(self._rover.execute("RRR"), "1:1:W")
        self._rover = rover.Rover()
        self.assertEqual(self._rover.execute("RRRR"), "1:1:N")