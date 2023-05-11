# remove leading and trailing zeros

## Task:

Create a function that takes a string input as a number and replaces leading and trailing zeros.

Hint:
re.sub("___(______)______", r"\1", given_string)  # r"\1" returns us the group

## Input/Output:

```
"0023.07623070"   -->   "23.0762307"  
"hello world"     -->   "hello world"  
"01230"           -->   "1230"  
```
