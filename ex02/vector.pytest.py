class Vector():
    def __init__(self, args):
        if isinstance(args, list) is True:
            self.values = args
            self.size = len(self.values)
        elif isinstance(args, int) is True:
            self.values = list("")
            for i in range(0, args):
                self.values.append(float(i))
            self.size = len(self.values)
        elif isinstance(args, tuple) is True:
            self.values = list("")
            for i in range(args[0], args[1]):
                self.values.append(float(i))
            self.size = len(self.values)
    def __add__(self, toadd):
        temp = Vector(self.size)
        if self.size is len(toadd.values):
            for i in range(0, self.size):
                temp.values[i] = self.values[i] + toadd.values[i]
        return temp
    def __sub__(self, tosub):
        temp = Vector(self.size)
        if self.size is len(tosub.values):
            for i in range(0, self.size):
                temp.values[i] = self.values[i] - tosub.values[i]
        return temp
    def __truediv__(self, todiv):
        temp = Vector(self.size)
        if self.size is len(todiv.values):
            for i in range(0, self.size):
                if todiv.values[i] > 0:
                    temp.values[i] = self.values[i] / todiv.values[i]
                else:
                    temp.values[i] = self.values[i]
        return temp
    def __mul__(self, tosub):
        temp = Vector(self.size)
        if self.size is len(tosub.values):
            for i in range(0, self.size):
                temp.values[i] = self.values[i] * tosub.values[i]
        return temp
    def __str__(self):
        return 'Vector(values='+ str(self.values)+', size='+ str(self.size) + ')'
    def __repr__(self):
        return {'values':self.values, 'Size':self.size}
