import re
# there is an ape in apex
# all_apes = re.findall("ape", "The ape was at the apex")

# for i in all_apes:
#     print(i)

the_str = "ape", "The ape was at the apex"
for i in re.finditer("ape", the_str):
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])