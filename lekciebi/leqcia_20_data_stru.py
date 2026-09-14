# # data structures -

# # list, set, tuple, dict - built-in python collections    (element)

# # linked_list, stack, queue    (element+pointer -> element+pointer )

# # linked_list - singly, doubly, circular

# # node - data+pointer
# # data - element
# # next - pointer rom mivutitot shemdeg node-ze
# # None - meti node roca aghar aris 

# # singly-linkedlist 
# # 1 2 3 4 
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.next = None

# class PersonLine:
#     def __init__(self):
#         self.head = None

#     def join_line(self, name):
#         new_person = Person(name)
#         if not self.head:
#             self.head = new_person
#         else:
#             current = self.head # last person   1 2 3 4
#             while current.next:
#                 current = current.next

#             current.next = new_person  # last person linked to the new person 

#     def serve_next(self):
#         if not self.head:
#             print("No one in line ")
#             return None
#         served = self.head
#         self.head = self.head.next
#         print(f"{served.name} is leaving the line")
#         return served.name

#     def show_line(self):
#         current = self.head
#         print(f"Line: ")
#         while current:
#             print(current.name)
#             current = current.next

# line = PersonLine()
# line.join_line("A")
# line.join_line("B")
# line.join_line("C")

# line.show_line()

# line.serve_next()
# line.show_line()


# # prev
# # --------------------------------------------------------------------------------------------------------------------------

# # STACK - LIFO - Last in first out

# # BROWSER HISTORY

# class BrowserHistory:
#     def __init__(self):
#         self.history_stack = []

#     def visit(self, url):
#         self.history_stack.append(url)
#         print(f"Visit: {url}")

#     def back(self):
#         if len(self.history_stack) <= 1:
#             print("Not previous pages")
#             return None

#         last = self.history_stack.pop()
#         print(f"GOing from {last} to {self.history_stack[-1]}")
#         return self.history_stack[-1]

    


#     def current_page(self):
#         if not self.history_stack:
#             print("Not visited pages")
#             return None 
#         print(f"current page: {self.history_stack[-1]}")
#         return self.history_stack[-1]


# browser = BrowserHistory()
# browser.visit("A")
# browser.visit("B")
# browser.visit("C")

# browser.current_page()

# browser.back()

# browser.current_page()
# # browser.back()


# -------------------------------------------------------------------

# QUEUES - FIFO (first in first out)
# from collections import deque
# import time

# customer_queue = deque()
# def add_customers():
#     print("Customers join")
#     customer_queue.append("1")
#     time.sleep(3)
#     customer_queue.append("2")
#     time.sleep(3)
#     customer_queue.append("3")

#     print("all customers have joined ")

# def serve_line():
#     print("customer service started")

#     while customer_queue:
#         current_customer = customer_queue.popleft()
#         print(f"serve: {current_customer}")
#         time.sleep(2)
#     print("all customers left the queue")

# if __name__ == "__main__":
#     add_customers()
#     serve_line()


# -----------------------------------------------------------------------------------------------------
# TREE
# root, parent, child, leaf, subtree
# O(n) - 
            
# linked_list, queue, tree, stack 
# linked_List - doubly, circuit




