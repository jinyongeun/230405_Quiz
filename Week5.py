score = input("점수를 입력하세요: ")

num_score = int(score)

if 71 <= num_score :
    print("A")

elif 41 <= num_score < 71 :
    print("B")
elif 11 <= num_score < 41 :
    print("C")
else :
    print("D")