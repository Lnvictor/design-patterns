from observer import Observer


class MessageObserver(Observer):
    def update(self, data):
        print(f'New message received from observable: {data}')
