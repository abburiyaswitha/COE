project = int(input("Enter project marks:"))
internal = int(input("Enter internal marks:"))
external = int(input("Enter external marks:"))
if project >= 50 and internal >= 50 and external >= 50:
    total_marks = (0.7 * project) + (0.1 * internal) + (0.2 * external)
    if total_marks >= 90:
        print("A grade")
    elif total_marks >= 80:
        print("B grade")
    elif total_marks >= 50:
        print("C grade")
    else:
        print("Fail")
else:
    if project < 50:
        print("Failed in project")
    if internal < 50:
        print("Failed in internal")
    if external < 50:
        print("Failed in external")
