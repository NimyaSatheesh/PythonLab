# Merge two dictionaries.
car1 = {
      "Maruti Suzuki": "1981 ",
      "model": "Swift "

    }
print("car1 : ", car1)
car2 = {
     "Hyundai": "1996",
     "model": "Nexo"

    }
print("car2 : ", car2)
print("")
car = car1.copy()
car.update(car2)

print("after merging : ", car)