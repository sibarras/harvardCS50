class Flight:
    def __init__(self, capacity:int) -> None:
        self.capacity:int = capacity
        self.passengers:list = []
    
    def add_passenger(self, name:int) -> bool:
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self) -> None:
        return self.capacity - len(self.passengers)

flight = Flight(3)

people:list = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    sucess = flight.add_passenger(person)
    if sucess:
        print(f"Added {person} to flight sucessfully.")
    else:
        print(f"No available seats for {person}.")