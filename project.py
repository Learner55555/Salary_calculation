# ------------------- Worker information ------------------- # Done OK list of dictionaries
name_lists=[]

flag = ""
while(flag.lower() != "n" or flag.upper() != "N"):
    d = {}
    d["name"] = input("Enter worker's name: ")
    d["surname"] = input("Enter worker's surname: ")
    d["patronmic"] = input("Enter worker's patronmic: ")
    d["id_number"] = int(input("Enter worker's id: "))
    name_lists.append(d)
    flag = input("Continue inputting worker personal data Y/N: ")
print(name_lists)

# # # # # ------------------- Job name, cost information ------------------- # Done OK list of lists
outer_cost_list=[]
flag = ""
while(flag.lower() != "n" or flag.upper() != "N"):
    inner_cost_list = []
    inner_cost_list.append(input("Enter a work name: "))
    inner_cost_list.append(int(input("Enter a work cost: ")))
    outer_cost_list.append(inner_cost_list)
    flag = input("Continue inputting data Y/N: ")
print(outer_cost_list)

# # # ------------------- Function definition ------------------- #

def salary_calculator_function(general_list):
    w=0
    general_work_salary=0
    for i in range(len(general_list)):#number of lists(2)
        h=0
        for j in range(len(general_list[w])):
            if j%2!=0:
                if general_list[i][j] == outer_cost_list[h][0]: # Zero because first element for the dictionary must always be checked
                    general_work_salary += outer_cost_list[h][1]*general_list[i][j+1]
                    h+=1
        for k in range(len(name_lists)):
            if general_list[i][0] == name_lists[k]['id_number']:
                print(name_lists[i]['name'], 'salary: ' + str(general_work_salary*24)) # Multiplied by 24, because on average a worker works for 24 days a month.
        general_work_salary = 0
        # print(i)
        w+=1
# Sample data:
# general_list=[[56, 'Pol yuvish', 5, 'Kir yuvish', 9], [89, 'Pol yuvish', 6, 'Kir yuvish', 8]]
# name_lists = [{'name': 'Muhammad', 'surname': 'Tolipov', 'patronmic': 'Excellency', 'id_number': 89}, {'name': 'Dilmurod', 'surname': 'Polishev', 'patronmic': "Polishev's son", 'id_number': 56}]
# outer_cost_list = [['Pol yuvish', 500], ['Kir yuvish', 900]]

# ------------------- Id, job, times ------------------- #

general_list=[]
flag=""
while(flag.lower() != "n" or flag.upper() != "N"):
    inner_list=[]
    inner_list.append(int(input("Enter id: ")))
    flag2='Y'
    i = 1
    while(flag2.lower() != "n" or flag2.upper() != "N"):
        inner_list.append(input("Enter job: "))
        inner_list.append(int(input("Enter times: ")))
        flag2 = input("Is there any done for this worker Y/N: ")
    general_list.append(inner_list)
    flag = input("Is there any other worker's information to add Y/N: ")

# ------------------- Function call ------------------- #

# print(general_list)
salary_calculator_function(general_list)



