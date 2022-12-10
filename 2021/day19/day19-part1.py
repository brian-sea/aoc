import sys
import re

with open('input-test', 'r') as f:

    scanners = []
    locations = []
    for line in f:

        line = line.strip()

        matches = re.findall('-+ scanner (\S+) -+', line)
        if len(matches) == 1:
            if len(locations) > 0:
                scanners.append(locations)
            locations = []
        elif len(line) > 0:
            location = [int(x) for x in line.split(',')]
            locations.append(location)

    