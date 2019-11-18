#  build out an infinite lineup and in many cases that will be the approach that you want to take whenever you need 
# to build your own custom behavior into the iteration process.

#  generator file
# class infiniteLineup

# generator's use it's called the yield keyword
# special keyword in python and essentially what it's doing is exactly what it says, it's yielding to the generator
#  yield to self.player's index.
#  fact that we have yield right here and yield here and then we're calling next automatically tells python 
# that we are creating a generator object. 
#  whenever you put yield inside that is telling Python hey watch out we have a generator coming 

# So right here we don't have to have all of that extra boilerplate code we don't have to declare our own Dunder 
# next method or Dunder iter but instead we've simply taken our values, we create our own custom function here and 
# then inside of it we can simply call the yield and then that is going to provide all of that next type of behavior. 

class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        idx = 0

        while True:
            if idx < lineup_max:
                yield self.players[idx]
            else:
                idx = 0
                yield self.players[idx]

            idx += 1

    def __repr__(self):
        return f'InfiniteLineup({self.players})'

    def __str__(self):
        return f"InfiniteLineup with the players: {', '.join(self.players)}"


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()

print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(full_lineup))

print(str(full_lineup))