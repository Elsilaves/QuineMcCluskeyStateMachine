# QuineMcCluskeyStateMachine

## Project Overview
QuineMcCluskeyStateMachine is a Python application designed to simulate an asynchronous state machine. It utilizes the Quine-McCluskey algorithm for Boolean function minimization and provides visualization through circuit diagrams. The application also calculates and displays Hamming distances between state pairs.

## Features
- Asynchronous state machine simulation.
- Generation of truth tables based on state transitions.
- Boolean function minimization using the Quine-McCluskey algorithm.
- Calculation and display of Hamming distances.
- Visualization of state transitions using circuit diagrams.

## Sequence Diagram
```
[Client]                [AsynchronousStateMachine]    [TruthTableGenerator]    [QuineMcCluskeyAlgorithm]    [CircuitDiagram]
    |                                 |                         |                             |                           |
    |---- create() -----------------> |                         |                             |                           |
    |                                 |                         |                             |                           |
    |<--- return state_machine -------|                         |                             |                           |
    |                                 |                         |                             |                           |
    |                                 |---- generate() -------->|                             |                           |
    |                                 |                         |                             |                           |
    |                                 |<--- return truth_table -|                             |                           |
    |                                 |                         |                             |                           |
    |                                 |                         |---- simplify(minterms) ---> |                           |
    |                                 |                         |                             |                           |
    |                                 |                         |<--- return simplified ----->|                           |
    |                                 |                         |                             |                           |
    |                                 |---- transition() ------>|                             |                           |
    |                                 |                         |                             |                           |
    |<--- return next_state, output --|                         |                             |                           |
    |                                 |                         |                             |                           |
    |                                 |                         |                             |---- draw() -------------> |
    |                                 |                         |                             |                           |
    |                                 |                         |                             |<--- return diagram ------ |
    |                                 |                         |                             |                           |
```

## Use Case Diagram
```
+-----------------------------------+
|           System                  |
|   QuineMcCluskeyStateMachine      |
|                                   |
|   [User]                          |
|     |                             |
|     |-------> (Initialize State   |
|     |          Machine)           |
|     |                             |
|     |-------> (Generate Truth     |
|     |          Table)             |
|     |                             |
|     |-------> (Apply              |
|     |          Quine-McCluskey)   |
|     |                             |
|     |-------> (Calculate and      |
|                Display Hamming    |
|                Distances)         |
|     |                             |
|     |-------> (Visualize State    |
|                Transitions)       |
+-----------------------------------+
```

## State Machine Diagram
```
+----------------+      +-----------------+      +-------------------+
|                |      |                 |      |                   |
|   Initialized  |----->| Truth Table     |----->| Minterms          |
|                |      | Generated       |      | Extracted         |
+----------------+      +-----------------+      +-------------------+
                            |                            |
                            V                            V
                      +------------------+       +-------------------+
                      |                  |       |                   |
                      | Simplification   |       | Hamming Distances |
                      | (Quine-McCluskey)|       | Calculated        |
                      |                  |       |                   |
                      +------------------+       +-------------------+
                                            \          |
                                             \         V
                                              \    +-----------------+
                                               \   |                 |
                                                -->| Visualization   |
                                                   |(Circuit Diagram)|
                                                   |                 |
                                                   +-----------------+
```

## Activity Diagram
```
+------------------+      +-----------------------+      +---------------------------+
|                  |      |                       |      |                           |
| Start Program    |----->| Initialize State      |----->| Generate Truth Table      |
|                  |      | Machine               |      | from State Machine        |
+------------------+      +-----------------------+      +---------------------------+
                                                                   |
                                                                   V
                                                         +-------------------------+
                                                         |                         |
                                                         | Extract Minterms from   |
                                                         | Truth Table             |
                                                         |                         |
                                                         +-------------------------+
                                                                   |
                                                                   V
                                                         +-------------------------+
                                                         |                         |
                                                         | Simplify Minterms using |
                                                         | Quine-McCluskey         |
                                                         | Algorithm               |
                                                         |                         |
                                                         +-------------------------+
                                                                   |
                                                                   V
                                                         +-------------------------+
                                                         |                         |
                                                         | Calculate Hamming       |
                                                         | Distances               |
                                                         |                         |
                                                         +-------------------------+


                                                                   |
                                                                   V
                                                         +-------------------------+
                                                         |                         |
                                                         | Visualize State         |
                                                         | Transitions with        |
                                                         | CircuitDiagram          |
                                                         |                         |
                                                         +-------------------------+
                                                                   |
                                                                   V
                                                         +-------------------------+
                                                         |                         |
                                                         | End Program             |
                                                         |                         |
                                                         +-------------------------+
```

## Installation
To run the project, clone the repository and install necessary dependencies:
```
git clone https://github.com/elsilaves/QuineMcCluskeyStateMachine.git
cd QuineMcCluskeyStateMachine
```

## Usage
Execute the main script to start the simulation:
```
python main.py
```

## Test
For tests run python3 -m unittest tests/test_state_machine.py

## License
This project is licensed under the MIT License.
