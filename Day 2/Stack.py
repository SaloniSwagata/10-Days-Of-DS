class Node:
    def __init__(self,value,link_node=None):
        self.value=value
        self.link_node=link_node
    def get_value(self):
        return self.value
    def get_link_node(self):
        return self.link_node
    def set_link_node(self,link_node):
        self.link_node=link_node

class Stack(Node):
    def __init__(self,size,limit=1000):
        self.size=0
        self.limit=limit
        self.top_item=None
        
    def has_space(self):
        return self.limit>self.size
    
    def is_empty(self):
        return self.size<=0
        
    def push(self,value):
        if self.has_space():
            super().__init__(value)
            self.set_link_node(self.top_item)
            self.top_item=value
            self.size+=1
        else:
            print("All out of space")
        
    def pop(self):
        if not self.is_empty():
            item_to_remove=self.top_item
            top_item=self.get_link_node()
            self.size-=1
            return item_to_remove
        else:
            print("Empty Stack")
            return 
    
    def peek(self):
        if not self.is_empty():
            return self.get_value()
        else:
            print("Empty Stack")
            return
        
pizza_stack=Stack(5,8)
pizza_stack.push("A")
pizza_stack.push("B")
print(pizza_stack.pop())
pizza_stack.push("C")
pizza_stack.peek()
