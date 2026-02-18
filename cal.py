def fun(x,y,op):
  if op == '+':
    return x + y
  elif op == '-':
    return x - y
  elif op == '*':
    return x * y
  elif op == '/':
    if y != 0:
      return x / y
    else:
      return "Error: Division by zero"
  else:
    return "Error: Invalid operator" 
  
def mulply(x,y):
  return x * y
def divide(x,y):
  if y != 0:
    return x / y
  else:
    return "Error: Division by zero"
def add(x,y):
  return x + y  
def subtract(x,y):
  return x - y  
def power(x,y):
  return x ** y 
def mod(x,y):
  if y != 0:
    return x % y
  else:
    return "Error: Division by zero"
