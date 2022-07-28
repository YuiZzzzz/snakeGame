

# FIFO队列实现
class Queue:
    def __init__(self):
        self.pos = []

    # 队列添加元素
    def push(self, num):
        self.pos.append(num)

    # 队列删除元素并返回
    def pop(self):
        last = self.pos[-1]
        self.pos.pop(0)
        return last

    # 获取FIFO元素
    def get(self):
        return self.pos[-1]

    # 返回蛇蛇位置信息队列
    def get_queue(self):
        return self.pos




