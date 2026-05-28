class Notification:
    def send(self):
        print("Sending Notification...")

class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")

class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")

def dispatch_notification(notifications):
    print("Dispatching Notifications:")

    for notification in notifications:
        notification.send()

email=EmailNotification()
sms=SMSNotification()
push=PushNotification()

all_notifications=[email,sms,push]

dispatch_notification(all_notifications)

