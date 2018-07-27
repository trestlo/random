import win32com.client


outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) 

messages = inbox.Items
message = messages.GetLast()
body_content = message.body
f = open('textfile.txt', 'w')
f.write(body_content)