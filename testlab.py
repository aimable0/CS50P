def main():
  # test
  name = "Aimable"
  # this would result into a value error because: the split separator can not be empty
  full_names = "".join(for i in name if i not in ['a', 'e', 'i'])
  print(full_names)
  

if __name__ == "__main__":
  main()