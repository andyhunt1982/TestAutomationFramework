import win32com.client


class CreateEmail:
    def __init__(self, to, subject, body, attachments=None):
        self.to = to
        self.subject = subject
        self.body = body
        self.attachments = []
        self.email_client = win32com.client.Dispatch("Outlook.Application")
        self.email_object = self.email_client.CreateItem(0)
        self.email_object.To = self.to
        self.email_object.CC = "andy.hunt1982@gmail.com"
        self.email_object.Subject = self.subject
        self.email_object.Body = self.body
        if attachments:
            for attachment in attachments:
                self.email_object.Attachments.Add(attachment)
        self.email_object.Display()
        self.email_client.Send()