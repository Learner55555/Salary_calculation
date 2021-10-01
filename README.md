# # Salary calculation based on the performance

# Project purpose
This project is created to calculate the salary of the workers based on their performance.

# Input variables
a) **Workers' personal infrmation**: 
List of dictionaries is used to store personal information. This information is saved in name_lists.

1) Worker name
2) Worker surname
3) Worker patronmic
4) Worker id --> Make sure to input integer number, otherwise there will an error as it only accepts integers


Sample output: [{'name': 'Zafarbek', 'surname': 'Tolipov', 'patronmic': 'Excellency', 'id_number': 89}, {'name': 'Otabek', 'surname': 'Polishev', 'patronmic': "Polishev's son", 'id_number': 56}]


b) **Work name, Work information**: 
List of lists is used to store job name and its cost. This information is saved in outer_cost_list.

1) Work name
2) Work cost --> Make sure to input integer number, otherwise there will an error as it only accepts integers

Sample output: outer_cost_list = [['Pol yuvish', 500], ['Kir yuvish', 900]]

b) **Worker id, Name of the work done, How many times**: 
List of lists is used to worker id, done work name and how many times the work was done. This information is saved in general_list.

1) Worker id
2) Name of the work done by the worker
3) How many times the work was done by the worker --> Make sure to input integer number, otherwise there will an error as it only accepts integers

Sample output: general_list=[[56, 'Pol yuvish', 5, 'Kir yuvish', 9], [89, 'Pol yuvish', 6, 'Kir yuvish', 8]]


# Output variables
After inserting all the variables, salary_calculator_function function calculates the salary.
Sample output: Zafarbek salary: 254400
               Otabek salary: 244800
