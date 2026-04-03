class InstagramAccount:
    def __init__(self, account_name, password):
    
        self.account_name = account_name
 
        self._private_reels = []
        
        self.__archived_reels = []
        
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"Private reel '{reel_name}' added.")

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"Archived reel '{reel_name}' added.")

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied! Incorrect password"

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Incorrect old password! Password not updated.")

account = InstagramAccount("dheemanth_official", "1234")

account.add_private_reel("Friends Party Reel")
account.add_private_reel("Vacation Reel")

account.add_archived_reel("Old College Reel")
account.add_archived_reel("Throwback Reel")

account.display_private_reels(is_follower=True)
account.display_private_reels(is_follower=False)

account.display_archived_reels("1234")
account.display_archived_reels("wrongpass")

print(account.get_archived_reels("1234"))

account.set_password("1234", "newpass")