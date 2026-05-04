import time
import random
import json
import os

def progress_bar(percentage):
    print()
    for i in range(percentage + 1):
        filled = int(i / 10)
        empty = 10 - filled
        bar = "▓" * filled + "░" * empty
        print(f"\r[{bar}] {i}%", end="")
        time.sleep(0.05)
    print()

def save_data(data):
    with open("student_data.json", "w") as f:
        json.dump(data, f)
    print("Data saved!")

def load_data():
    if os.path.exists("student_data.json"):
        with open("student_data.json", "r") as f:
            return json.load(f)
    return {"grades": [], "attendance": [], "skills": []}

print("========================================================")
print("            Student Career Assistant                    ")
print("========================================================")

name = input("Enter your name: ")
student_id = input("Enter your student ID: ")

print(f"\nWelcome, {name}!")
binary_id = bin(int(student_id))[2:]
print(f"Your Binary ID: {binary_id}")

data = load_data()
skills = data["skills"]
grades = data["grades"]
attendance = data["attendance"]

while True:
    print("\n--- MENU ---")
    print("1. View Grades")
    print("2. Attendance")
    print("3. Skills")
    print("4. My Progress Summary")
    print("5. Quit")

    choice = input("\nChoose (1-5): ")

    if choice == "1":
        while True:
            print("\nGrade Tracker:\n")
            print("1. Add Grade")
            print("2. View All Grades")
            print("3. Return to Main Menu")
            grade_choice = input("\nChoose (1-3): ")

            if grade_choice == "1":
                subject = input("Enter subject name: ")
                grade = int(input(f"Enter your grade % in {subject}: ").replace("%", ""))
                print(f"\n{subject} Progress:")
                progress_bar(grade)
                if grade < 50:
                    print("!! Warning: Grade is critically low! Study harder!")
                elif grade < 75:
                    print(">> You're getting there, keep pushing!")
                else:
                    print("** Excellent grade, keep it up!")
                grades.append({"subject": subject, "grade": grade})
                data["grades"] = grades
                save_data(data)
                input("\nPress Enter to continue...")

            elif grade_choice == "2":
                if len(grades) == 0:
                    print("No grades recorded yet!")
                else:
                    print("\nYour Grade History:")
                    for i, g in enumerate(grades, 1):
                        print(f"{i}. {g['subject']}: {g['grade']}%")
                        progress_bar(g['grade'])
                input("\nPress Enter to continue...")

            elif grade_choice == "3":
                break
            else:
                print("Invalid choice!")

    elif choice == "2":
        while True:
            print("\nAttendance Tracker:\n")
            print("1. Add Attendance")
            print("2. View All Attendance")
            print("3. Return to Main Menu")
            att_choice = input("\nChoose (1-3): ")

            if att_choice == "1":
                total_classes = int(input("Total classes held: "))
                attended = int(input("Classes you attended: "))
                if attended > total_classes:
                    print("You can't attend more classes than total!")
                else:
                    percentage = int((attended / total_classes) * 100)
                    print(f"\nYour Attendance:")
                    progress_bar(percentage)
                    if percentage < 75:
                        print("!! Warning: Attendance is too low!")
                    elif percentage < 90:
                        print(">> Good but try to improve!")
                    else:
                        print("** Excellent attendance!")
                    attendance.append({"total": total_classes, "attended": attended, "percentage": percentage})
                    data["attendance"] = attendance
                    save_data(data)
                input("\nPress Enter to continue...")

            elif att_choice == "2":
                if len(attendance) == 0:
                    print("No attendance recorded yet!")
                else:
                    print("\nYour Attendance History:")
                    for i, a in enumerate(attendance, 1):
                        print(f"{i}. Total: {a['total']} | Attended: {a['attended']} | {a['percentage']}%")
                input("\nPress Enter to continue...")

            elif att_choice == "3":
                break

    elif choice == "3":
        while True:
            print("\nSkills Tracker:\n")
            print("1. Add a skill")
            print("2. View my skills")
            print("3. Return to Main Menu")
            skills_choice = input("\nChoose (1-3): ")

            if skills_choice == "1":
                new_skill = input("Enter a skill you learned: ")
                skills.append(new_skill)
                print(f"'{new_skill}' added to your skills!")
                data["skills"] = skills
                save_data(data)
                input("\nPress Enter to continue...")

            elif skills_choice == "2":
                if len(skills) == 0:
                    print("No skills added yet!")
                else:
                    print("\nYour Skills:")
                    for i, skill in enumerate(skills, 1):
                        print(f"{i}. {skill}")
                input("\nPress Enter to continue...")

            elif skills_choice == "3":
                break

    elif choice == "4":
        print("\n--- Progress Summary & Personal Advisor ---\n")
        time.sleep(0.5)

        if len(grades) == 0:
            print("No grades recorded yet! Add some grades first.")
            input("\nPress Enter to return to menu...")
        else:
            avg_grade = round(sum(g["grade"] for g in grades) / len(grades))

            if len(attendance) > 0:
                last_att = attendance[-1]["percentage"]
            else:
                last_att = 100

            print(f"Student: {name}")
            print(f"Skills learned: {len(skills)}")
            print(f"Grades recorded: {len(grades)}")
            print(f"Average Grade: {avg_grade}%")
            print()
            progress_bar(avg_grade)
            print()

            if avg_grade >= 85:
                print("=" * 50)
                print("  [OUTSTANDING PERFORMANCE!]")
                print("=" * 50)
                print(f"\n{name}, you are absolutely crushing it!")
                print("You should be incredibly proud of yourself.")
                print("Not everyone can reach this level -- you did!")
                print()
                print(">> Keep doing what you are doing")
                print(">> Consider helping your classmates")
                print(">> Start exploring advanced topics")
                print(">> You are university ready!")

            elif avg_grade >= 70:
                print("=" * 50)
                print("  [GREAT WORK - KEEP PUSHING!]")
                print("=" * 50)
                print(f"\n{name}, you are doing really well!")
                print("You are above average and improving!")
                print("Just a little more push and you will be exceptional!")
                print()
                print(">> Review your weakest subject daily")
                print(">> You are closer to the top than you think")
                print(">> Stay consistent and results will follow")
                print(">> Proud of your progress so far!")

            elif avg_grade >= 50:
                print("=" * 50)
                print("  [AVERAGE - YOU CAN DO BETTER!]")
                print("=" * 50)
                print(f"\n{name}, you are getting there!")
                print("Average is not your limit -- it is your starting point!")
                print("You have everything it takes to improve!")
                print()
                print(">> Study for at least 1 hour daily")
                print(">> Focus on one subject at a time")
                print(">> Ask for help when stuck -- it is smart not weak")
                print(">> Small improvements every day add up big!")

            else:
                print("=" * 50)
                print("  [NEEDS IMPROVEMENT - LET US FIX THIS!]")
                print("=" * 50)
                print(f"\n{name}, it is okay -- every expert was once a beginner!")
                print("Your grades do not define you but they do need attention.")
                print("The fact that you are tracking them means you care!")
                print()
                print(">> Start with just 30 minutes of focused study")
                print(">> Re-read your notes from the beginning")
                print(">> Remove distractions when studying")
                print(">> Talk to your teacher -- they want to help you!")
                print(">> You CAN turn this around, starting today!")

            print()
            if last_att < 75:
                print("[!] Attendance Warning:")
                print(f"    Your attendance is at {last_att}%")
                print("    Missing classes is hurting your grades!")
                print("    Attend every class starting tomorrow!")
            elif last_att < 90:
                print("[i] Attendance Note:")
                print(f"    Attendance at {last_att}% -- try to get above 90%!")
            else:
                print("[*] Attendance:")
                print(f"    Great attendance at {last_att}%! Keep showing up!")

            print()
            if len(skills) == 0:
                print("[i] Skills: Start adding skills you are learning!")
            elif len(skills) < 3:
                print(f"[*] Skills: Good start with {len(skills)} skill(s)! Keep adding more!")
            else:
                print(f"[*] Skills: Impressive! You have learned {len(skills)} skills!")

            print()
            print("-" * 50)
            tips = [
                "Study in short 25-minute sessions with breaks!",
                "Review your notes within 24 hours of class!",
                "Teach what you learned to truly understand it!",
                "Consistency beats cramming every single time!",
                "Focus on your weakest subject when energy is high!"
            ]
            selected = random.sample(tips, 2)
            print("Personal Tips:")
            for i, tip in enumerate(selected, 1):
                print(f"  Tip {i}: {tip}")
            print("-" * 50)
            input("\nPress Enter to return to menu...")

    elif choice == "5":
        print(f"\nGoodbye {name}! Keep hustling!")
        break

    else:
        print("Invalid choice! Pick 1-5")