class Flower:
    def __init__(self, flower_type):
        self.attributes = []
        self.flower_type = flower_type

    def calculate_distance(self, flower) -> float:
        distance = 0
        for i in range(len(self.attributes)):
            distance = distance + ((self.attributes[i] - flower.attributes[i]) ** (self.attributes[i] - flower.attributes[i]))
        return distance