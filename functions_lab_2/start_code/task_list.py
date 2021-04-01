import pdb

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# 1  Print a list of uncompleted tasks

def uncompleted_tasks(list):
    
    jobs = []
    for task in tasks:
        if task['completed'] == False:
            jobs.append(task['description'])
    return jobs

print(uncompleted_tasks(tasks))

# 2. Print a list of completed tasks

def completed_tasks(list):
    
    jobs = []
    for task in tasks:
        if task['completed'] == True:
            jobs.append(task['description'])
    return jobs

print(completed_tasks(tasks))


# 3. Print a list of all task descriptions

def all_tasks(list):
    
    jobs = []
    for task in tasks:
        jobs.append(task['description'])
    return jobs

print(all_tasks(tasks))