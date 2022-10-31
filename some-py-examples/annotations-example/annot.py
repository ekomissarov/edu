# 2-Dec-2006 https://www.python.org/dev/peps/pep-3107/ Function Annotations
# 29-Sep-2014 https://www.python.org/dev/peps/pep-0484/ Type Hints
# 09-Aug-2016 https://www.python.org/dev/peps/pep-0526/ Syntax for Variable Annotations
# 8-Sep-2017 https://www.python.org/dev/peps/pep-0563/ Postponed Evaluation of Annotations

# https://habr.com/ru/company/lamoda/blog/432656/
# https://www.youtube.com/watch?v=R2QtnebNZdo

# from __future__ import annotations
from typing import List


def concat_them_all(strs: List[str]):
    return ''.join(strs)


print(concat_them_all(['1', '2']))
