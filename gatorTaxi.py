from redBlackTree import RedBlackTree
from minHeap import MinHeap
import sys, os

class Ride:
    def __init__(self, rideNumber, rideCost, tripDuration):
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration

    def __lt__(self, other):
        return self.rideCost < other.rideCost


class RideService:
    def __init__(self):
        self.rbt = RedBlackTree()
        self.heap = MinHeap()
        self.pointers = {}

    def print_triplet(self, rideNumber):
        """
        prints the details of the ride with the given rideNumber in the format 
        "(rideNumber, rideCost, tripDuration)" to the file "output_file.txt"
        or (0, 0, 0) if ride doesn't exist !!!.
        """
        ride = self.rbt.get(rideNumber)
        if ride:
            print(f"({rideNumber}, {ride.rideCost}, {ride.tripDuration})", file=open("output_file.txt", "a"))
        else:
            print("(0, 0, 0)", file=open("output_file.txt", "a"))

    def print_triplets(self, rideNumber1, rideNumber2):
        """
        prints the details of all the rides with rideNumber between rideNumber1 and rideNumber2 (inclusive) 
        to the file "output_file.txt". The rides are printed in the format 
        "(rideNumber, rideCost, tripDuration)" separated by a comma and a space
        or (0, 0, 0) if ride doesn't exist !!!.
        """ 
        ride_numbers = [num for num in range(rideNumber1, rideNumber2 + 1) if self.rbt.get(num)]
        if ride_numbers:
            output_str = ", ".join([f"({num}, {self.rbt.get(num).rideCost}, {self.rbt.get(num).tripDuration})" for num in ride_numbers])
            print(output_str, file=open("output_file.txt", "a"))
        else:
            print("(0, 0, 0)", file=open("output_file.txt", "a"))

    def insert_ride(self, rideNumber, rideCost, tripDuration):
        """
        creates a new Ride object with the given parameters and inserts it into the 
        RedBlackTree and MinHeap instances. It also adds a pointer to the Ride object in the pointers 
        dictionary. If the rideNumber already exists, it will exit the code with the following 
        Error message: "Dulplicate RideNumber".
        """
        if self.rbt.get(rideNumber):
            print("Dulplicate RideNumber", file=open("output_file.txt", "a")) 
            sys.exit()

        ride = Ride(rideNumber, rideCost, tripDuration)
        self.rbt.put(rideNumber, ride)
        node = self.rbt.get(rideNumber)
        self.heap.insert(node)
        self.pointers[node] = ride
        # print(f"({rideNumber}, {rideCost}, {tripDuration})", file=open("output_file.txt", "a"))

    def get_next_ride(self):
        """
        removes the minimum ride (i.e., the ride with the lowest rideCost + ties are broken by
        selecting the ride with the lowest tripDuration) from the MinHeap, 
        deletes the corresponding Ride object from the RedBlackTree and the pointers dictionary, 
        and prints the ride details to the file "output_file.txt".
        """
        if self.heap.is_empty():
            print("No active ride requests", file=open("output_file.txt", "a"))
            return
        else:
            node = self.heap.extract_min()
            ride = self.pointers[node]
            del self.pointers[node]
            self.rbt.delete(ride.rideNumber)
            print(f"({ride.rideNumber}, {ride.rideCost}, {ride.tripDuration})", file=open("output_file.txt", "a"))

    def cancel_ride(self, rideNumber):
        """
        deletes the Ride object with the given rideNumber from the RedBlackTree, the MinHeap, 
        and the pointers dictionary and can be ignored if an entry for rideNumber doesn't exist
        """
        ride = self.rbt.get(rideNumber)
        if ride:
            node = self.rbt.get(rideNumber)
            self.heap.delete(node)
            del self.pointers[node]
            self.rbt.delete(rideNumber)

    def update_trip(self, rideNumber, new_tripDuration):
        """
        updates the tripDuration of the Ride object with the given rideNumber. 
        If the new tripDuration is less than or equal to the old tripDuration, it simply updates 
                                            the tripDuration and decreases the key in the MinHeap. 
        If the new tripDuration is between the old tripDuration and twice the old tripDuration, 
                                            it cancels the old Ride object and creates a new 
                                            Ride object with a higher rideCost i.e add 10 and the new tripDuration. 
        If the new tripDuration is more than twice the old tripDuration, it simply cancels the old Ride object. 
        """
        ride = self.rbt.get(rideNumber)
        if not ride:
            return

        if new_tripDuration <= ride.tripDuration:
            ride.tripDuration = new_tripDuration
            node = self.rbt.get(rideNumber)
            self.heap.decrease_key(node)
        elif ride.tripDuration < new_tripDuration <= 2 * ride.tripDuration:
            self.cancel_ride(rideNumber)
            self.insert_ride(rideNumber, ride.rideCost + 10, new_tripDuration)
        else:  # new_tripDuration > 2 * ride.tripDuration
            self.cancel_ride(rideNumber)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_name.py input_file")
        sys.exit(1)
    input_file = sys.argv[1]

    # specify file path
    file_path = "./output_file.txt"

    # check if file exists
    if os.path.isfile(file_path):
        # if file exists, delete its contents
        open(file_path, 'w').close()
    else:
        # if file does not exist, create it
        open(file_path, 'a').close()

    ride_service = RideService()
    with open(input_file) as f:
        for command in f:
            action, params = command.split('(', 1)
            params = params.strip(')\n ')
            if len(params) > 0 and params != " ":
                action_params = [int(x) for x in params.split(',')]

            if action == "Insert":
                rideNumber, rideCost, tripDuration = action_params
                ride_service.insert_ride(rideNumber, rideCost, tripDuration)
            elif action == "Print":
                if len(action_params) == 1:
                    rideNumber = action_params[0]
                    ride_service.print_triplet(rideNumber)
                elif len(action_params) == 2:
                    rideNumber1, rideNumber2 = action_params
                    ride_service.print_triplets(rideNumber1, rideNumber2)
            elif action == "UpdateTrip":
                rideNumber, new_tripDuration = action_params
                ride_service.update_trip(rideNumber, new_tripDuration)
            elif action == "GetNextRide":
                ride_service.get_next_ride()
            elif action == "CancelRide":
                ride_service.cancel_ride(action_params[0])