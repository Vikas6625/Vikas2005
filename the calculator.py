import random

const_logo = '''
    _____________________
   |  _________________  |
   | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
   | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
   |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
   | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\    | || |  |_   _|     | || |   .' ___  |  | |
   | |___|___|___| |___| | | |  / .'   \\_| | || |    / /\\ \\  | || |    | |       | || |  / .'   \\_| | |
   | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\  | || |    | |   _   | || |  | |         | |
   | |___|___|___| |___| | | |  \\ '.___.'\\| || | _/ /    \\ \\| || |   _| |__/ |  | || |  \\ '.___.'\\| |
   | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
   | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
   | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
   | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
   |_____________________|

'''


#write four function add, sub,mul,div

def add(n1,n2):
      return  n1 + n2

def subtract(n1,n2):
      return  n1 - n2

def multiply(n1,n2):
      return  n1 * n2

def divide(n1,n2):
      if n2 == 0:
         return "Error! division by zero."
      return  n1 / n2

   # add these four function to the dictionary

operations = {
      "+": add,
      "-":subtract,
      "*":multiply,
      "/":divide,
      }

   # print the operation 
def calculator():
         print(const_logo)
         should_accumulate = True
         num1 = float(input("what is the first nimber?: "))

         while should_accumulate:
            for symbol in operations:
               print(symbol)
            operations_symbol = input("pick an operation: ")
            num2 = float(input("what is the next number?: "))
            answer = operations[operations_symbol](num1, num2)
            print(f"{num1} {operations_symbol} {num2} = {answer}")

            choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit  :   \n ")
            

            if choice == "y":
               num1 = answer
            else:
               should_accumulate = False
               print("\n" *20)
               calculator() 


calculator()