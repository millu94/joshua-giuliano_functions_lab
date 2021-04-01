tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# 1  Print a list of uncompleted tasks

def uncompleted_tasks(list, completed):
    jobs = []
    for task in tasks:
        if 'completed' == False:
            return task

print(uncompleted_tasks(tasks, completed))

