# This is a sample Python script to practice and review some OOP, classes and basic methods

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)

s1 = Student('Nando', 29, 90)
s2 = Student('Paco',34, 60)
s3 = Student('Luis', 28, 83)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)

print(s1.name)
print(course.students[0].name)
print(course.get_average_grade())

print(course.add_student(s3)) #this will return a false and it wont change the average below because the Max students is 2!
print(course.get_average_grade())

################### lets practice with inheritance
print('lets practice with inheritance !!!!!!!!!!!!!!!!!!!!!!!!')

class Cattest:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Meow')

class Dogtest:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print('Bark')

cat1test = Cattest('Roberto', 8)
cat2test = Cattest('Lola', 14)
dog1test = Dogtest('Ringo', 16)
cat1test.speak()
cat2test.speak()
dog1test.speak()

#now as Cattest and Dogtest has similar __init__ we want to combine then
#we will create an upper level class Pet

class Pet: #this is the general class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):   #this is only to show me all the things about my objects
        print(f'i am {self.name} and i am {self.age} years old')
    def speak(self):
        print('I dont know what i am but this is a Object class Pet method')

#Cat and Dog are more specific classes that have been created an inheritate from Pet
class Cat(Pet): #adding the (Pet) we are inheritating the upper level class Pet
    def speak(self):
        print('Meow')
class Dog(Pet):
    def speak(self):
        print('Bark')


p = Pet('Paco', 30)
p.show() #this show me the details of the Pet class
p.speak() #this is printing the speak method from the Pet function becuase its a Pet object
c = Cat('Bill', 34)
c.show() #so even if def show is not inside Class Cat we can still use the method .show with Cat objects
c.speak() #but this is saying Meow becuase its a Class Cat object
d = Dog('Jill', 25)
d.show()
d.speak() #and this is saying Bark because its a Dog class object

#we can create an additional class which inheritate Pet but without the function speak
#so if we call method .speak it will take it from the upper level
class Fish(Pet):
    pass

f = Fish('Bubbles', 10)
f.speak()

#we can a new class object with an additional attribute color but with the same method speak
class Bird(Pet):
    def __init__(self, name, age, color):
        #self.name = name #Esto se sustitutye por el super().__init__(name, age)
        #self.age = age   #Esto se sustitutye por el super().__init__(name, age)
        super().__init__(name, age)  #nota que el name y age no llevan self
        self.color = color

    def speak(self):
        print('piopio')
    def show(self):
        print(f'i am {self.name},  i am {self.age} years old and i am {self.color}' )


b = Bird('Pinkie', 18, 'Pink')

b.speak()
b.show()


##############################################################################
print('######################################################################3')
#Statics and class methods and class atributes

# we will show now the Class atributes

class Person_test1:
    number_of_people_test = 0  #THIS IS A CLASS ATRIBUTE this will not change for everyperson, like name
    #this is why it doenst have self.... becuase its the same for every Person

    def __init__(self, name):
        self.name = name

per1 = Person_test1('Tim')
per2 = Person_test1('Jill')
print(per1.number_of_people_test)
print(Person_test1.number_of_people_test) #as it is an atribute from the class i dont have to necesarily call the specific object, i can call the class

#and i can change the Class atribute from the class:
Person_test1.number_of_people_test = 9
print(per1.number_of_people_test)
print(per2.number_of_people_test)
Person_test1.number_of_people_test = 7
print(per1.number_of_people_test)
print(per2.number_of_people_test)
print(Person_test1.number_of_people_test)

## what can we do with number of people? We will define a new class similar

class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        # THIS IS WITHOUT THE CLASS METHOD Person.number_of_people += 1 #this will increase +1 every new people object we will create
        Person.add_person() #this is for ##CLASS METHOD
    ##CLASS METHOD########
    @classmethod #this is a decorator it mus be placed over the class method below number of people (cls)
    def number_of_plp(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person('Timmy')
#print(Person.number_of_people) #We add one person it should show 1  # THIS IS WIHTOU THE CLASS METHOD
p2 = Person('Jilly')
#print(Person.number_of_people) # we added a second person it should show 2 #THIS IS WITHOUT THE CLASS METHODS
#with the class method implemented we can add the people uisng
print(Person.number_of_plp())



####Static methods###############

class Math:

    @staticmethod
    def add5(x): #this is not gonna access anything so this is why we dont put cls or self
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def pr():
        print('run')

print(Math.add5(6))
print(Math.add10(8))
Math.pr()