import time
start = time.time()
_end = '_end_'


def MakeTrie(words):
  root = dict()
  for word in words:
    current_dict = root
    for letter in word:
      current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end
  return root

def LongestCompoundWord(original_trie, trie, word, level=0):
  first_letter = word[0]
  if not first_letter in trie:
    return False
  if len(word)==1 and _end in trie[first_letter]:
    return level>0
  if _end in trie[first_letter] and LongestCompoundWord(original_trie, original_trie, word[1:], level+1):
    return True
  return LongestCompoundWord(original_trie, trie[first_letter], word[1:], level)


# f = open("file_name", 'r')

f = open("./Input_01.txt", 'r')

lines = f.readlines()
words=[]
for line in lines:
    words.append(line.replace("\n",""))


trie = MakeTrie(words)

words = sorted(words, key=lambda x: len(x), reverse=True)



for word in words:
  if LongestCompoundWord(trie,trie,word):
    print("Longest Compound Word: {0:}".format(word))
    words.remove(word)
    break

for word in words:
  if LongestCompoundWord(trie,trie,word):
    print("Second Longest Compound Word: {0:}".format(word))
    words.remove(word)
    break

end = time.time()
elapsed = end-start
print("Execution Time is: " + str(elapsed) + " seconds.")