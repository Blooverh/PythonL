def build_profile(first, last, **userInfo):
    userInfo['first_name']= first
    userInfo['last_name']= last
    return userInfo

user_profile=build_profile('Albert','Einstein', location='Princeton', field='Physics')
print(user_profile)