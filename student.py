students=[
    {'name':'ram','gender':'male','status':True},
    {'name':'sita','gender':'female','status':True},
    {'name':'gita','gender':'female','status':False},
    {'name':'hari','gender':'male','status':False},
    {'name':'gopal','gender':'male','status':False},
    {'name':'laxmi','gender':'female','status':True},
    {'name':'sophia','gender':'female','status':True}
]

# total_users=len(students)
# total_male=0
# total_female=0
# total_active_user=0
# total_inactive_user=0
# total_active_male=0
# total_active_female=0
# total_inactive_male=0   
# total_inactive_female=0


# Total users 
for i in range(len(students)+1):
    total_users = i

print(f"Total users: {total_users}")



# Total male 
total_male = 0
for i in students:
    if i['gender'] == 'male':
     total_male += 1
    
    
print(f"Total number of male: {total_male}")


# Total female 
total_female = 0
for i in students:
     total_female += 1
    
    
print(f"Total number of female: {total_female}")



# Total activce users
total_active = 0
for i in students:
    if i['status']:
        total_active += 1

print(f"Total active users: {total_active}")


# Total inactivce users
total_inactive = 0
for i in students:
    if not i['status']:
        total_inactive += 1

print(f"Total inactive users: {total_inactive}")


# Total active male 

total_active_male = 0
for i in students:
    if i['gender'] == 'male' and i['status']:
        total_active_male += 1

print(f"Total active male: {total_active_male}")



# Total active female 

total_active_female = 0
for i in students:
    if i['gender'] == 'female' and i['status']:
        total_active_female += 1

print(f"Total active female: {total_active_female}")


# Total inactive male 

total_inactive_male = 0
for i in students:
    if i['gender'] == 'male' and  not i['status']:
        total_inactive_male += 1

print(f"Total inactive male: {total_inactive_male}")



# Total inactive female 

total_inactive_female = 0
for i in students:
    if i['gender'] == 'female' and  not i['status']:
        total_inactive_female += 1

print(f"Total inactive female: {total_inactive_female}")



