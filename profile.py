def buildprofile(first, last, **userinfo):
    """Build a dictionary containing everything we know about a user."""
    profile={}
    profile['firstname'] = first
    profile['lastname'] = last
    for key, value in userinfo.items():
        profile[key]= value
    return profile
userprofile= buildprofile('pam', 'huffman', status='student', age='33', gender='female')
print(userprofile)