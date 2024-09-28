import os
import time

def animate_bordered_output(text, delay=0.1):
    """Animates the given text within a border by printing it character by character."""
    terminal_width, _ = os.get_terminal_size()
    border_char = '─'  # Horizontal border character
    vertical_border_char = '│'  # Vertical border character
    top_bottom_border = border_char * (terminal_width + 2)
    side_border = vertical_border_char + ' ' * terminal_width + vertical_border_char

    print(top_bottom_border)
    print(side_border)
    for char in text:
        print(vertical_border_char + ' ' + text[:len(text) - len(char)].center(terminal_width) + char + ' ' + vertical_border_char, end='', flush=True)
        time.sleep(delay)
    print(vertical_border_char + ' ' + text.center(terminal_width) + ' ' + vertical_border_char)
    print(side_border)
    print(top_bottom_border)

# Example usage
text = "This is an animated text within a border."
animate_bordered_output(text)