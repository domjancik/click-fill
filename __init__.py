# Click fill

import time
import click
from ast import literal_eval

INDEXABLE_TYPES = [
        list,
        tuple
        ]

# Note - seems that it's not possible to write into Python closures, object it is then
class Loop():
    def __init__(self, items):
        self._idx = -1 # Make first call end up at zero without storing extra var
        self._items = items

    def next(self):
        if type(self._items) not in INDEXABLE_TYPES:
            return self._items 

        self._idx = (self._idx + 1) % len(self._items)
        return self._items[self._idx]


@click.command()
@click.option('--color', help='The color to fill your screen, obvsly dud')
@click.option('--interval', default=1.0, help='Interval to wait between going to next color value, seconds')
def fill(color, interval):
    parsed_color = color
    try:
        parsed_color = literal_eval(color)
    except:
        pass
    print(f"The color is {parsed_color}, type {type(parsed_color)}")
    x, y = click.get_terminal_size()
    color_loop = Loop(parsed_color)
    while(True):
        bg_color = color_loop.next()
        for i in range(y):
            click.secho(' ' * x, bg=bg_color)
        time.sleep(interval)
        click.clear()
    

def main():
    fill()

if __name__ == "__main__":
    main()
    
