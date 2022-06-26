from observable import Observable


class MessageObservable(Observable):
    def write_message(self, message):
        self.notify_observer(data=message)
