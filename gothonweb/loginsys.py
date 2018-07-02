def checkpass(login, pword):
    login = login.strip()
    pword = pword.strip()
    logintext = open("gothonweb/users.txt")
    logins = {}
    for line in logintext.readlines():
        dong, pword = line.split(' ')
        logins[dong] = pword.strip()
    #print logins
    logintext.close()
    try:
        if logins[login] == pword:
            return True
    except KeyError:
        return False
    return False
