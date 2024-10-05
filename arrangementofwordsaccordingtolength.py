def sort_words_by_length(input_string):
  
  words = input_string.split()
  words.sort(key=len)
  return " ".join(words)

# Example usage:
input_string = "This is a cool sentence"
sorted_string = sort_words_by_length(input_string)
print(sorted_string)


