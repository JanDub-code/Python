class Otec:
    def __init__(self, vek):
        self.vek = vek
    
class Syn(Otec):
    def __init__(self, vek, jmeno):
        super().__init__(vek)
        self.jmeno = jmeno