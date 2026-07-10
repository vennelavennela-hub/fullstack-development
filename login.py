def login(func):
    def wrapper():
        print("checking login")
        func()
    return wrapper 
@login
def dashboard():
    print("dashboard page")
dashboard()