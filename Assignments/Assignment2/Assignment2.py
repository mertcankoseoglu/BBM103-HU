liste = []          # main list with commands
patient_list = []   # current list with patient data
prob_list = []      #probability of patient list


def create(add_patient):
    global patient_list         # patient information list
    name_found = False          # for unique name

    if not patient_list:
        patient_list.append(add_patient)        # add patient information to the list
        with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
            output_file.write("Patient " + add_patient[0] + " is recorded\n")
    else:
        for r in range(len(patient_list)):
            if patient_list[r][0] == add_patient[0]:        # check the patient name
                with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
                    output_file.write("Patient " + add_patient[0] + " cannot be recorded due to duplication\n")
                name_found = True       # patient is recorded, end

        if not name_found:      # to record new patient
            patient_list.append(add_patient)
            with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
                output_file.write("Patient " + add_patient[0] + " is recorded\n")


def remove(remove_patient):
    global patient_list         # current patient list
    found_name = False          # check the name

    for p in range(len(patient_list)):
        if patient_list[p][0] == remove_patient[0]:     # check the name
            found_name = True                           # go to "if found_name"
            patient_list.pop(p)                         # delete the patient from the list
            break

    if found_name:
        with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
            output_file.write("Patient " + remove_patient[0] + " is removed\n")
    else:
        with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
            output_file.write("Patient " + remove_patient[0] + " cannot be removed due to absence\n")


def probability(prob):
    global patient_list
    global prob_list        # list of list name and probability.

    temp_list = []          # example: ['Hayriye','33.33']

    if not patient_list:
        pass
    else:
        for z in range(len(patient_list)):
            if patient_list[z][0] == prob[0]:           # check  the name
                temp_list.append(prob[0])               # add name to temp_list
                x = patient_list[z][4].split('/')       # separate index 4 by \  to get float value
                y = float(float(x[0]) / float(x[1]))    # disease incidence
                f = float(patient_list[z][1])           # treatment risk

                result = y / ((1 - f) + y)              # probability calculation
                result = "%.2f" % (result * 100)        # two decimal numbers

                temp_list.append(result)                # add probability value to temp_list
                prob_list.append(temp_list)             # make list of list

                with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
                    output_file.write("Patient " + prob[0] + " has a probability of " + str(result) + "% of having " +
                                      patient_list[z][2] + " Cancer\n")
                break
        else:
            with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
                output_file.write("Probability for " + prob[0] + " cannot be calculated due to absence.\n")


def list_patient():
    with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
        output_file.write("Patient\tDiagnosis\tDisease\t\tDisease\t\tTreatment\tTreatment\n")
        output_file.write("Name\tAccuracy\tName\t\tIncidence\t\tName\t\tRisk\n")
        output_file.write("-----------------------------------------------------------------\n")

        for patient in patient_list:
            output_file.write("\t".join(patient) + "\n")


def recommendation(recommend):
    global patient_list
    global prob_list
    not_found = False

    for a in range(len(patient_list)):
        for b in range(len(prob_list)):
            not_found = False
            if patient_list[a][0] == prob_list[b][0]:
                if prob_list[b][0] == recommend[0]:     # check the patient name
                    x = float(patient_list[a][-1])      # x = treatment risk
                    if float(prob_list[b][-1]) > float("%.2f" % (x * 100)):     # for 40% > 33%
                        with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
                            output_file.write("System suggests " + recommend[0] + " to have the treatment.\n")
                        break
                    elif float(patient_list[a][-1]) < float(prob_list[b][1]):
                        with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
                            output_file.write("System suggests " + recommend[0] + " NOT to have the treatment.\n")
                        break
                else:
                    not_found = True

    if not_found:
        with open("doctors_aid_outputs.txt", 'a', encoding="utf-8") as output_file:
            output_file.write(
                "Recommendation for " + recommend[0] + "  cannot be calculated due to absence.\n")


# read the input file line by line and append it to the list.
with open('doctors_aid_inputs.txt', encoding='utf-8') as input_file:
    for line in input_file:
        line_list = []
        line_split = line.split()       # separate by space
        for item in line_split:
            x = item.strip(',')         # get rid of comma
            line_list.append(x)
        liste.append(line_list)

for i in range(len(liste)):
    if liste[i][0] == 'create':         # command check
        liste[i].pop(0)
        create(liste[i])

    elif liste[i][0] == 'probability':
        liste[i].pop(0)                 # delete command in the list
        probability(liste[i])

    elif liste[i][0] == 'recommendation':
        liste[i].pop(0)
        recommendation(liste[i])        # send the list to function

    elif liste[i][0] == 'list':
        list_patient()                  # call function

    elif liste[i][0] == 'remove':
        liste[i].pop(0)
        remove(liste[i])
