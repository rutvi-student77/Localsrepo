def calculate_overs(balls):
    overs = balls // 6  
    remaining_balls = balls % 6  
    return float(f"{overs}.{remaining_balls}")  

balls_bowled = int(input("Enter the number of balls bowled: "))
overs_balls = calculate_overs(balls_bowled)
print(f"The bowler has bowled: {overs_balls} overs")
