while True:
    try:
        s = input()
    except EOFError:
        break

    if s.count('@') != 1:
        print("NO");
        continue

    # if (s[0]=='@' or s[-1]=='@' or s[0]=='.' or s[-1]=='.'):
    if (s[0] in {'@', '.'} or s[-1] in {'@', '.'}):
        print("NO");
        continue

    if (s.find("@.") != -1 or s.find(".@") != -1):
        print("NO");
        continue

    p = s.find("@");
    q = s.find(".", p + 1);

    '''
    if (q==-1):
        print("NO")
    else:
        print("YES")
    '''
    print('NO' if q == -1 else 'YES')
