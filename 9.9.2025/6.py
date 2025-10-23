def student_scores():
    scores = {"Quang": 85,
              "Giang": 90,
              "Duc": 78}
    scores["Loc"] = 92
    scores["Viet"] = 88
    scores["Phong"] = 86
    scores["Minh"] = 84
    return scores
def top_student(scores):
    highest = max(scores, key=scores.get)
    return highest
final_scores = student_scores()
print(final_scores)

for name in final_scores:
    print(f"Student {name} , score of {final_scores[name]}")

print(f"Top student is {top_student(final_scores)}")