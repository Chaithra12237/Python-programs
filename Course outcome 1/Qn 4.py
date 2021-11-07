def word_count(str):
    c = dict()
    words = str.split()

    for word in words:
        if word in c:
            c[word] += 1
        else:
            c[word] = 1

    return c
str=input("Enter the line of text : ")
print("count of words : ",word_count(str))