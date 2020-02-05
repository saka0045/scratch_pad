# Open the staging directory list file
staging_file = open("/Users/m006703/Illumina/staging_area_013020.txt", "r")
new_staging_file = open("/Users/m006703/Illumina/staging_area_unique_013020.txt", "w")

# Skip header line
staging_file.readline()

altered_string_list = []
for line in staging_file:
    line = line.rstrip()
    line_item = line.split("/")
    for item in line_item:
        # Remove the fastq file names
        if item.endswith(".fastq.gz"):
            line_item.remove(item)
    altered_string = "/".join(line_item)
    # Only keep unique staging directory names before the fastq files
    if altered_string not in altered_string_list:
        altered_string_list.append(altered_string)

for staging_directory in altered_string_list:
    new_staging_file.write(staging_directory + "\n")

staging_file.close()
new_staging_file.close()
