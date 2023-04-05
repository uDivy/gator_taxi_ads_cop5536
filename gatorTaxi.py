from redBlackTree import RedBlackTree
from minHeap import MinHeap

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
        ride = self.rbt.get(rideNumber)
        if ride:
            print(f"({rideNumber}, {ride.rideCost}, {ride.tripDuration})", file=open("output_file.txt", "a"))
        else:
            print("(0, 0, 0)", file=open("output_file.txt", "a"))

    def print_triplets(self, rideNumber1, rideNumber2):
        ride_numbers = [num for num in range(rideNumber1, rideNumber2 + 1) if self.rbt.get(num)]
        if ride_numbers:
            output_str = ", ".join([f"({num}, {self.rbt.get(num).rideCost}, {self.rbt.get(num).tripDuration})" for num in ride_numbers])
            print(output_str, file=open("output_file.txt", "a"))
        else:
            print("(0, 0, 0)", file=open("output_file.txt", "a"))

    def insert_ride(self, rideNumber, rideCost, tripDuration):
        if self.rbt.get(rideNumber):
            print("Error: Ride number already exists", file=open("output_file.txt", "a"))
            return

        ride = Ride(rideNumber, rideCost, tripDuration)
        self.rbt.put(rideNumber, ride)
        node = self.rbt.get(rideNumber)
        self.heap.insert(node)
        self.pointers[node] = ride
        # print(f"({rideNumber}, {rideCost}, {tripDuration})", file=open("output_file.txt", "a"))

    def get_next_ride(self):
        if self.heap.is_empty():
            print("No active ride requests", file=open("output_file.txt", "a"))
            return
        else:
            node = self.heap.pop()
            ride = self.pointers[node]
            del self.pointers[node]
            self.rbt.delete(ride.rideNumber)
            print(f"({ride.rideNumber}, {ride.rideCost}, {ride.tripDuration})", file=open("output_file.txt", "a"))

    def cancel_ride(self, rideNumber):
        ride = self.rbt.get(rideNumber)
        if ride:
            node = self.rbt.get_node(rideNumber)
            self.heap.delete(node)
            del self.pointers[node]
            self.rbt.delete(rideNumber)

    def update_trip(self, rideNumber, new_tripDuration):
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
    ride_service = RideService()
    while True:
        command = input()
        action, params = command.split('(', 1)
        params = params.strip(')')
        if len(params) > 0:
            action_params = [int(x) for x in params.split(',')]

        if action == "Insert":
            rideNumber, rideCost, tripDuration = action_params
            ride_service.insert_ride(rideNumber, rideCost, tripDuration)
        elif action == "Print":
            if len(action_params) == 1:
                rideNumber = action_params
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