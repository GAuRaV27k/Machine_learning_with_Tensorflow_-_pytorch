class book:
    title = "Last of Us"
    author = "Gaurav Kaushik"
    lst_review = ["nice","bad" ,"worst it ", "excellent"]

    def new(self,new_review):
        (self.lst_review).append(new_review)
        
    def count(self):
        counts = len(self.lst_review)
        print(counts)
    def display(self):
        print(self.lst_review)

my = book()
my.new("very good")
my.count()
my.display()
