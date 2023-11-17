CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels_list):
        self.channels = {number + 1: channel for number, channel in enumerate(channels_list)}
        self.current = 1

    def first_channel(self):
        self.current = 1
        return self.channels[self.current]

    def last_channel(self):
        self.current = len(self.channels)
        return self.channels[self.current]

    def turn_channel(self, number):
        if number not in self.channels.keys():
            print(f"Channel number {number} is not on the channels list")
            return None
        self.current = number
        return self.channels[self.current]

    def next_channel(self):
        self.current = self.current + 1 if self.current < len(self.channels) else 1
        return self.channels[self.current]

    def previous_channel(self):
        self.current = len(self.channels) if self.current == 1 else self.current - 1
        return self.channels[self.current]

    def current_channel(self):
        return self.channels[self.current]

    def exists(self, arg):
        existence = "No"
        if type(arg) is int or type(arg) is str:
            for number, channel in self.channels.items():
                if arg in (number, channel):
                    existence = "Yes"
        return existence


controller = TVController(CHANNELS)

controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel() == "BBC"

controller.exists(4) == "No"

controller.exists("BBC") == "Yes"
