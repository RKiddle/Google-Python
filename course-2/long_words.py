import re
def long_words(text):
  pattern = re.search(r"\b[a-zA-Z]{7}\b", text)
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

#errors 3 and 7
