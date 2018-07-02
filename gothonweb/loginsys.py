def checkpass(login, pword):

    logintext = open("~/projects/gothonwebproject/gothonweb/users.txt")
    logins = {}
    for line in logintext.readlines():
        login, pword = line.split(' ')
        logins[login] = pword.strip()
    close(logintext)

    try:
        if logins[login] == pword:
            return True
    except KeyError:
        return False
    return False
