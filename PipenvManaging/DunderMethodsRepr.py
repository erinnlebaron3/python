# Dunder repr
# Dunder repr is used more for raw output so you usually do not format it nicely. 
# would do like output to your logs or to an error log or something like that


class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

  def __repr__(self):
    return f"Invoice({self.client}, {self.total})"


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))