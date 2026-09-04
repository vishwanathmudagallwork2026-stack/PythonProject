# age = 20
# has_id = True
# has_sober = True
# if (age >= 18 and has_id) and has_sober:
#     print("you can Drive")
# else:
#     print("you cannot Drive")
#
#
#






# Real example: allow access if NOT (banned or underage)
is_banned = False
is_underage = True

if not (is_banned or is_underage):
    print("Access granted")
else:
    print("Access denied")



