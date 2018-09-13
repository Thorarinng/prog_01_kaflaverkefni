# Hlynur Magnus Magnusson 
# hlynurm18@ru.is

# Les inn manud og dag
manudur = input("Month: ")
dagur = int(input("Day: "))

# Fyrsti stafur hastafur
manudur = manudur.capitalize()

# Setja saman i einn streng
daga_check = manudur + " " + str(dagur)

if daga_check == "January 1":
    print("New year's day")
elif daga_check == "June 17":
    print("National holiday")
elif daga_check == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")

# if manudur == "Januari" and dagur == 1:
#     print("New year's day")
# elif manudur == "June" and dagur == 17:
#     print("National holiday")
# elif manudur == "December" and dagur == 25:
#     print("Christmas day")
# else:
#     print("Not a holiday")