def chpo(a, b):
    if lst2[a] == lst[b]:
        str1[b], str1[a] = str1[a], str1[b]


str1 = ["this is good", "omkar is th omkar and omkar us oamkr omakt omkar",
        "omkar is omkar", "omkar is student", "omkar omkar omkar"]
print("please input your query string")
que = input()
n = 0
lst = []
for item in str1:
    li = list(item.split(" "))
    for word in li:
        if que == word:
            n = n + 1
        else:
            continue
    lst.append(n)
    n = 0
lst2 = lst.copy()
lst.sort(reverse=True)
chpo(1, 0)
chpo(2, 0)
chpo(3, 0)
chpo(4, 0)
chpo(0, 1)
chpo(2, 1)
chpo(3, 1)
chpo(4, 1)
chpo(0, 2)
chpo(1, 2)
chpo(3, 2)
chpo(4, 2)
i = 1
for item in str1:
    print(i, item)
    i += 1
"""
def mathingwords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1 
    return score


if __name__ == "__main__":
    # mathingWords("This is good", "python is good")
    sentences = ["python is a good", "this is snake",
                 "harry is a good boy", "Subscribe to code with harry"]

    query = input("Please enter the query string\n")
    scores = [mathingwords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] != 0]
    # print(sortedSentScore)

    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f" \"{item}\": with a score of {score}")
"""