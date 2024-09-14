import random

def createTable(data, k=4):
  table = {}
  for i in range(len(data) - k - 1):
    pattern = data[i:i+k]
    next = data[i+k]
    if pattern in table:
      if next in table[pattern]:
        table[pattern][next] += 1
      else:
        table[pattern][next] = 1
    else:
      table[pattern] = {next: 1}
      
  return table

def makeProbabilityTable(table):
  for key in table:
    row = table[key]
    total = sum(row.values())
    for key2 in row:
      row[key2] = row[key2]/total

  return table

def generateNextcharacter(table, pattern, k=4):
  pattern = pattern[-k:]
  if pattern in table:
    row = table[pattern]
    possible_chars = list(row.keys())
    weightage = list(row.values())
    return random.choices(possible_chars, weights=weightage)[0]
  else:
    return " "

def makeTable(filename):
  with open(filename, 'r') as file:
    data = file.readline().lower()
    table = createTable(data)
    table = makeProbabilityTable(table)
    return table

def generateSentence(table, pattern):
  next_char = ''
  while next_char != ".":
    next_char = generateNextcharacter(table, pattern)
    pattern += next_char
    if pattern[-2] == " " and next_char == " ":
      break

  print(pattern)


def main():
  pattern = input("Enter the text: ").lower().strip()
  table = makeTable("data.txt")
  generateSentence(table, pattern)


main()
  
