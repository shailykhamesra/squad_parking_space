from src.parking import ParkingSpace

class SquadStackParkingSysytem:
    
    def __init__(self, input):
        self.input = input


    def process_input(self):
        """
        This method is used to process the user input.
        It is a smart method which does not limit itself based on case sensitivity.
        It welcomes user friendly analysis by skiping the empty lines.
        It focuses on the users simplicity.
        """
        input = open(self.input, 'r').read()
        newFileContent = input.lower()
        processed_input = []
        with open(self.input) as f:
            for line in f:
                if line == '\n':
                    continue
                processed_input.append(line.rstrip())

        return processed_input


    def initiate_parking_process(self, processed_input):
        """
        This method is used to do the actual initialization of the parking slot.
        It the communication link between the parking space and parking bound functionalities.
        """
        pl = ParkingSpace(processed_input)
        pl.initialize_parking()

if __name__ == "__main__":
    # It help reads user enetered input file
    # It helps to create a communiction between user input and SuadStackParkingSystem
    import sys
    input = sys.argv[1]
    ssps = SquadStackParkingSysytem(input)
    processed_input = ssps.process_input()
    ssps.initiate_parking_process(processed_input)