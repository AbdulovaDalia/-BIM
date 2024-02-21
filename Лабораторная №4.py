from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Base class representing a vehicle."""

    def __init__(self, make: str, model: str, year: int):
        """Initialize a Vehicle object with make, model, and year."""
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def move(self, distance: float) -> None:
        """Move the vehicle for a given distance."""
        pass

    @abstractmethod
    def honk(self) -> None:
        """Produce a honking sound."""
        pass

    def __str__(self) -> str:
        """Return a string representation of the vehicle."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Return a detailed string representation of the vehicle."""
        return f"{self.__class__.__name__}(make={self.make}, model={self.model}, year={self.year})"


class Car(Vehicle):
    """Class representing a car, inheriting from Vehicle."""

    def __init__(self, make: str, model: str, year: int, num_doors: int):
        """
        Initialize a Car object with make, model, year, and number of doors.

        Args:
            make: The make of the car.
            model: The model of the car.
            year: The year the car was manufactured.
            num_doors: The number of doors the car has.
        """
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk(self) -> None:
        """Produce a honking sound specific to a car."""
        print("Beep! Beep!")

    def move(self, distance: float) -> None:
        """
        Move the car for a given distance.

        Args:
            distance: The distance to move the car.
        """
        # Implementation details for moving the car
        pass

    def accelerate(self, speed: float) -> None:
        """
        Accelerate the car to a given speed.

        Args:
            speed: The speed to accelerate to.
        """
        # Implementation details for accelerating the car
        pass


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 4)
    print(car)  # Output: 2022 Toyota Camry
    print(repr(car))  # Output: Car(make=Toyota, model=Camry, year=2022)
    car.honk()  # Output: Beep! Beep!
    car.accelerate(60)  # Accelerating the car to 60 mph
