import pygame

def str_to_pygame_event(event_str):
    if event_str == "mousebuttondown":
        return pygame.MOUSEBUTTONDOWN
    elif event_str == "mousebuttonup":
        return pygame.MOUSEBUTTONUP
    elif event_str == "mousemotion":
        return pygame.MOUSEMOTION
    elif event_str == "keydown":
        return pygame.KEYDOWN
    elif event_str == "keyup":
        return pygame.KEYUP
    else:
        raise Exception("Invalid event string")