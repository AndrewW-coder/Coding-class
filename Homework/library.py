class library(object):
    def __init__(self, name, author, review):
        self.name = name
        self.author = author
        self.review = review
    def about(self):
        print('This book is', self.name, '.It is written by', self.author, '. It has a review of', self.review, '.')
book1 = library('Bryan is awesome', 'Bryan', '-100 stars')
book1.about()