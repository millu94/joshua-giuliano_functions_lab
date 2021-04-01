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

# 4. Print a list of tasks where time_taken is at least a given time

def time_taken_over_20(list):
    
    time = []
    for task in tasks:
        if task['time_taken'] >= 20:
            time.append(task['description'])
    return time

print(time_taken_over_20(tasks))

# 5. Print any task with a given description

def clean_windows_print(list, job):
    
    for task in tasks:
        if task['description'] == job:
            return job

print(clean_windows_print(tasks, 'Clean Windows'))