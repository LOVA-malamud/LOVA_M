smokers = {"John Smith", "Maya Levi", "Noam Cohen", "Liam Patel"}
ride_bikes = {"Maya Levi", "Omer Halevi", "Liam Patel"}
ride_motorcycles = {"John Smith", "Noam Cohen", "Rina Gold"}
likes_skyjump = {"John Smith", "Rina Gold", "Dina Bar"}

print("Suspects:", {"John Smith","Maya Levi","Noam Cohen","Liam Patel","Omer Halevi","Rina Gold","Dina Bar"})
print("\nClues:")
print("1) The suspect SMOKES")
print("2) The suspect likes SKYDIVING")
print("3) The suspect rides a BIKE or a MOTORCYCLE")

print(smokers & likes_skyjump & (ride_bikes | ride_motorcycles))
