class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
      
        self.description = description
        
        self.creator_name = creator_name
        
        self.location = location
    
        self.likes = 0
        
        self.comments = []

    def display_title(self):
        print("The title of the reel is:", self.title)

    def display_description(self):
        print("The description of the reel is:", self.description)


    def display_creator(self):
        print("The creator of the reel is:", self.creator_name)


    def display_location(self):
        print("The location of the reel is:", self.location)

    def display_likes(self):
        print("The likes of the reel is:", self.likes)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def display_comments(self):
        print("Comments on the reel:")
        for comment in self.comments:
            print("-", comment)

reel1 = Instagram(
    "dancing",
    "dancing with friends",
    "Rahul",
    "Bangalore"
)

reel1.liked()
reel1.liked()
reel1.disliked()
reel1.add_comment("Nice dance")
reel1.add_comment("Awesome moves")

reel2 = Instagram(
    "finance minister conference",
    "finance minister conference with friends",
    "Anita",
    "Delhi"
)

reel2.liked()
reel2.add_comment("Very informative")

reel1.display_likes()
reel1.display_comments()

reel2.display_likes()
reel2.display_comments()

print(id(reel1))
print(id(reel2))