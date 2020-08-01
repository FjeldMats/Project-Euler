from treys import Card, Evaluator
import sys
file = open("poker.txt", "r")
p1Wins = 0
p2Wins = 0
for line in file:
  game = line.strip('\n').split(" ")
  p1 = game[:5]
  p2 = game[5:]

  p1Cards = []
  p2Cards = []
  for c in p1:
      p1Cards.append(Card.new(c[0] + c[1].lower()))
  for c in p2:
      p2Cards.append(Card.new(c[0] + c[1].lower()))
  evaluator = Evaluator()
  p1Score = evaluator.evaluate(p1Cards[:3], p1Cards[3:])
  p2Score = evaluator.evaluate(p2Cards[:3], p2Cards[3:])
  sys.stdout.flush()
  if(p1Score < p2Score): # lower score is better
      p1Wins += 1
      print(f"p1:{p1Wins}, p2:{p2Wins}", end="\r")
  else:
      p2Wins += 1
      print(f"p1:{p1Wins}, p2:{p2Wins}", end="\r")

print(f"p1 wins total of {p1Wins} times")
