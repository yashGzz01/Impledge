import time
startTime = time.time()
_endTime = '_end_'


def MakeTrie(words):
  root_dictionary = dict()
  for word in words:
    current_dictionary = root_dictionary
    for letter in word:
      current_dictionary = current_dictionary.setdefault(letter, {})
    current_dictionary[_endTime] = _endTime
  return root_dictionary

def LongestCompoundWord(original_trie, trie, word, level=0):

  # first letter
  f_l = word[0]

  if not f_l in trie:
    return False
  if len(word)==1 and _endTime in trie[f_l]:
    return level>0
  if _endTime in trie[f_l] and LongestCompoundWord(original_trie, original_trie, word[1:], level+1):
    return True
  return LongestCompoundWord(original_trie, trie[f_l], word[1:], level)


# f = open("file_name", 'r')

f = open("./Input_01.txt", 'r')

total_lines = f.readlines()
words=[]
for line in total_lines:
    words.append(line.replace("\n",""))


trie = MakeTrie(words)

words = sorted(words, key=lambda x: len(x), reverse=True)


# Finding the first Longest Compound Word

for word in words:
  if LongestCompoundWord(trie,trie,word):
    print("Longest Compound Word: {0:}".format(word))
    words.remove(word)
    break
  
  
# Finding the Second Longest Compound Word

for word in words:
  if LongestCompoundWord(trie,trie,word):
    print("Second Longest Compound Word: {0:}".format(word))
    words.remove(word)
    break

end = time.time()
elapsedTime = end-startTime
print("Execution Time is: " + str(elapsedTime) + " seconds.")