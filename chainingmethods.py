class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email) 
        print(self.age) 
        print(self.gold_card_points)
        print(self.is_rewards_member)
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        # print(self.gold_card_points)
        # print(self.is_rewards_member)
        if(self.is_rewards_member==True):
            print("User already a member")
            return False
        else: 
            return True
    def spend_points(self,amount):
        self.amount = amount
        self.gold_card_points = self.gold_card_points - amount
        # print(amount)
        # print(self.gold_card_points)
        if(self.gold_card_points<=amount):
            print("Not enough points")

user_1 = User('Eric', 'Trudell', 'ettrudell17@gmail.com', 30)
user_2 = User('Odin', 'Trudell', 'throwmeabone@gmail.com', 5)
user_3 = User('Jack', 'Hannah', 'iloveanimals@gmail.com', 40)
user_1.enroll()
user_1.spend_points(50)
user_2.enroll()
user_2.spend_points(80)
user_1.display_info()
user_2.display_info()
user_3.display_info()
user_1.enroll()
user_3.spend_points(40)