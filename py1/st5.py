from http import cookies
import os, json
import datetimem, random, hashlib

class CookieSession:
    SESSION_ID = "CookieSessionId"
    SESSION_DIR = os.path.dirname(
        os.path.abspath(__file__)
    ) + "/SESSION"

    def __init__(self):
        if not os.path.exists(self.SESSION_DIR):
            os.mkdir(self.SESSION_DIR)

        rc = os.environ.get("HTTP_COOKIE", "")
        self.cookie = cookies.SimpleCookie(rc)
        if self.SESSION_ID in self.cookie:
            self.sid = self.cookie[self.SESSION_ID].value
        else:
            self.sid = self.gen_sid()
        
        self.modified = False
        self.values = {}
        path = self.SESSION_DIR + "/" + self.sid
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                a_json = f.read()
                self.values = json.loads(a_json)


    def gen_sid(self):
        token = ":#sa$2jAiN"
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        rnd = random.randint(0, 100000)
        key = (token + now + str(rnd)).encode('utf-8')
        sid = hashlib.sha256(key).hexdigest()
        return sid

    def output(self):
        self.cookie[self.SESSION_ID] = self.sid
        self.save_data()
        return self.cookie.output()

    def save_data(self):
        if not self.modified: return
        path = self.SESSION_DIR + "/" + self.sid
        a_json = json.dumps(self.values)
        with open(path, "w", encoding="utf-8") as f:
            f.write(a_json)
    
    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.modified = True
        self.values[key] = value

    def __contains__(self, key):
        return key in self.values

    def clear(self):
        self.values = {}

if __name__ == "__main__":
    ck = CookieSession()
    counter = 1
    if "counter" in ck:
        counter = int(ck["counter"]) + 1
    ck["counter"] = counter
    print("Content-Type: text/html")
    print(ck.output())
    print("")
    print("counter=", counter)

# --------

import os, cgi, cgitb, html
import cksession
import datetime

class SecBoard:
    
    USERS = { "taro": "aaa", "jiro": "bbb" }
    FILE_MSG = "sec-msg.bin"

    def __init__(self):
        self.form = cgi.FieldStorage()
        self.session = cksession.CookieSession()
        self.check_mode()
    
    def check_mode(self):
        mode = self.form.getValue("mode", "login")
        if mode == "login"      : self.mode_login()
        elif mode == "trylogin" : self.mode_trylogin()
        elif mode == "logout"   : self.mode_logout()
        elif mode == "sec"      : self.mode_sec()
        elif mode == "secedit"  : self.mode_secedit()
        else: self.mode_login()
    
    def print_html(self, title, html, headers = []):
        print("Content-Type: text/html; charset=utf-8")
        for hd in headers: print(hd)
        print("")
        print("""
        
        """.format(title, html))
    
    def show_error(self, msg):
        self.print_html("error", """
        
        """.format(msg))

    def mode_login(self):
        self.print_html("login", """
        
        """)
    
    def mode_trylogin(self):
        user = self.form.getvalue("user", "")
        pw   = self.form.getvalue("pw", "")

        if not (user in self.USERS):
            self.show_error("no user")
            return
        if self.USERS[user] != pw:
            self.show_error("password not eq")
            return
        
        now = datetime.datetime.now()
        self.session["login"] = now.timestamp()
        headers = [self.session.output()]
        self.print_html("success login", """
        
        """, headers)
    
    def mode_logout(self):
        self.session["login"] = 0
        self.print_html("logout", """
        
        """, [self.session.output()])

    def is_login(self):
        if "login" in self.session:
            if self.session["login"] > 0:
                return True
        return False

    def mode_sec(self):
        if not self.is_login():
            self.show_error("need login")
            return
        
        msg = "write message"
        if os.path.exists(self.FILE_MSG):
            with open(self.FILE_MSG, "r", encoding="utf-8") as f:
                msg = f.read()
        
        msg = html.escape(msg)
        self.print_html("message", """
        
        """.format(msg))

    def mode_secedit(self):
        if not self.is_login():
            self.show_error("need login", "")
            return

        msg = self.form.getvalue("msg", "")
        with open(self.FILE_MSG, "w", encoding="utf-8") as f:
            f.write(msg)
        
        self.print_html("saved", """
        
        """)

if __name__ == "__main__":
    cgitb.enable()
    app = SecBoard()
