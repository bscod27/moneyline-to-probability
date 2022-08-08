import sys


def convert_moneyline(line: str) -> float: 
  """
  Takes a moneyline input (with a + or - sign in front) and converts the line to a probability.

  :params line: String input of the moneyline odds for any given sports event.
  """

  risk = 100
  win = abs(int(line))

  if win < 100:  # defensive programming
    raise SyntaxError('Input line is invalid. Moneyline odds are always +/- a value greater than or equal to 100.')

  if int(line) > 0: # underdog
    odds = risk/win
  else: # favorite 
    odds = win/risk
  
  return round(odds/(1 + odds), 2)


if __name__ == '__main__':
  args = sys.argv[1:]
  
  for i in args: 
    print(i+':')
    print(convert_moneyline(line=i))
    print('='*5, '\n')
