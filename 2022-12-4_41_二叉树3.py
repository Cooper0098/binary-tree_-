class Treenode():
    def __init__(self,data,left_child=None,right_child=None):
        self.data = data
        self.left_child  = left_child
        self.right_child = right_child
class Bitree():
    def __init__(self):
        self.root = None
        self.list = []
    def add(self,data):
        node = Treenode(data)
        if self.root == None:
            self.root = node
            self.list.append(self.root)
        else:
            rootnode = self.list[0]
            if rootnode.left_child == None:
                rootnode.left_child = node
                self.list.append(rootnode.left_child)
            elif rootnode.right_child == None:
                rootnode.right_child = node
                self.list.append(rootnode.right_child)
                self.list.pop(0)
    def preOrder(self,root):
        if root == None:
            print('',end='')
        else:
            print(root.data,end=' ')
            self.preOrder(root.left_child)
            self.preOrder(root.right_child)

    def inOrder(self,root):
        if root == None:
            print('',end = '')
        else:
            self.inOrder(root.left_child)
            print(root.data,end =' ')
            self.inOrder(root.right_child)

    def postOrder(self,root):
        if root == None:
            print('', end ='')
        else:
            self.preOrder(root.left_child)
            self.preOrder(root.right_child)
            print(root.data,end =' ')

    def Order(self,root):
        Sqqueue0 = Sqqueue(100)
        if root != None:
            Sqqueue0.offer(root)
        while Sqqueue0.front != Sqqueue0.rear:
            node = Sqqueue0.poll()
            print(node.data,end=' ')
            if node.left_child != None:
                Sqqueue0.offer(node.left_child)
            if node.right_child != None:
                Sqqueue0.offer(node.right_child)
        print()
    def get_height(self,root):
        if root == None:
            return 0
        else:
            left_height = self.get_height(root.left_child)
            left_height = left_height + 1
            right_height = self.get_height(root.right_child)
            right_height = right_height + 1
            if left_height > right_height:
                return left_height
            else:
                return right_height
    def get_count(self,root):
        count = 0
        if root != None:
            count +=1
            count += self.get_count(root.left_child)
            count += self.get_count(root.right_child)
        return count

class Sqqueue():
    def __init__(self,maxsize):
        self.listitem = [None]*maxsize
        self.front = 0
        self.rear = 0
        self.maxsize = maxsize
    def offer(self,data):
        if (self.rear+1)%self.maxsize == self.front:
            print('队列已满')
            return None
        else:
            self.listitem[self.rear] = data
            self.rear = (self.rear + 1)%self.maxsize
    def poll(self):
        if self.front == self.rear:
            print('队列为空')
            return None
        else:
            data = self.listitem[self.front]
            self.front = (self.front +1)%self.maxsize
            return data

Bitree0 = Bitree()
a  = input("请输入插入元素:")
while a != '':
    Bitree0.add(a)
    a = input("请输入插入元素:")
print("前序遍历的结果是:",end="")
Bitree0.preOrder(Bitree0.root)
print()
print("中序遍历的结果是:",end="")
Bitree0.inOrder(Bitree0.root)
print()
print("后序遍历的结果是:",end="")
Bitree0.preOrder(Bitree0.root)
print()
print("层次遍历的结果是:",end="")
Bitree0.Order(Bitree0.root)
print()

print('二叉树高度为:%d' % Bitree0.get_height(Bitree0.root))
print('二叉树结点个数为:%d' % Bitree0.get_count(Bitree0.root))







