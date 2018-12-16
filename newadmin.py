from user import Users
from privelage import Privelages
from privelage import Admin

admin1= Admin('mary', 'adams')
admin1.privelages.powers= ['can add post', 'can delete post', 'can ban user']
admin1.privelages.showprivelages()