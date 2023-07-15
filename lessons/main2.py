class Comment:
    def __init__(self, text, initial_votes_qty=0):
        self.text = text
        self.votes_qty = initial_votes_qty

    def upvote(self, up):
        self.votes_qty += up

    def reset_votes_qty(self):
        self.votes_qty = 0


my_comment = Comment("My comment", 10)
print(my_comment.votes_qty)
my_comment.upvote(10)
my_comment.upvote(20)
print(my_comment.votes_qty)
my_comment.reset_votes_qty()
print(my_comment.votes_qty)
