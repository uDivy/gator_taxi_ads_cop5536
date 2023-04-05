Start
|
|--- 1. Print(rideNumber)  
|      |
|      |--- Get triplet (rideNumber, rideCost, tripDuration) from RBT and print
| 
|--- 2. Print(rideNumber1, rideNumber2)  
|      |
|      |--- Get all triplets (rx, rideCost, tripDuration) where rideNumber1 <= rx <= rideNumber2 from RBT and print
|
|--- 3. Insert (rideNumber, rideCost, tripDuration)  
|      |
|      |--- Check if rideNumber already exists in RBT
|            |
|            |--- If yes, ignore
|            |
|            |--- If no, insert (rideNumber, rideCost, tripDuration) into RBT and insert a pointer to the corresponding node in the min heap
|                |
|                |--- Also, insert the triplet (rideNumber, rideCost, tripDuration) into the min heap
|
|--- 4. GetNextRide()  
|      |
|      |--- Check if there are any rides in the min heap
|            |
|            |--- If no, print "No active ride requests"
|            |
|            |--- If yes, get the triplet with lowest rideCost (ties are broken by selecting the triplet with the lowest tripDuration) from min heap, print it, delete it from min heap and RBT, and update pointers
|
|--- 5. CancelRide(rideNumber)  
|      |
|      |--- Delete the triplet (rideNumber, rideCost, tripDuration) from RBT and min heap, and update pointers if it exists
|
|--- 6. UpdateTrip(rideNumber, new_tripDuration)  
       |
       |--- Get the triplet (rideNumber, rideCost, tripDuration) from RBT
             |
             |--- If new_tripDuration <= existing tripDuration, update tripDuration in the triplet with new_tripDuration in RBT and min heap
             |
             |--- Else if existing_tripDuration < new_tripDuration <= 2*(existing tripDuration), remove the triplet from RBT and min heap, insert a new triplet (rideNumber, rideCost+10, new_tripDuration) into RBT and min heap, and update pointers
             |
             |--- Else if new_tripDuration > 2*(existing tripDuration), remove the triplet from RBT and min heap, and update pointers
End