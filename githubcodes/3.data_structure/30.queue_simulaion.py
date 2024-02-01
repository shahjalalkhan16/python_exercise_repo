from queue import Queue

q = Queue()

q.put("Arif")
q.put(1)
q.put("Mamun")

print(q.get())