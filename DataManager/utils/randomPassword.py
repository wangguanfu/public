import random
import string

def random_password():
    src = string.ascii_letters + string.digits
    list_passwds = []
    for i in range(int(1)):
        list_passwd_all = random.sample(src, 10) #从字母和数字中随机取5位
        list_passwd_all.extend(random.sample(string.digits, 1))  #让密码中一定包含数字
        list_passwd_all.extend(random.sample(string.ascii_lowercase, 1)) #让密码中一定包含小写字母
        list_passwd_all.extend(random.sample(string.ascii_uppercase, 1)) #让密码中一定包含大写字母
        random.shuffle(list_passwd_all) #打乱列表顺序
        str_passwd = ''.join(list_passwd_all) #将列表转化为字符串
        if str_passwd not in list_passwds: #判断是否生成重复密码
            list_passwds.append(str_passwd)
    return str(list_passwds[0])
