def main():
  number1 = int(input('First number: '))
  number2 = int(input('Second number: '))
  sum = calc(number1, number2)
  print(sum)

def calc(num1, num2):
  return num1 + num2

if __name__ == "__main__":
  main()
