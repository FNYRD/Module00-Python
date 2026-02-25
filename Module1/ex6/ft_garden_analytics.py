#!/usr/bin/env python3
#Parent class
class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"
    #Method that allows growing the plants by 1cm
    def grow(self) ->None:
        self.height += 1
        print(f"{self.name} grew 1cm")

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = False
    #This function changes the is_blooming boolean to True
    def bloom(self) -> None:
        self.is_blooming = True

    def __str__(self) -> str:
        if self.is_blooming:
            return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"
        else:
            return f"{self.name}: {self.height}cm"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height, color)
        self.prize_points: int = 0
    
    def __str__(self) -> None:
        return super().__str__() + " " + f"Prize points: {self.prize_points}"
    

class Garden:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
    
    def add_plant(self, plant: Plant) -> None:
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.plants.append(Plant)

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()


class GardenManager:
    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    def add_garden(self, garde: Garden) -> None:
        print(f"Added {garde.owner} to the Garden Manager")

    class GardenStats:
        def __init__(self, ) -> None:
            pass


def main() -> None:
    plants: list[Plant] = []
    plants = [Plant("Oak Tree", 100), 
              FloweringPlant("Rose", 25, "red"), 
              PrizeFlower("Sunflower", 50, "yellow")
             ]
    alice_garden: Garden = Garden("Alice")
    for plant in plants:
        alice_garden.add_plant(plant)
    


if __name__ == "__main__":
    main()
