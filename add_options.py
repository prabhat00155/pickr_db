from collections import defaultdict
import random
import pprint

#from animals import animals as array
#from birds import birds as array
from cities import cities as array
#from dishes import dishes as array
#from flags import flags as array
#from fruits import fruits as array
#from logos import logos as array
#from monuments import monuments as array
#from sports import sports as array


def fetch_options(d, all_items):
    cur_level, cur_name = d['level'], d['name']
    poss_levels = []
    if cur_level == 1:
        poss_levels = [1, 2, 3]
    elif cur_level == 10:
        poss_levels = [8, 9, 10]
    else:
        poss_levels = [cur_level - 1, cur_level, cur_level + 1]
    options = []
    for level in poss_levels:
        option = []
        while len(option) < 2:
            idx = random.randint(0, len(all_items[level]) - 1)
            if all_items[level][idx] != cur_name and all_items[level][idx] not in option:
                option.append(all_items[level][idx])
        options.extend(option)
    return options


all_items = defaultdict(list)
for a in array:
    all_items[a['level']].append(a['name'])

result = []
for a in array:
    tmp = {}
    tmp['name'] = a['name']
    tmp['level'] = a['level']
    tmp['options'] = fetch_options(tmp, all_items)
    result.append(tmp)
pp = pprint.PrettyPrinter(width=200)
pp.pprint(result)
