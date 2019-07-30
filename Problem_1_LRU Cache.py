
# coding: utf-8

# In[1]:


#Problem 1: LRU Cache 
#Least Recently Used Cache
import collections

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.size = capacity
        self.cache = collections.OrderedDict()
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache: 
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)
#Test Case1
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 'Not a number');
our_cache.set(None, 5);
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(4))       # return Not a number
print(our_cache.get(5))       # return -1
print(our_cache.get(6))       # return -1

# Test case2
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1)) #return 10
print(our_cache.get(2)) #rerurn 2

# Test case3
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
print(our_cache.get(1)) # return 'Can't perform operations on 0 capacity cache -----need help！！！！！

