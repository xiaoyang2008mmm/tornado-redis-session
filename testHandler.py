#coding=utf-8

from base import BaseHandler


class HelloHandler(BaseHandler):
    def get(self):
        l = []
        #print self.session
	print self.session['admin']
        l.append(self.session['user'])
        self.render("./templates/hello.html", page_object=l)


class loginHandler(BaseHandler):
    def get(self):
	for  i in self.locale:
	    print  i
	for i in dir(self):
	    print i
        user = self.get_argument('user', '')
        passwd = self.get_argument('passwd', '')
	if user =="admin":
	    if  passwd=="admin":
                 self.session[user] = "这个是admin的session的"
                 self.session.save()
                 print self.session
                 self.write(user)
                 self.finish()
	    else:
                 self.write('密码不对!!!')
		
	else:
            self.write('密码不对!!!')
	   







####退出登录的时候只要把该用户的对应的在redis 里存的session
session[SESSION_USER] = None
session.save()

参考
https://www.androiddev.net/%E4%BD%BF%E7%94%A8redis%E6%90%AD%E5%BB%BAtornado%E7%9A%84session/
