def checkpass(login, pword):
    logintext = open("gothonweb/users.txt")
    logins = {}
    for line in logintext.readlines():
        dong, pord = line.split(' ')
        logins[dong] = pord.strip()
    #print logins
    logintext.close()
    try:
        if logins[login] == pword:
            return True
    except KeyError:
        return False
    return False
