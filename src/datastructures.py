
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members =[
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": "33 Years old",
                "lucky_numbers": "7, 13, 22"
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": "35 Years old",
                "lucky_numbers": "10, 14, 3"
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": "5 Years old",
                "lucky_numbers": "1"
            },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member: dict)->None:
        
        self._members.append(member)
        return True

    def delete_member(self, id:int)->dict:
        
        for position in range(len(self._members)):
            if self._members[position]["id"]==id:
                self._members.pop(position)
                return True

                

    def get_member(self, id:int)->dict:
        
        for m in self._members:
            if m["id"]==int(id):
                return m

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
