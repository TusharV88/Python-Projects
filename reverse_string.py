# REVERSE A STRING

# Take any string from user
string = input('Enter any string : ')

############## Method-1 #################
new_string = string[::-1]   # Indexing
print('-'*20)
print(f'Reversed String using 1st method : {new_string}')

############## Method-2 #################
def reverse_fun1(s):  # Loop
  str = ""
  for i in s:
    str = i + str
  return str

print('-'*20)
print(f'Reversed String using 2nd method : {reverse_fun1(string)}')

############## Method-3 #################
def reverse(s):   # Recursion
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

print('-'*20)
print(f'Reversed String using 3rd method : {reverse(string)}')

############## Method-4 #################
def reverse(string):    # Reversed
    string = "".join(reversed(string))
    return string

print('-'*20)
print(f'Reversed String using 4th method : {reverse(string)}')


