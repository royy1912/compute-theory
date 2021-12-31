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
        send_text_message(reply_token, "覺丸\nhttps://www.google.com.tw/maps/place/%E8%A6%BA%E4%B8%B8%E6%8B%89%E9%BA%B5/@22.9960078,120.2275515,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76c075aa3a33:0x6399402cf32a429c!8m2!3d22.9959967!4d120.2297791?hl=zh-TW\n一拉麵\nhttps://www.google.com.tw/maps/place/%E3%84%A7%E6%8B%89%E9%9D%A2-%E8%B1%9A%E9%AA%A8%E5%B0%88%E8%B3%A3/@23.0086666,120.218289,17z/data=!3m1!4b1!4m5!3m4!1s0x346e77989d1e8655:0x81024a287238f3d0!8m2!3d23.0086639!4d120.2205063?hl=zh-TW")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
    
    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state3")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
