class SongData:
  def __init__(self, path, name, artist, album, length):
    self.path = path
    self.name = name
    self.artist = artist
    self.album = album
    self.length = length
    
  def __str__(self):
    return self.name + " - " + self.artist