from message_observer import MessageObserver
from message_observable import MessageObservable

obs = MessageObserver()
obs2 = MessageObserver()
obs3 = MessageObserver()

observable = MessageObservable()

observable.register_observer(obs)
observable.register_observer(obs2)
observable.register_observer(obs3)

observable.write_message('Alou Alou')
observable.write_message('Alou Alou 2')