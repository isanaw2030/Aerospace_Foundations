# Nested condition
# 1 Create a program to check for an age, age >= 18 == Adult, age >=60 == senior adult, else == minor
# 2 Create a grading program for grades analysis, score >= 80 == excellent, score >= 50 == pass, score else == below average

# 1 Age checker

age = int(input("Enter age: "))

if age >= 18:

    if age >= 60:
        print("Senior Adult 🧔🏽")
    else:
        print("Adult 👨")

else:
    print("A minor 👦")


print("========= 🛰️ Reliable Age Checker deployed successfully 🏁 ============")

# Grading Analysis 

print("========== 📊 Performing grading analysis 📊 ==============")

score = int(input("Enter a score: "))

if score >= 50:

    if score >= 80:
        print("Excellent 🚀🎉")
    else:
        print("Pass ✅")

else:
    print("Below average, try again! 👍")

print("=========== 🛰️ Successfully deployed super charged grading system 🏁 =====================")

