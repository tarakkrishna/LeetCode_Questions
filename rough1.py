import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
paragraph=paragraph.lower().split()
paragraph = re.sub(r'[^\w\s]', '', paragraph)
print(paragraph)
# count=0
# word=''
# for i in paragraph:
#     if i not in banned:
#         if count<paragraph.count(i):
#             count=paragraph.count(i)
#             word=i
# print(word)