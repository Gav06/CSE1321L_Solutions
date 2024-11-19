

STD_COMP_TIME = 15
STD_SERVER_TIME = 19

BTLCKR_COMP_TIME = 39
BTLCKR_SERVER_TIME = 57

print("[Post-Crowdstrike Plan]")

dep = 1
another = True

std_comps_broken = 0
bitlocker_comps_broken = 0

std_servers_broken = 0
bitlocker_servers_broken = 0


while another:
    print(f"Department {dep}")
    total_comps = int(input("How many computers need to be fixed? "))
    bitlocker_comps = int(input("How many of those computers had Bitlocker enabled? "))
    std_comps = total_comps - bitlocker_comps

    std_comps_broken += std_comps
    bitlocker_comps_broken += bitlocker_comps

    total_servers = int(input("How many servers need to be fixed? "))
    bitlocker_servers = int(input("How many of those servers had Bitlocker enabled? "))
    std_servers = total_servers - bitlocker_servers

    std_servers_broken += std_servers
    bitlocker_servers_broken += bitlocker_servers

    choice = input("Is there another department? (Y/N) ")

    if choice != "Y":
        another = False
    else:
        dep += 1


std_c_repairs = std_comps_broken * STD_COMP_TIME
btlr_c_repairs = bitlocker_comps_broken * BTLCKR_COMP_TIME

std_s_repairs = std_servers_broken * STD_SERVER_TIME
btlr_s_repairs = bitlocker_servers_broken * BTLCKR_SERVER_TIME

overall_time = std_c_repairs + btlr_c_repairs + std_s_repairs + btlr_s_repairs

print(f"Across all departments, there are {std_comps_broken + bitlocker_comps_broken} "
      f"computers and {std_servers_broken + bitlocker_servers_broken} servers. "
      f"Of those, {bitlocker_comps_broken} computers and {bitlocker_servers_broken} servers had Bitlocker enabled.")

print(f"The {std_comps_broken} computers without Bitlocker will take {std_c_repairs} minutes to fix.")
print(f"The {bitlocker_comps_broken} computers with Bitlocker will take {btlr_c_repairs} minutes to fix.")

print(f"The {std_servers_broken} computers without Bitlocker will take {std_s_repairs} minutes to fix.")
print(f"The {bitlocker_servers_broken} computers without Bitlocker will take {btlr_s_repairs} minutes to fix.")

print(f"Assuming we fix them one at a time, it will take {overall_time} minutes to repair all devices.")