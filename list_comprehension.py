def main():
  # using list comprehensions

  friends = [
    { "name": "Karake",
      "age": 20
    },
    {
      "name": "Didier",
      "age": 22
    },
    {
      "name": "Uwase",
      "age": 24
    },
    {
      "name": "Shemsa",
      "age": 22
    },
    {
      "name": "Roxana",
      "age": 22
    },
    {
      "name": "Levis",
      "age": 21
    }
  ]

  # list comprehensions: concise way of making lists from sequences/iterable
  # usage [expression(value to be added to the returned list) for item in sequence/iterable if condition] 
  ages =  [friend['age'] for friend in friends if friend['age'] <= 21]
  print(ages)
  #print(sample)

if __name__ == "__main__":
  main()