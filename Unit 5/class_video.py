class Video:
    def __init__(self, title, url, num_comments):
        self.title = title
        self.url = url
        self.num_comments = num_comments
        
    def is_trending(self):
        if(self.num_comments > 100):
            print(self.title + " is trending!")
        else:
            print(self.title + " is not trending.")


cat = Video("my cat", "example.com", 175)

print(cat.title)
cat.is_trending()

