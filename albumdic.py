def makealbum(artistname, albumtitle, tracks=''):
    """Return a dictionary of information about an album."""
    album = {'artist': artistname, 'album': albumtitle}
    if tracks:
        album['tracks'] = tracks
    return album
while True:
    print ("What is the name of the artist?")
    print ("(enter 'q' at any time to quit)")
    aname = input("Artist's Name: ")
    if aname == 'q':
        break
    print ("What is the name of the album?")
    print ("(enter 'q' at any time to quit)")
    alname = input("Album's Name: ")
    if alname == 'q':
        break
    print ("How many tracks are in the album?")
    print ("(enter 'q' at any time to quit)")
    track = input("Number of tracks: ")
    if track == 'q':
        break
    albumdic= makealbum(aname, alname, track)
    print (albumdic)
