import requests
while True:

    msg = input("Please Insert webhook Spam Message: ")
    webhook = input("Please Insert webhook URL: ")
    def spam(msg, webhook):
        for i in range(30):
            try:   
                data = requests.post(webhook, json={'content': msg})
                if data.status_code == 204:           
                    print(f"Sent MSG {msg}")
            except:
                print("Bad Webhook :" + webhook)
                
                exit()
    counts = 0.5
    while counts == 0.5:
        spam(msg, webhook)