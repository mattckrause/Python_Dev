import json
import io
import base64

messages = []
count = 0
#parsing all the message objects listed in the file
for message in open(r'C:\github\Python_Dev\python_Functions\bc4e3318-b96f-45ac-aee6-b0dfae9a1744_0_0'):
    messages.append(json.loads(message))
    count +=1

#processing each message
print("Processing {} messages...".format(count))
for i in messages:
    #does it have an attachment?
    if i['hasAttachments'] == True:
        for a in i['attachments']:
            #download attachments
            fileName = (a['name'])
            content = base64.b64decode(a['contentBytes'])
            outFile = 'C:/Temp/%s' % (fileName)
            print(outFile)
            byteData = io.BytesIO()
            byteData.write(content)
            with open(outFile, "wb") as binary_file:
                binary_file.write(byteData.getbuffer())
