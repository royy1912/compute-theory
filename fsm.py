from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        
    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "豚骨"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "雞白湯"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "二郎系"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "覺丸拉麵\nhttps://www.google.com.tw/maps/place/%E8%A6%BA%E4%B8%B8%E6%8B%89%E9%BA%B5/@22.9960078,120.2275515,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76c075aa3a33:0x6399402cf32a429c!8m2!3d22.9959967!4d120.2297791?hl=zh-TW\n一拉麵\nhttps://www.google.com.tw/maps/place/%E3%84%A7%E6%8B%89%E9%9D%A2-%E8%B1%9A%E9%AA%A8%E5%B0%88%E8%B3%A3/@23.0086666,120.218289,17z/data=!3m1!4b1!4m5!3m4!1s0x346e77989d1e8655:0x81024a287238f3d0!8m2!3d23.0086639!4d120.2205063?hl=zh-TW\n寶來軒\nhttps://www.google.com.tw/maps/place/%E5%AF%B6%E4%BE%86%E8%BB%92/@23.0020166,120.2037229,17z/data=!3m1!4b1!4m5!3m4!1s0x346e765fea7e7689:0xb6fff831dde12cb!8m2!3d23.002018!4d120.2059127?hl=zh-TW")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "白露拉麵\nhttps://www.google.com.tw/maps/place/%E7%99%BD%E9%9C%B2%E6%8B%89%E9%BA%B5+bailu+ramen/@22.9898981,120.2060597,17z/data=!3m1!4b1!4m5!3m4!1s0x346e77bab41970bd:0xd7c99b74c3e560fe!8m2!3d22.9898932!4d120.2082484?hl=zh-TW\n麵屋青鳥\nhttps://www.google.com.tw/maps/place/%E9%BA%B5%E5%B1%8B%E9%9D%92%E9%B3%A5/@22.9691166,120.2253553,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7560a7bd79e5:0xf2ccd8af45cca510!8m2!3d22.9691117!4d120.227544?hl=zh-TW\n淳鳩一夫拉麵\nhttps://www.google.com.tw/maps/place/%E6%B7%B3%E9%B3%A9%E4%B8%80%E5%A4%AB%E6%8B%89%E9%BA%B5%EF%BC%88%E5%BA%97%E4%BC%91%E7%9C%8B%E8%87%89%E6%9B%B8%EF%BC%89/@22.9955872,120.1990443,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7663db357fab:0xbb2e072a5c93d199!8m2!3d22.9955823!4d120.201233?hl=zh-TW")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
    
    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "菜良sara日式拉麵\nhttps://www.google.com.tw/maps/place/%E8%8F%9C%E8%89%AFsara%E6%97%A5%E5%BC%8F%E6%8B%89%E9%BA%BA/@22.9810728,120.2141869,17z/data=!3m1!4b1!4m5!3m4!1s0x346e768334367327:0xcc0a9b850adcbbb1!8m2!3d22.9810908!4d120.2164303?hl=zh-TW")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
