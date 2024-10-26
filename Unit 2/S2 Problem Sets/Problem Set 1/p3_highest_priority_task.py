"""
Find highest priority task in tasks. Remove it and return
name of the task of highest priority,.

"""

def get_highest_priority_task(tasks):
	popped = ""
	tasks_dict = sorted(tasks.keys())
	max_value = 0
	for key in tasks_dict:
		if tasks[key] > max_value:
			max_value = tasks[key]
			popped = key
	tasks.pop(popped)
	return popped

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)