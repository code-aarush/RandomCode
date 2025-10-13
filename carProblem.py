current_pos1, current_pos2, speed1, speed2, finish = 0, 10, 2, 3, 50
car1_str, car2_str = str(current_pos1), str(current_pos2)
while current_pos1 < finish and current_pos2 < finish :
    if current_pos1 < current_pos2 and current_pos1 + speed1 > current_pos2 + speed2:
        car1_str += " " + "Winner(overtake)"
        car2_str += " " + "Runner-Up"
        break
    elif current_pos2 < current_pos1 and current_pos2 + speed2 > current_pos1 + speed1:
        car1_str += " " + "Runner-Up"
        car2_str += " " + "Winner(overtake)"
        break
    car1_str, car2_str = str(car1_str) + " " + str((current_pos1 := current_pos1 + speed1)), str(car2_str) + " " + str((current_pos2 := current_pos2 + speed2))
    if current_pos1 >= finish :
        car1_str = car1_str + " " + "Winner"
        car2_str = car2_str + " " + "Runner-Up"
        break
    elif current_pos2 >= finish :
        car1_str = car1_str + " " + "Runner-Up"
        car2_str = car2_str + " " + "Winner"
        break
if current_pos1 == current_pos2 : print("Tie")  
print(car1_str, print(car2_str))
