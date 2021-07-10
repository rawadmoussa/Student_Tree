import sys

class Student:
	def __init__(self, firstname, lastname, major, age):
		self.firstname = firstname
		self.lastname = lastname
		self.major = major
		self.age = age
	def __repr__(self):
	    	return "firstname: " + self.firstname + " , lastname: " + self.lastname + " , major: " + self.major + " , age: " + self.age

class Node:

		def __init__(self, data):
			self.left = None
			self.right = None
			self.data = data

		def insert(self, data):

			if self.data:
				if data.age < self.data.age:
					if self.left is None:
						self.left = Node(data)
					else:
						self.left.insert(data)
				elif data.age > self.data.age:
					if self.right is None:
						self.right = Node(data)
					else:
						self.right.insert(data)
				else:
					self.data = data


		def search(self, value):

			if value < self.data.age:
				if self.left is None:
					return "False"
				return self.left.search(value)
			elif value > self.data.age:
				if self.right is None:
					return "False"
				return self.right.search(value)
			else:
				return 'True'
		    
		def PrintTree(self):
			
			if self.left:
				self.left.PrintTree()
			students.append((self.data.firstname + "," + self.data.lastname + "," + self.data.major + "," + self.data.age))
			if self.right:
				self.right.PrintTree()
			

students = []
studentList = []
f = open(str(sys.argv[1]), "r")
for x in f:
	result = [y.strip() for y in x.split(',')]
	studentList.append ((Student(result[0],result[1],result[2],result[3])))
root = Node (studentList[0])
for i in range (1, len(studentList)):
	root.insert(studentList[i])
print(root.search(sys.argv[2]))
root.PrintTree()
print("This is the sorted list of students : ")
print(students)