class Clock(object):
    def __init__(self, input_hour, input_second):
        delta = ((input_hour * 60) + input_second) % (24 * 60)
        self.ans = abs(((24 * 60) + delta) % (24 * 60))

    def __repr__(self):
        ans_hour = '%02d' % int(self.ans / 60)
        ans_second = '%02d' % int(self.ans % 60)
        res = ans_hour + ":" + ans_second
        return res

    def __eq__(self, other):
        return repr(self) == repr(other)

    def add(self, add_number):
        self.ans = (self.ans + add_number) % (24 * 60)
        return repr(self)
