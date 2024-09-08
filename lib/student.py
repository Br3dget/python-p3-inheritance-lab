#!/usr/bin/env python

from user import User

class Student(User):
     def __init__(self,first_name,second_name):
            super().__init__(first_name, second_name)
            self.knowledge = []
    
     def learn(self, string):
         self.knowledge.append(string)
        