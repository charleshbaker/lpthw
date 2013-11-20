


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

row = Song(["Row, row, row your boat",
            "Merrily down the stream"])

row.sing_me_a_song()

lyric = "Call me big poppa!"

biggie = Song(lyric)

biggie.sing_me_a_song()

jordan = ["Jordan river is chilly and cold",
          "It chills the body",
          "But not the soul"]

spiritual = Song(jordan)

spiritual.sing_me_a_song()
