from base64 import main
from pyrebase import initialize_app

class FireAuth:
    config = {
        "apiKey": "",
        "authDomain": "",
        "databaseURL": "",
        "storageBucket": ""
    }
    firebase = initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()
    # sign user up
    def signUp(self, username, name , lname, email, password):
        user = self.auth.create_user_with_email_and_password(email, password)
        results = self.db.child("users").push({"username":username, "name":name,
                                               "lname":lname}, user['idToken'])
        # email verification
        self.auth.send_email_verification(user['idToken'])
        return results
    # Log the user in
    def login(self, email, password):
        user = self.auth.sign_in_with_email_and_password(email, password)
        # Account information
        return self.auth.get_account_info(user['idToken'])
    # rest password
    resetPasswd = lambda self, email: self.auth.send_password_reset_email(email)



if __name__=="__main__":
    fire_auth = FireAuth()
    # register account
    signUp = fire_auth.signUp(username='usklsn4', name='ismail',
                              lname='salmi', email='ismail@gmail.com',
                              password=00000000)
    print(signUp, 'Confirm your account')
    '''
    # login
    logIn = fire_auth.login(email='ismail@gmail.com', password=00000000)
    for i in logIn:
       print(json.dumps(logIn[i], indent=1, sort_keys=True))
    '''
    '''
    # reset password
    resetPass = fire_auth.resetPasswd('ismail@gmail.com')
    print(resetPass)
    '''
    main()
