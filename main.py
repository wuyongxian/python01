from Demo import DemoOne

if __name__=='__main__':
    car=DemoOne()
    print('我是一辆小车车，哈哈哈')

    while True:
        action=input('What shoud I do?[A]accelarate,[B]brake,[O]odometer,[S]average speed?')
        if action not in 'ABOS' or len(action)!=1:
            print('I do not known what to do')
            continue
        if action=='A':
            car.accelerate()
        elif action=='B':
            car.brake()
        elif action=='O':
            print('The car have driven {} kilometers' .format(car.odometer))
        elif action=='S':
            print('The car average speed is {} kph' .format(car.average_speed()))

        car.step()
        car.say_state()
