from blocks.block import Block

class PlayerBlock(Block):
    def __init__(self):
        self.color = 'red'
        self.position = [10, 250]
        super().__init__(self.color, self.position)