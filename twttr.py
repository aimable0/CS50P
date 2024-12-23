def main(): 
  word = input('Input: ')
  word = shorten(word)
  print("Output:", word)

def shorten(word):
  return "".join([char for char in word if char.lower() not in ['a', 'e', 'i', 'o', 'u']])

if __name__ == "__main__":
  main()
