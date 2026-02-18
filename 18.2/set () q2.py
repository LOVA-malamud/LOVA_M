smokers = {"Avi Ron", "Sara Kim", "Ben Azulay", "Nina Fox"}
ride_bikes = {"Sara Kim", "Tom Green", "Nina Fox"}
ride_motorcycles = {"Avi Ron", "Ben Azulay", "Nina Fox", "Eli Stone"}
likes_skyjump = {"Avi Ron", "Nina Fox", "Sara Kim", "Dana Wolf"}

print("Suspects:", {"Avi Ron","Sara Kim","Ben Azulay","Nina Fox","Tom Green","Eli Stone","Dana Wolf"})
print("\nClues:")
print("1) The suspect rides a BIKE or a MOTORCYCLE")
print("2) The suspect SMOKES")
print("3) The suspect likes SKYDIVING")
print("4) The suspect is NOT someone who rides BOTH bike AND motorcycle")

print((ride_bikes | ride_motorcycles) & smokers & likes_skyjump - (ride_bikes & ride_motorcycles))
