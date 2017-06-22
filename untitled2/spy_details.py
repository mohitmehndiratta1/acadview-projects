from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('mohit', 'Mr.', 24, 4.7)

buddy_one = Spy('richard', 'Mr.', 4.9, 27)
buddy_two = Spy('jared', 'Ms.', 4.39, 21)
buddy_three = Spy('No', 'Dr.', 4.95, 37)


buddy = [buddy_one, buddy_two, buddy_three]
