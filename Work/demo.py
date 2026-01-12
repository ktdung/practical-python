import math
print(math.sqrt(16))

import urllib.request
u = urllib.request.urlopen('http://www.python.org')
data = u.read()

print(data.decode())
print(data[:20].decode())