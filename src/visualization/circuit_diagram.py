import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_circuit_diagram(ax, prev_state, current_state, input_signal, output):
    """
    Draws a single state transition in the circuit diagram.

    :param ax: The matplotlib axes to draw on.
    :param prev_state: The previous state of the state machine.
    :param current_state: The current state of the state machine.
    :param input_signal: The input signal for the transition.
    :param output: The output of the state machine.
    """
    # Displaying previous state, input signal, and next state
    ax.text(0.1, 0.7, f"Previous: {prev_state}", ha="center", va="center", fontsize=12)
    ax.text(0.1, 0.5, f"Input: {input_signal}", ha="center", va="center", fontsize=12)
    ax.text(0.1, 0.3, f"Next: {current_state}", ha="center", va="center", fontsize=12)

    # Drawing the state machine box
    machine_rect = patches.Rectangle((0.3, 0.4), 0.4, 0.2, facecolor="lightblue", edgecolor="black")
    ax.add_patch(machine_rect)
    ax.text(0.5, 0.5, "State Machine", ha="center", va="center", fontsize=10)

    # Indicating the output with a colored LED
    led_color = "green" if output else "gray"
    led = patches.Circle((0.9, 0.5), radius=0.08, color=led_color, ec="black")
    ax.add_patch(led)
    
    # Drawing lines representing connections
    ax.plot([0.1, 0.3, 0.3], [0.5, 0.5, 0.6], color="black")
    ax.plot([0.7, 0.9], [0.5, 0.5], color="black")
    
    # Setting the plot limits and removing axis
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

def draw_circuit_diagrams(state_machine, test_inputs):
    """
    Draws the entire circuit diagram based on a series of test inputs.

    :param state_machine: The state machine object.
    :param test_inputs: A list of input signals to test the state machine.
    """
    fig, axs = plt.subplots(len(test_inputs), 1, figsize=(6, 4 * len(test_inputs)))
    prev_state = state_machine.states[0]
    for ax, input_signal in zip(axs, test_inputs):
        current_state, output = state_machine.transition(input_signal)
        draw_circuit_diagram(ax, prev_state, current_state, input_signal, output)
        prev_state = current_state

    plt.tight_layout()
    plt.show()
