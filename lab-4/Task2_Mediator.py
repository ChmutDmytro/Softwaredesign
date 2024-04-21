import uuid

class Aircraft:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def request_landing(self):
        self.mediator.request_landing(self)

    def request_take_off(self):
        self.mediator.request_take_off(self)

    def land(self):
        print(f"Aircraft {self.name} is landing.")
        print("Checking runway.")
        if self.mediator.allocate_runway(self):
            print(f"Aircraft {self.name} has landed.")
        else:
            print("Could not land, all runways are busy.")

    def take_off(self):
        print(f"Aircraft {self.name} is taking off.")
        if self.mediator.release_runway(self):
            print(f"Aircraft {self.name} has taken off.")
        else:
            print("Aircraft cannot take off as it is not on any runway.")

class CommandCentre:
    def __init__(self):
        self.runways = []
        self.aircrafts = []

    def add_runway(self, runway):
        self.runways.append(runway)

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def request_landing(self, aircraft):
        aircraft.land()

    def request_take_off(self, aircraft):
        aircraft.take_off()

    def allocate_runway(self, aircraft):
        for runway in self.runways:
            if runway.is_busy_with_aircraft is None:
                runway.is_busy_with_aircraft = aircraft
                return True
        return False

    def release_runway(self, aircraft):
        for runway in self.runways:
            if runway.is_busy_with_aircraft == aircraft:
                runway.is_busy_with_aircraft = None
                return True
        return False

class Runway:
    def __init__(self):
        self.id = uuid.uuid4()
        self.is_busy_with_aircraft = None


if __name__ == "__main__":
    command_centre = CommandCentre()
    runway1 = Runway()
    runway2 = Runway()
    command_centre.add_runway(runway1)
    command_centre.add_runway(runway2)

    aircraft1 = Aircraft("Aircraft1", command_centre)
    aircraft2 = Aircraft("Aircraft2", command_centre)

    command_centre.add_aircraft(aircraft1)
    command_centre.add_aircraft(aircraft2)

    aircraft1.request_landing()
    aircraft2.request_landing()

    aircraft1.request_take_off()