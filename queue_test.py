from queue import Queue

q = Queue()
q.push((50,100))
print(q.get_queue())

new_node_x, new_node_y = q.get()
new_node_y += 10

q.push((new_node_x, new_node_y))
print(q.get_queue())

last_node = q.pop()
print(q.get_queue())
