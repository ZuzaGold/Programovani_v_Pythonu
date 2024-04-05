school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

#průměrná známka studenta na vysvědčení
# sum_of_marks = 0
# for mark in school_report:
#     sum_of_marks += mark[1]
# average = sum_of_marks / len(school_report)
# print(f"Průměrná známka studenta/studentky je {average}.")

# problematické předměty, ty ze kterých má 3
# print("Pro studenta/studentku jsou problematické tyto předměty:")
# for mark in school_report:
#     if mark[1] > 3:
#         print(mark[0])

# vypočítat průměr předmětů důležitých pro technickou školu
#český jazyk, anglický jazyk, matematika, fyzika

# print(school_report[0],
#       school_report[1],
#       school_report[2],
#       school_report[5])

# new_school_report = [
#     ['Český jazyk', 1], 
#     ['Anglický jazyk', 1], 
#     ['Matematika', 1],
#     ['Fyzika', 2],
#  ]

# sum_of_marks = 0
# for mark in new_school_report:
#     sum_of_marks += mark[1]
# average = sum_of_marks / len(school_report)
# print(f"Průměrná známka z vybraných předmětů je {average}.")

#for znamky in new_school_report:
#    soucet_znamky = sum(znamky[1])
#    print(soucet_znamky)


subjects = ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]
sum_of_marks = 0
count_of_subjects = 0

for subject, mark in school_report:
    if subject in subjects:
        sum_of_marks += mark
        count_of_subjects += 1
average = sum_of_marks / count_of_subjects
print(f"průměrná známka ze základních technických předmětů je {average}.")








    







