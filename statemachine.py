from initialstate import InitialState
from time import time


class StateMachine:
    def __init__(self):
        self._states = []
        self._next_state = None

        self._running = True
        self._adding = False
        self._replacing = False
        self._resuming = False

    def size(self):
        return len(self._states)

    def empty(self):
        return len(self._states) == 0

    def top(self):
        if not self.empty():
            return self._states[-1]

    def push(self, state):
        self._adding = True
        self._replacing = False
        self._next_state = state

    def replace(self, state):
        self._adding = True
        self._replacing = True
        self._next_state = state

    def next_state(self):
        if self._resuming:
            if not self.empty():
                self._states.pop()
            if not self.empty():
                self.top().resume()
            self._resuming = False

        if self._adding:
            if not self.empty():
                if self._replacing:
                    self._states.pop()
                else:
                    self.top().pause()

            self._states.append(self._next_state)
            self._adding = False

    def update(self):
        if not self.empty():
            self.top().update()

    def quit(self):
        self._running = False

    def clear(self):
        self._running = False

        while not self.empty():
            self._states.pop()

    def running(self):
        return self._running


def game_loop():
    game_loop_delay_start = 0

    machine = StateMachine()
    initState = InitialState(machine)
    machine.push(initState)

    while True:
        if game_loop_delay_start == 0:
            game_loop_delay_start = int(round(time() * 1000))

        game_loop_delay_end = int(round(time() * 1000))

        if game_loop_delay_end - game_loop_delay_start >= 1000:
            machine.next_state()
            machine.update()
            game_loop_delay_start = game_loop_delay_end


if __name__ == '__main__':
    game_loop()
