#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    # Okno gry i zestaw elementow
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    # Zmienne pozycja rogue
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    event_handler = EventHandler()
    # nowe okno
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Yet Another Roguelike Tutorial",
            vsync=True,
    ) as context:
        # okno x i y F odwraca
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                # akcja ruchu
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                # akcja escape
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()