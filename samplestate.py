from state import State


class SampleState(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.init()

    def __del__(self):
        self.cleanup()

    def init(self):
        print('Sample State init')

    def cleanup(self):
        print('Sample State cleanup')

    def update(self):
        print('Sample State update')

    def resume(self):
        print('Sample State resume')

    def pause(self):
        print('Sample State pause')

    def __repr__(self):
        return __class__.__name__
