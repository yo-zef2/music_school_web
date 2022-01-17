
from typing import Pattern
import pandas as pd
import re

"正規表現"

uni = "東京藝術大学ギター学部"
print(uni)

matches = re.match(".{1,}大学", uni)
print(matches.group())

