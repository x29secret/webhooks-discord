import requests
import json

url = " link webhook "

# Set your webhook parameters
data = {
    "username": "Smoslock Notify",#แก้ไขได้
    "avatar_url": "https://cdn.discordapp.com/attachments/1095770891398434846/1098555541640458270/240398018_991057598294903_8825235666542450670_n.png",#แก้ไขได้
    "content": "**สนใจซื้อไอดี** [**Click Here**](https://smoslockshop.com/)", #แก้ไขได้
    "embeds": [
        {
            "title": "",#แก้ไขได้
            "description": " **ตอนนี้มีไอดีขายแล้วนะครับ** 😘 @everyone",#แก้ไขได้
            "color": 16777215,
            "image": {
                "url": "https://cdn.discordapp.com/attachments/1095770891398434846/1098554296586481664/image.png" #แก้ไขได้

                },
            "footer": {
                "text": "Bot By phakaphop", #แก้ไขได้
                "icon_url": "https://cdn.discordapp.com/attachments/1095770891398434846/1098555541640458270/240398018_991057598294903_8825235666542450670_n.png"#แก้ไขได้
            }
        }
    ]
}

# Send the webhook request
response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})

# Print the response status code
print(response.status_code)
