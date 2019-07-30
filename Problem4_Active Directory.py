
# coding: utf-8

# In[4]:


#Problem 4: Active Directory 
#Write a function that provides an efficient look up of whether the user is in a group.
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
def is_user_in_group(user, group):
    if user in group.get_users():
        return True
    else:
        for group in group.get_groups():
            return is_user_in_group(user, group)
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Case
answer = is_user_in_group("sub_child_user", parent)
print(answer)
answer = is_user_in_group("a_child", parent)
print(answer)
answer = is_user_in_group("child_user", parent)
print(answer)
        

