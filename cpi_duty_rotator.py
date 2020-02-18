#!/usr/bin/env python3

import json


def main():
    open_cpi_profile = open("/Users/m006703/scratch_pad/cpi_profile.json", "r")
    rotator_file = open("/Users/m006703/scratch_pad/duty_rotator_index.txt", "r")

    cpi_profile = json.load(open_cpi_profile)

    # Get the list of names for each role from cpi_profile.json
    informatics_specialist_list = cpi_profile["informatics_specialist"]
    spa_list = cpi_profile["statistical_programmer_analyst"]

    # Read the rotator index file to get the rotator index for each element
    rotator_index_dict = {}
    parse_rotator_index_file(rotator_file, rotator_index_dict)

    rotator_file.close()

    print(informatics_specialist_list)
    print(spa_list)
    print(rotator_index_dict)

    # Get information on IS on duty
    is_on_duty, is_on_duty_index = assign_personnel(informatics_specialist_list, rotator_index_dict,
                                                    "is_rotator_index")
    print("Today's IS is: " + is_on_duty)

    # Get list of ISes on duty for the week
    number_of_IS_for_week = 4
    number_of_IS_chosen = 0
    list_of_IS_for_week = []
    # Start by picking whoever is on duty at the beginning of the week
    is_list_index = is_on_duty_index

    while number_of_IS_chosen < number_of_IS_for_week:
        if is_list_index == len(informatics_specialist_list):
            is_list_index = 0
        else:
            is_for_week = informatics_specialist_list[is_list_index]["name"]
            list_of_IS_for_week.append(is_for_week)
            number_of_IS_chosen += 1
            is_list_index += 1
    print("This week's ISes are:")
    print(list_of_IS_for_week)

    # Get information on SPA on duty
    spa_on_duty, spa_on_duty_index = assign_personnel(spa_list, rotator_index_dict, "spa_rotator_index")
    print("Today's SPA is: " + spa_on_duty)

    # Increment the IS index rotator
    increment_rotator_index(informatics_specialist_list, is_on_duty_index, rotator_index_dict,
                            "is_rotator_index")

    # Increment the SPA index rotator
    increment_rotator_index(spa_list, spa_on_duty_index, rotator_index_dict, "spa_rotator_index")

    # Write the new index information in the rotator text file
    updated_rotator_file = open("/Users/m006703/scratch_pad/duty_rotator_index.txt", "w")

    for key, val in rotator_index_dict.items():
        updated_rotator_file.write(key + "=" + str(val) + "\n")

    open_cpi_profile.close()
    updated_rotator_file.close()


def assign_personnel(personnel_list, rotator_index_dict, index_string):
    """
    Assigns the person performing the duty depending on the rotator index
    :param personnel_list: List of personnel to choose for the duty
    :param rotator_index_dict:
    :param index_string: string, name of index string corresponding from the index text file
    :return: Returns the person performing the duty and their list index
    """
    personnel_index = rotator_index_dict[index_string]
    person_on_duty = personnel_list[personnel_index]["name"]
    return person_on_duty, personnel_index


def increment_rotator_index(list_to_rotate, index_to_increment, rotator_index_dict, index_string):
    """
    Increments the rotator index by 1, if the index becomes out of bounds for the list it will set to 0
    :param list_to_rotate: the list corresponding to the index to increment
    :param index_to_increment: index name to increment
    :param rotator_index_dict:
    :param index_string: string, name of index string in rotator_index_dict to replace
    :return:
    """
    index_to_increment += 1
    # If the index is out of range, reset the index to 0
    if index_to_increment == len(list_to_rotate):
        index_to_increment = 0
    # Replace the value in the rotator_index_dict
    rotator_index_dict[index_string] = index_to_increment


def parse_rotator_index_file(rotator_file, rotator_index_dict):
    """
    Parses the rotator index file to make the rotator_index_dict
    :param rotator_file:
    :param rotator_index_dict:
    :return:
    """
    for line in rotator_file:
        line = line.rstrip()
        line_item = line.split("=")
        rotator_name = line_item[0]
        rotator_value = int(line_item[1])
        rotator_index_dict[rotator_name] = rotator_value


if __name__ == "__main__":
    main()
