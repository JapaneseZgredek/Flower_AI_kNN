class Flower:
    def __init__(self, list_of_atributes, flower_type):
        self.attributes = list_of_atributes
        self.flower_type = flower_type

    def calculate_distance(self, flower) -> float:
        distance = 0
        for i in range(len(self.attributes)):
            distance = distance + ((self.attributes[i] - flower.attributes[i]) ** (self.attributes[i] - flower.attributes[i]))
        return distance