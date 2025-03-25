Users = {}
Posts = {}

class chatbook:
    def __init__(self):
        self.Username = ''
        self.LoggedIn = False
        self.Password = ''
        self.PostIdx = 0
        print(1)
        self.menu()


    def Register(self):
        self.Username = input("Enter Your Username")
        self.Password = input("Enter Your Password")
        if self.Username in Users:
            print("Username already exists")
            self.menu()
        else:
            Users[self.Username] = self.Password
            print("Registration Successful")
            self.LoggedIn = True
            print(self.LoggedIn)
            print(Users)
            self.menu()

    def Login(self):
        self.Username = input("Enter Your Username")
        self.Password = input("Enter Your Password")
        if self.Username in Users and self.Password == Users[self.Username]:
            print("Login Successful")
            self.LoggedIn = True
            self.menu()
        else:
            print("Invalid Credentials")
            self.menu()
    def SendPost(self):
        if self.LoggedIn:
            self.post[self.PostIdx] = input("Enter Your Post")
            self.PostIdx += 1
            print(self.post)
            self.menu()
        else:
            print("Login First")
            self.menu()
    def menu(self):
        user_input = input('''Enter Your Choice
        1. Login
        2. Register
        3. Send a Post
        4. Exit
        ''')
         
        if user_input == '1':
            self.Login()
        elif user_input == '2':
            self.Register()
        elif user_input == '3':
            self.SendPost()
        elif user_input == '4':
            exit()
        else:
            print("Invalid Input")
            self.menu()

c1 = chatbook()