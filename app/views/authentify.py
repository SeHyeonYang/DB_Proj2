def login_required(user):
    print(user)
    if user.is_anonymous():
        return False
    return True
