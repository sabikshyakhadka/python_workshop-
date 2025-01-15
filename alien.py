from collections import Counter

#simple text 
text = """ 
python is an amazing programming language. python is fun to learn and powerful to use
 """
 #split text into words and count frequency 
words = text.lower().split()
words_count = Counter(words)

 #display word frequently 
print("words frequencies")
for words, count in words_count.items():
    print(f"{words}:{count}")


from queue import Queue 
task_queue = Queue()

#create a tasks to the Queue
tasks = ["task 1: clean the room", "task 2: write the python program", "task 3 : read a nobel"]
for task in tasks:
    task_queue.put(task) 

# process tasks 
print("processing tasks ")
while not task_queue.empty():
    print(task_queue.get())
