from state import State
from samplestate import SampleState


class InitialState(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.init()

    def __del__(self):
        self.cleanup()

    def init(self):
        print('Initial State init')

    def cleanup(self):
        print('Initial State cleanup')

    def update(self):
        print('Initial State update')
        sampleState = SampleState(self._state_machine)
        self._state_machine.replace(sampleState)

    def resume(self):
        print('Initial State resume')

    def pause(self):
        print('Initial State pause')

    def __repr__(self):
        return __class__.__name__
