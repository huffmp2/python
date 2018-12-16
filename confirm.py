unconfirmed = ['alice', 'brian', 'candace']
confirmed = []
while unconfirmed:
    current = unconfirmed.pop()
    print ("Verifying user: " + current.title())
    confirmed.append(current)
print ("\nThe following users have been confirmed:")
for confirm in confirmed:
    print(confirm.title())