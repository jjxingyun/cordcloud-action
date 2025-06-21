from app.action import Action

email = 'contact@yanglibin.info'
passwd = 'xxxxxxxx'
host = 'cordcloud.one'
action = Action(email, passwd, host=host)
action.run()
