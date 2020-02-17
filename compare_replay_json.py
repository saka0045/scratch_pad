import json

open_remote_json = open("/Users/m006703/Downloads/YutaNewTest-replay.json", "r")
open_local_json = open("/Users/m006703/Illumina/WES-NA12878-CTRL-replay.json", "r")

remote_json_file = json.load(open_remote_json)
local_json_file = json.load(open_local_json)

remote_dragen_config = remote_json_file["dragen_config"]
local_dragen_config = local_json_file["dragen_config"]

# Make the remote dragen config to a dicationary since it's in list format now
remote_dragen_dict = {}

for index in range(len(remote_dragen_config)):
    remote_name = remote_dragen_config[index]["name"]
    remote_value = remote_dragen_config[index]["value"]
    remote_dragen_dict[remote_name] = remote_value

# Check the local dragen config against the remote dragen config dict
for index in range(len(local_dragen_config)):
    local_name = local_dragen_config[index]["name"]
    local_value = local_dragen_config[index]["value"]
    if local_name in remote_dragen_dict.keys():
        if local_value != remote_dragen_dict[local_name]:
            print(local_name + " has different value from remote")
            print("local value is: " + local_value)
            print("remote value is: " + remote_dragen_dict[local_name] + "\n")
    else:
        print(local_name + " is not in remote dragen configs\n")

open_remote_json.close()
open_local_json.close()
