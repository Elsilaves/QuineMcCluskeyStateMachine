import unittest
from src.models.state_machine import AsynchronousStateMachine

class TestAsynchronousStateMachine(unittest.TestCase):
    def setUp(self):
        # Initialize the state machine with a fixed number of states for testing
        self.num_states = 4
        self.state_machine = AsynchronousStateMachine(self.num_states)

    def test_initial_state(self):
        # Test if the state machine initializes with a valid current state
        self.assertIn(self.state_machine.current_state, self.state_machine.states, "Initial state should be in the list of states.")

    def test_state_transition(self):
        # Test if the state machine transitions to a valid state and produces a valid output
        initial_state = self.state_machine.current_state
        input_signal = 1  # Example input signal
        next_state, output = self.state_machine.transition(input_signal)

        self.assertIn(next_state, self.state_machine.states, "Next state should be in the list of states.")
        self.assertIn(output, [0, 1], "Output should be either 0 or 1.")

    def test_truth_table_structure(self):
        # Test if the truth table has the correct structure
        truth_table = self.state_machine.truth_table()
        for row in truth_table:
            self.assertEqual(len(row), 4, "Each row in the truth table should have 4 elements.")
            self.assertIn(row[0], self.state_machine.states, "Current state should be in the list of states.")
            self.assertIn(row[2], self.state_machine.states, "Next state should be in the list of states.")
            self.assertIn(row[1], [0, 1], "Input signal should be either 0 or 1.")
            self.assertIn(row[3], [0, 1], "Output should be either 0 or 1.")

if __name__ == '__main__':
    unittest.main()



