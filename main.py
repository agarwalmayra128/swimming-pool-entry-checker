age = int(input("how old are you?"))
can_swim = input("can you swim 25 meters(yes/no)?")
adult_here = input("is there any adult with you(yes/no)?")
if age < 4:
    print("age group    :   toddler")
elif age < 12:
    print("age group    :   child")
elif age < 18:
    print("age group    :   teen")
else:
    print("age group    :   adult")
if can_swim == "yes" and adult_here == "yes":
    print("deep pool - you cans swim as an adult is with you.")
if age < 12 or can_swim == "no":
    print("shallow end - stay near the shallow end today.")
if not (adult_here == "yes"):
    print("rememeber - no adult with you,tell the lifegaurd.")
if can_swim != "yes" and can_swim != "no":
    print("input error - please answer the swimming question with yes or no.")
