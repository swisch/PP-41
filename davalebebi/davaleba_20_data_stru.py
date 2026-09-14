# - თეორიულად აღწერეთ და დააამუშავეთ:
# Linked List, Stack, Queue, Tree


# - გიტოვებთ Doubly Linked List-ის და Tree მაგალითს:
# # DoublyLinkedList
# class House:
#     def __init__(self, address):
#         self.address = address
#         self.next = None
#         self.prev = None

# class Street:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_house(self, address):
#         new_house = House(address)
#         if not self.head:
#             self.head = new_house
#             self.tail = new_house
#         else:
#             self.tail.next = new_house
#             new_house.prev = self.tail
#             self.tail = new_house

#     def show_street_forward(self):
#         current = self.head 
#         print("street forward ")
#         while current:
#             print(current.address, end=' - ')
#             current = current.next

#     def show_street_backward(self):
#         current = self.tail
#         print("Street Backward ")
#         while current:
#             print(current.address, end=' ')
#             current = current.prev


# street = Street()
# street.add_house("A")
# street.add_house("b")
# street.add_house("c")
# street.add_house("d")

# street.show_street_backward()
# street.show_street_forward()

# ------------------------------------------------------------------------------------------------------------

# RA ARIS TREE 
#- ROOT  -  top node 
# - PARENT - node romelsac aqvs 1 an meti child node 
# - child - node romelic pirdapiraa dakavshorebuli imis zemot myof nodetan 
# LEAF - node with no children 

# -------------------------------------------------------------
# CEO - managers - team leads - employees
# class EmployeeNode:
#     def __init__(self, name):
#         self.name = name 
#         self.reports = []

#     def add_report(self, employee_node):
#         self.reports.append(employee_node)

#     def print_hierarchy(self, level = 0):
#         print("  " * level + self.name)

#         for report in self.reports:
#             report.print_hierarchy(level + 1)


#     def find_report(self, manager_name):
#         if self.name == manager_name:
#             return self.collect_all_reports()

#         else:
#             for report in self.reports:
#                 found = report.find_report(manager_name)
#                 if found:
#                     return found 
#             return []
        

#     def collect_all_reports(self):
#         all_reports = []
#         nodes = [self]

#         while nodes:
#             current = nodes.pop()
#             for r in current.reports:
#                 all_reports.append(r.name)
#                 nodes.append(r)
#         return all_reports

# if __name__ == '__main__':
#     ceo = EmployeeNode("CEO")

#     manager_1 = EmployeeNode("MANAGER 1 ")
#     manager_2 = EmployeeNode("MANAGER 2")

#     lead_1 = EmployeeNode("LEAD 1")
#     lead_2 = EmployeeNode("LEAD 2")
#     lead_3 = EmployeeNode("LEAD 3")

#     emp_1 = EmployeeNode("EMPLOYEE 1")
#     emp_2 = EmployeeNode("EMPLOYEE 2")
#     emp_3 = EmployeeNode("EMPLOYEE 3")
#     emp_4 = EmployeeNode("EMPLOYEE 4")

#     ceo.add_report(manager_1)
#     ceo.add_report(manager_2)

#     manager_1.add_report(lead_1)
#     manager_1.add_report(lead_3)
#     manager_2.add_report(lead_2)

#     lead_1.add_report(emp_1)
#     lead_1.add_report(emp_2)
#     lead_2.add_report(emp_3)
#     lead_2.add_report(emp_4)

#     print("Company Hierarchy: ")
#     ceo.print_hierarchy()

#     print('reporting ro manager 1')
#     reports = ceo.find_report("MANAGER 1 ")    
#     print(reports)
