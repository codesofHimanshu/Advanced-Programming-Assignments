class Address:
    def __init__(self, street, city, zipCode):
        self.street = street
        self.city = city
        self.zipCode = zipCode

    def display(self):
        return f"{self.street}, {self.city} - {self.zipCode}"


class Student:
    def __init__(self, name, age, address, courses=None):
        self.name = name
        self._age = None  # protected attribute
        self.age = age    # setter validation
        self.address = address  # composition (HAS-A)
        self.courses = courses if courses else []

    # Property for age (validation)
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0 or value > 120:
            raise ValueError("Age must be between 1 and 120")
        self._age = value

    # Add course (mutable list behavior)
    def add_course(self, course):
        self.courses.append(course)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address.display()}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'No courses'}")


class ScholarshipStudent(Student):
    def __init__(self, name, age, address, scholarshipAmount, courses=None):
        super().__init__(name, age, address, courses)
        self.scholarshipAmount = scholarshipAmount

    # Override display method
    def display(self):
        super().display()  # call parent display
        print(f"Scholarship Amount: {self.scholarshipAmount}")


# -------------------------
# Testing the implementation
# -------------------------

# Create Address object (Composition)
addr = Address("ABC Road", "Guwahati", "781001")

# Create Student
s1 = Student("Himanshu", 20, addr)
s1.add_course("Math")
s1.add_course("Python")

# Mutable behavior demonstration
courses_ref = s1.courses
courses_ref.append("Data Structures")  # persists

print("----- Student Details -----")
s1.display()

# Create ScholarshipStudent
s2 = ScholarshipStudent("Rahul", 22, addr, 50000)
s2.add_course("AI")

print("\n----- Scholarship Student Details -----")
s2.display()