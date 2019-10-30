# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:18:45 2018

@author: furrukh
"""

class intdict(object):
    def __init__(self, number):
        self.bucket = []
        self.number_of_buckets = number
        
        for i in range(self.number_of_buckets):
            self.bucket.append([])
            
    def add_entry(self, key, value):
        hashbucket = self.bucket[key%self.number_of_buckets]
        
        for i in range(len(hashbucket)):
            if hashbucket[i][0] == key:
                hashbucket[i] = (key, value)
                return
        hashbucket.append((key, value))
        
        
        
    def getvalue(self, key):
        hashbucket = self.bucket[key%self.number_of_buckets]
        
        for e in hashbucket:
            if e[0] == key:
                return e[1]
        
        return "No Such Key"
        
        
    def __str__(self):
        result = "{"
        for each in self.bucket:
            for every in each:
                result = result + str(every[0]) + ":" + str(every[1]) + ","
                
        return result[:-1] + "}"
            