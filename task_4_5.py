import sys

import utils

result = utils.currency_rates(sys.argv[1])
if result is None:
    print(result)
else:
    print(f"{result[0]}, {result[1]}")
