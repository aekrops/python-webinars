from abc import ABC, abstractmethod
from random import randint

class AbstractParent(ABC):

	@abstractmethod
	def hello_friend(self):
		raise NotImplementedError

class Mother(AbstractParent):
	def __init__(self, age = 0):
		self.age = age
		print('Mother constructor!')

	def do_work(self):
		print("I'm working")

	def do_house_work(self):
		print('listening music')

class Father(AbstractParent):
	def __init__(self, name = None):
		print('Father constructor!')

	def play_guitar(self):
		print('play guitar')

	def do_house_work(self):
		print('sitting on the sofa and drink beer')


class Daughter(Mother, Father):
	
	def __init__(self, age = 0, name = None):
		Mother.__init__(self, age=age)
		Father.__init__(self, name=name)

	def do_work(self):
		print("I'm working like a horse!")

	def hello_friend(self):
		pass

	def visit_university(self):
		print("Daughter visited the University")

class Friend:
	pass

def greet_mother(mother : Mother):
	print("Hello mother!!!")
	mother.do_work()


def greet_father(father : Father):
	print('time to beer!')
	father.play_guitar()




if __name__ == "__main__":

	daughter = Daughter()
	#mother.do_work()

	#change object class
	#daughter.__class__ = Friend

	greet_mother(daughter)
	greet_father(daughter)
	print('Age: ', daughter.age)

	daughter.hello_friend()
	daughter.do_house_work()

	for x in [daughter]:
		x.do_house_work()

	#list
	povtorka_list = ['mathan_2', 'mathan_3', 'mathan D:']
	print(povtorka_list)

	#tuple 
	vasian = ('11 years', 12, 3.14, daughter)

	#set
	my_set = {23, 11, 10, 10 , 10, 'call'}
	print(my_set)

	#frozen set 
	another_set = frozenset(['di_', 'mi_', 'do'])
	print(another_set)

	#dictionary
	dictionary = {'japanese' : "kon'nichiwa", 'chinese' : "nihao"}
	nums = 0
	for num in range(10):
		nums += num 

	dictionary['nums'] = nums
	dictionary['random_number'] = randint(0, 100)
	print(dictionary.values())
