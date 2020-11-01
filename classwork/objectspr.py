class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    def __repr__(self):
        return 'Account:' , self.holder

class checkingAccount(Account):
    withdraw_charge = 1
    interest_rate = 0.01
    def withdraw(self, balance):
        return Account.withdraw(self, balance + self.withdraw_charge)

class Student:
    students = 0 # this is a class attribute

    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)
    
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1
    
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):

        self.clients = {}
    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        
        self.clients[email.recipient_name].inbox.append(email)
    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name] = client
class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        self.server.send(self.server, Email(msg, self.name, recipient_name))
    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)


class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)
class B(A):
    n = 5
    def f(self):
        return 4

"""
What would python display

>>> x, y = A(), B()
>>> x.f()
2
>>> B.f()
Error
>>> x.g(x, 1)
4
>>> y.g(x, 2)
8
"""

"""
getattr(object, attribute)
hasattr(object, attribute)
"""

class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return f'Ratio({self.numer}, {self.denom})'

    def __str__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        if isinstance(other, int):
            n = self.denom*other + self.numer
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer*other.denom + self.denom*other.numer
            d = self.denom*other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n//g, d//g)
    def __float__(self):
        return self.numer/self.denom

    __radd__ = __add__



def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n

class Kangaroo:
    def __init__(self):
        self.pouch_contents = []
    
    def put_in_pouch(self, st):
        if st in self.pouch_contents:
            print("Object already in pouch")
            print(self)
        else:
            self.pouch_contents.append(st)
    
    def __str__(self):
        if len(self.pouch_contents) == 0:
            return "The kangaroo's pouch is empty."
        else:
            return f"The kangaroo's pouch contains: {self.pouch_contents}"
     