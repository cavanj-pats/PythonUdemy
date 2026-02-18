#challenge_DS_ThreeMostCommonWords.py

from collections import Counter
import re


text = ''' Python is an easy programmers language.
Python syntax is like the English language.
Python language is easy to learn and adapt to compared with Java and C.
In Python language, the same task can be performed using fewer lines of code.
 its easy learning and easy to code.'''

regex = '\w+'
match = re.findall(regex, text)

c = Counter(match)

print(c.most_common(3))

