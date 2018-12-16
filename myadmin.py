import user

admin1= user.Admin('mary', 'adams')
admin1.privelages.powers= ['can add post', 'can delete post', 'can ban user']
admin1.privelages.showprivelages()