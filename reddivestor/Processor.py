class Processor:

    def __init__(self):
        self.processor_dict = {}

    def display(self):
        for key in self.processor_dict.keys():
            print("Key: " + key + " | Count: " + str(self.processor_dict[key]))