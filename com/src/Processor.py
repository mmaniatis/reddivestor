class Processor:

    def __init__(self):
        self.processor_dict = {}

    def display(self):
        try:
            for key in self.processor_dict.keys():
                print("Key: " + key + " | Count: " + str(self.processor_dict[key]))
        except Exception as e:
            print("Exception while displaying processor_dict, StackTrace(): " + e)
            return False
        return True
            