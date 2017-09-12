#  File: Friends.py
#  Description: Use linked lists to implement the "friend" functionality of a
#               Facebook-like application
#  Student's Name:  Amy Fang
#  Student's UT EID: af27947
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 07/11/17
#  Date Last Modified: 07/16/17

########
# User #
########
class User:

   def __init__(self, name):
      self.name = name
      self.friends = UnorderedList()
      self.next = None            # always do this â€“ saves a lot

   def getName (self):
      return self.name            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newName):
      self.name = newName         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER
      
   def __str__(self):
      return str(self.name)

   def addFriend(self, other):
      self.friends.add(other)
      other.friends.add(self)

   def unfriend(self, other):
      self.friends.remove(other)
      other.friends.remove(self)

   def listFriends(self):
      listOfFriends = "[ " + self.friends.returnList() + "]"
      return listOfFriends
      
   def searchFriend(self, person):
      return self.friends.search(person.name)

##################
# Unordered List #
################## 
class UnorderedList:

   def __init__(self):
      self.head = None

   def isEmpty (self):
      return self.head == None

   def add (self,item):
      # add a new Node to the beginning of an existing list
      temp = User(item)
      temp.setNext(self.head)
      self.head = temp

   def length (self):
      current = self.head
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

   def search (self, name):
      current = self.head
      found = False

      while current != None and not found:
         if str(current.getName()) == name:
            found = True
         else:
            current = current.getNext()
      return found

   def remove (self,item):
      current = self.head
      previous = None
      found = False

      while not found:
         if current.getName() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext())

   # Returns the node of a user with name
   def searchUser(self, name): # assuming user is in the list
      current = self.head

      while current != None:
         if current.getName() == name:
            return current
         else:
            current = current.getNext()

   # Returns a list of names in list
   def returnList(self):
      allNames = ""

      current = self.head

      while current != None:
         name = str(current.getName())
         allNames += name + " "
         current = current.getNext()

      return allNames

################
# Main program #
################
def main():

    # Create linked list of User objects
    allUsers = UnorderedList()

    
    infile = open("FriendData.txt", "r")  # Open file

    for line in infile: # Go through each line
        line = line.strip()
        lst = line.split(" ")

        print("-->", line)
      
        command = lst[0]
        
        if command == "Person":  # Create a user
            name = lst[1]

            if allUsers.search(name): # if the user has already been created
               print("A person with name", name, "already exists.")
            else:
               allUsers.add(name)
               print(name, "now has an account.")
            
        elif command == "Friend": # Add a friend
            user1_name = lst[1]
            user2_name = lst[2]

            # If either users haven't been created
            if not allUsers.search(user1_name) or not allUsers.search(user2_name):
               if not allUsers.search(user1_name):
                  print("A person with name", user1_name, "does not currently exist.")
               if not allUsers.search(user2_name):
                  print("A person with name", user2_name, "does not currently exist.")

            # If both users have been created
            else:
               user1 = allUsers.searchUser(user1_name)
               user2 = allUsers.searchUser(user2_name)
               
               if user1_name == user2_name: # If same person
                  print("A person cannot friend him/herself.")
               elif user1.searchFriend(user2): # If they're already friends
                  print(user1_name, "and", user2_name, "are already friends.")
               else: # If not friends
                  user1.addFriend(user2)
                  print(user1_name, "and", user2_name, "are now friends.")
        
        elif command == "Unfriend": # Delete a friend
            user1_name = lst[1]
            user2_name = lst[2]

            # If either users haven't been created
            if not allUsers.search(user1_name) or not allUsers.search(user2_name):
               if not allUsers.search(user1_name):
                  print("A person with name", user1_name, "does not currently exist.")
               if not allUsers.search(user2_name):
                  print("A person with name", user2_name, "does not currently exist.")

            # If both users have been created
            else:
               user1 = allUsers.searchUser(user1_name)
               user2 = allUsers.searchUser(user2_name)

               if user1_name == user2_name: # If same person
                  print("A person cannot unfriend him/herself.")
               elif not user1.searchFriend(user2): # If they're already not friends
                  print(user1_name, "and", user2_name, "aren't friends so you can't unfriend them.")
               else: # If friends
                  user1.unfriend(user2)
                  print(user1_name, "and", user2_name, "are no longer friends.")
                  
        elif command == "Query": # Query friend status
            user1_name = lst[1]
            user2_name = lst[2]

            if user1_name == user2_name: # If same person
               print("A person cannot query him/herself")

            # If either users haven't been created
            elif not allUsers.search(user1_name) or not allUsers.search(user2_name):
               if not allUsers.search(user1_name):
                  print("A person with name", user1_name, "does not currently exist.")
               if not allUsers.search(user2_name):
                  print("A person with name", user2_name, "does not currently exist.")

            # If both users have been created
            else:
               user1 = allUsers.searchUser(user1_name)
               user2 = allUsers.searchUser(user2_name)

               if user1.searchFriend(user2):
                  print(user1_name, "and", user2_name, "are friends.")
               else: # if not friends
                  print(user1_name, "and", user2_name, "are not friends.")
               
        
        elif command == "List": # List all friends
            name = lst[1]

            if allUsers.search(name): # If user is already made
               user = allUsers.searchUser(name)
               listOfFriends = user.listFriends()

               if listOfFriends == "[ ]": # If no friends in list
                  print(user, "has no friends.")
               else: # If there is at least one friend in list
                  print(listOfFriends)
               
            else: # If user has not been created
               print("A person with name", user1_name, "does not currently exist.")

        else: # Exit command
            print("Exiting...")
            break

        print()


    infile.close()

main()






    
