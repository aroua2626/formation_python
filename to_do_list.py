import random
tasks=[]
print("TO DO LIST:")
print("1-add a new task")
print("2-Search for a task by ID or Name")
print("3-Delete a given task by ID or Name")
print("4-Update Status of a task by ID or Name")
print("5-List all tasks")
print("6-List using filtering by Tag or Status or together")
print("7-Show Stats( all tasks, new tasks, completed tasks, highs tasks, low tasks).")
print("8-q to quit")

#add a new task
def add_task():
  id=random.randint(1,20)
  name=input("name:")
  description=input("description:")
  status=input("status:")
  tag=input("tag:")
  task={"id":id,"name":name,"description":description,"status":status,"tag":tag}
  tasks.append(task)
  print(tasks)
 

#Search for a task by ID or Name
def search():
 mysearch=input("enter your search:")
 for task in tasks:
  if task["name"]==mysearch :
    print(tasks)
    return print("yes")
  else:
    return print("no")
  
#Delete a given task by ID or Name
def delete():
  NAME=input("enter the name to delete:").lower()
  ID=input("enter the id to delete:").lower()
  if tasks:
    for task in tasks:
      if task["name"]==NAME:
        print(tasks)
        tasks.remove(task)
        print(tasks)
        return
  else:
    print("is empty")



#Update Status of a task by ID or Name
def update():
  NAME=input("enter the name to update:").lower()
  ID=input("enter the id to update:").lower()
  for task in tasks:
    if task["name"]==NAME or task["id"]==ID:
      newstatus=input("enter the new status:")
      task["status"]=newstatus
    return

#List all tasks
def tasks_list():
 if tasks:
    for task in tasks:
      print(task)
 else:  
    print("it's empty")  
   
#List using filtering by Tag or Status or together
def filter_list():
  tag_filter=input("enter the tag filter:")
  status_filter=input("enter the status filter:")
  if tasks:
    for task in tasks:
      if (task["tag"]==tag_filter) or (task["status"]==status_filter) or(task["tag"]==tag_filter and task["status"]==status_filter):
       print(task)

#Show Stats( all tasks, new tasks, completed tasks, highs tasks, low tasks).
def show():
  sum_new=0
  sum_completed=0
  sum_high=0
  sum_low=0
  if tasks:
    print("length of task",len(tasks))
    for task in tasks:
      if task["status"]=="new":
        sum_new=sum_new+1
        print("length of new task",sum_new)
      elif task["status"]=="completed":
          sum_completed=sum_completed+1
          print("length of completed task",sum_completed)
      if task["tag"]=="high":
          sum_high=sum_high+1
          print("length of high task",sum_high)
      elif task["tag"]=="low":
          sum_low=sum_low+1
          print("length of low task",sum_low)        
  else:
    print("empty") 


while True:
   choice = input("Enter your choice: ")
   if choice=='1':
    add_task()
   elif choice=='2':
    search()
   elif choice=='3':
    delete()
   elif choice=='4':
    update()
   elif choice=='5':
    tasks_list()
   elif choice=='6':
     filter_list()
   elif choice=='7':
    show()
   elif choice.lower()=='q':
    break
   else:
    print("Invalid choice. Please run the program again and select a valid choice.")
