text = "The cat sat on the mat. The cat was happy. The mat was red."
text = text.lower()
text = text.replace(".", "")
words = text.split()

count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

sorted_words = sorted(count.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_words[:5]

print (top_5)
