# List, Dictionary, & Set: Given a list of tuples (name,  score), create a dictionary where the keys are the names, and  the values are the scores, then return a set of names whose  scores are above a certain threshold.
l = [("Ram", 85), ("Sita", 70), ("Hari", 90), ("Gita", 65)]
threshold = 80
score_dict = {}
above_threshold = set()
for name, score in l:
    score_dict[name] = score
    if score > threshold:
        above_threshold.add(name)
print(score_dict)
print(above_threshold)
