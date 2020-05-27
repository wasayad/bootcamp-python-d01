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

    def __add__(self, tosub):
        temp = Vector(self.size)
        if type(self) is type(tosub):
            if self.size is len(tosub.values):
                for i in range(0, self.size):
                    temp.values[i] = self.values[i] + tosub.values[i]
        else:
            for i in range(0, self.size):
                temp.values[i] = self.values[i] + tosub
        return temp

    def __sub__(self, tosub):
        temp = Vector(self.size)
        if type(self) is type(tosub):
            if self.size is len(tosub.values):
                for i in range(0, self.size):
                    temp.values[i] = self.values[i] - tosub.values[i]
        else:
            for i in range(0, self.size):
                temp.values[i] = self.values[i] - tosub
        return temp

    def __truediv__(self, tosub):
        temp = Vector(self.size)
        if type(self) is type(tosub):
            if self.size is len(tosub.values):
                for i in range(0, self.size):
                    if tosub.values[i] > float(0):
                        temp.values[i] = self.values[i] / tosub.values[i]
        else:
            for i in range(0, self.size):
                if tosub.values[i] > float(0):
                    temp.values[i] = self.values[i] / tosub
        return temp

    def __mul__(self, tosub):
        temp = Vector(self.size)
        if type(self) is type(tosub):
            if self.size is len(tosub.values):
                for i in range(0, self.size):
                    temp.values[i] = self.values[i] * tosub.values[i]
        else:
            for i in range(0, self.size):
                temp.values[i] = self.values[i] * tosub
        return temp

    def __str__(self):
        stri = ""
        stri = stri + 'Vector(values='
        stri = stri + str(self.values)
        stri = stri + ', size='
        stri = stri + str(self.size)
        stri = stri + ')'
        return stri

    def __repr__(self):
        return {'values': self.values, 'Size': self.size}
