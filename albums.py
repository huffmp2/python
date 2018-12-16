def makealbum(artistname, albumtitle, tracks=''):
    """Return a dictionary of information about an album."""
    album = {'artist': artistname, 'album': albumtitle}
    if tracks:
        album['tracks'] = tracks
    return album
albums = makealbum('Michael Jackson', 'Thriller')
print (albums)
albums = makealbum('The Fray', 'How to Save a Life')
print (albums)
albums = makealbum('Beatles', 'Sgt. Peppers Lonely Hearts Club Band', tracks = '15')
print (albums)