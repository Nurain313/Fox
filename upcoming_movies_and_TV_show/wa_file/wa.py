from heyoo import WhatsApp

access_token = "EAANdhfNw2mUBANyEhjJ36yNohCFxoKia0p0ZCwjwdLNagOctLVvTXPeHalKdnLfrmns5UZBRkYYfskfGMy3JKcss45q6IYCZBwlVSg9FlbeWj0Ybjc5rXFGg3oReogaTrhKDJYdSqdxkJ4ZCSvvQL3OCUa2SzuPBTi0ZBFBLbVcmVOcdBWp7uZB42vCDPx3HPsMmZAyC8aIsJDQkZBQVaKNPXSbSZCdoueVIZD "
phone_number_id= "108662742221303"
#WhatsApp_Business_Account_ID = "114060805011332"
Group_id = "+254711220439"
messenger = WhatsApp(access_token, phone_number_id)
# For sending a Text messages
messenger.send_message('Hello I am WhatsApp Cloud API', Group_id)
# For sending an Image
messenger.send_image(
        image="https://www.themoviedb.org/t/p/original/c0Zv7gNTH8LoRnHANhAHGWhGvJC.jpg",
        recipient_id=Group_id,
    )