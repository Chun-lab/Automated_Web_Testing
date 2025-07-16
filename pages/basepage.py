from common.driver import DriverOperate


class BasePage:

    def __init__(self):
        self.operate: DriverOperate = DriverOperate.globalDriverOperate
