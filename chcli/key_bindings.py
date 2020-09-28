from prompt_toolkit.filters import completion_is_selected
from prompt_toolkit.key_binding import KeyBindings

kb = KeyBindings()


@kb.add("enter", filter=completion_is_selected)
def _(event):
    event.current_buffer.complete_state = None
    b = event.app.current_buffer
    b.complete_state = None
