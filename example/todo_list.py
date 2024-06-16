def print_todo(todo):
    print(f"{todo['name']}: {todo['description']}")

def take_first(todo_list):
    first_todo=todo_list.pop()
    print("Here's your todo for now:")
    print_todo(first_todo)
    print("These are your remaining todos:")
    for todo in todo_list:
        print_todo(todo)

def sum_points(todo_list):
    points=0
    for todo in todo_list:
        points+=todo['points']
    return points
        

todo_list=[{'name':'Staubsaugen','description':'Einmal mit dem Staubsauger die Wohnung durchsaugen','points':2},
          {'name':'Aufräumen','description':'Das muss hier alles seine Ordnung haben','points':7},
          {'name':'Altglas wegbringen','description':'Schließlich bringt sich das scheiß Glas nicht von selber weg!','points':5}]


print("Here's the full todo list")
for todo in todo_list:
    print_todo(todo)
print(f"The total amount of time you need to finish all todos is {sum_points(todo_list)} hours")

print("Let's pick one todo")
take_first(todo_list)

print("And another one!")
take_first(todo_list)
