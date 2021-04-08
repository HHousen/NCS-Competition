import re

with open("50k-users.txt", "r") as file:
    users_list = file.readlines()

users_list = [x.strip() for x in users_list]

r = re.compile("..x[2-6].*S$")
output = list(filter(r.match, users_list))
output = [x for x in output if "Z" in x]
print(output)
# Answer: `YXx52hsi3ZQ5b9rS`
