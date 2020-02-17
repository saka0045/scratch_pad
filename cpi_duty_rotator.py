#!/usr/bin/env python3

import json

open_cpi_profile = open("/Users/m006703/scratch_pad/cpi_profile.json", "r")
open_rotator = open("/Users/m006703/scratch_pad/duty_rotator_index.txt", "r")

cpi_profile = json.load(open_cpi_profile)

informatics_specialist_list = cpi_profile["informatics_specialist"]

# Read the rotator index file to get the rotator index for each element
rotator_index_dict = {}
for line in open_rotator:
    line = line.rstrip()
    line_item = line.split("=")
    rotator_name = line_item[0]
    rotator_value = line_item[1]
    rotator_index_dict[rotator_name] = rotator_value

print(informatics_specialist_list)
print(rotator_index_dict)

is_on_duty_index = int(rotator_index_dict["is_rotator_index"])
is_on_duty = informatics_specialist_list[is_on_duty_index]["name"]

print("Today's IS is: " + is_on_duty)

open_cpi_profile.close()
open_rotator.close()
