questions = [
    ["What is the name of Thor’s hammer?", "A. Stormbreaker", "B. Mjolnir", "C. Gungnir", "D. Leviathan", "B"],
    ["Who was the first Avenger?", "A. Iron Man", "B. Captain America", "C. Thor", "D. Hulk", "B"],
    ["What is Black Panther’s real name?", "A. M'Baku", "B. N'Jadaka", "C. T'Challa", "D. Shuri", "C"],
    ["Which Infinity Stone was hidden on Vormir?", "A. Time Stone", "B. Power Stone", "C. Mind Stone", "D. Soul Stone", "D"],
    ["What is the name of Iron Man’s A.I. assistant after J.A.R.V.I.S.?", "A. F.R.I.D.A.Y.", "B. KAREN", "C. E.D.I.T.H.", "D. S.H.I.E.L.D.", "A"]
]

prize_money = ["150 RUPEYA", 5000, 10000, 50000, "7 CRORE"]
total_prize = 0

print("Welcome to the Marvel Quiz! \n")

for i, q in enumerate(questions):
    print(f"Question {i+1}: {q[0]}")
    for option in q[1:5]:
        print(option)
    
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    if answer == q[5]:
        total_prize = prize_money[i]
        print(f"Correct! You have won Rs.{total_prize}\n")
    else:
        print(f"Wrong ANswer! You are taking home Rs.{total_prize}\n")
        break

print(f"Game over! Your final prize amount is Rs.{total_prize}")
