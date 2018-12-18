class RobotController:
    def move(self, data):
        print(data)
        self.move_left()
        self.move_right()

    def move_left(self):
        print('moving left')

    def move_right(self):
        print('moving right')