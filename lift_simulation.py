# import time

# class Lift:
#     def __init__(self):
#         self.floors = ["B2", "B1", "G", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#         self.current_floor = "G"
#         self.door_open = False

#     def display_status(self):
#         print("\n----------------------------")


#         print(f"Current Floor : {self.current_floor}")
#         print(f"Door          : {'Open' if self.door_open else 'Closed'}")
#         print("----------------------------")

#     def open_door(self):
#         self.door_open = True
#         print("Door Opening...")
#         time.sleep(1)

#     def close_door(self):
#         self.door_open = False
#         print("Door Closing...")
#         time.sleep(1)

#     def move_to_floor(self, destination):

#         if destination not in self.floors:
#             print("Invalid Floor!")
#             return

#         current_index = self.floors.index(self.current_floor)
#         destination_index = self.floors.index(destination)

#         self.close_door()

#         if current_index < destination_index:
#             while current_index < destination_index:
#                 current_index += 1
#                 self.current_floor = self.floors[current_index]
#                 print(f"Going Up --> {self.current_floor}")
#                 time.sleep(1)

#         elif current_index > destination_index:
#             while current_index > destination_index:
#                 current_index -= 1
#                 self.current_floor = self.floors[current_index]
#                 print(f"Going Down --> {self.current_floor}")
#                 time.sleep(1)

#         else:
#             print("Lift is already on this floor.")

#         self.open_door()
#         print(f"Arrived at Floor {self.current_floor}")

# lift = Lift()

# while True:

#     lift.display_status()

#     print("\nAvailable Floors")
#     print("--------------------------------")
#     print("B2 B1 G 1 2 3 4 5 6 7 8 9 10")
#     print("--------------------------------")

#     floor = input("Enter Destination (or Q to Quit): ").upper()

#     if floor == "Q":
#         print("Lift Shutdown.")
#         break

#     lift.move_to_floor(floor)