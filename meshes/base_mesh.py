import numpy as np


class BaseMesh:
    def __init__(self) -> None:
        self.ctx = None
        
        self.program = None
        
        self.vbo_format = None