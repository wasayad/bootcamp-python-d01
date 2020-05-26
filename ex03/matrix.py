class Matrix():
    def __init__(self, args, *shap):
        if isinstance(args, list) is True:
            self.data = args
            self.shape = (len(self.data), len(self.data[0]))
        elif isinstance(args[0], int) is True and isinstance(args[1], int):
            self.data = list("")
            for i in range(0, args[0]):
                temp = list("")
                for j in range(0, args[1]):
                    temp.append(0.0)
                self.data.append(temp)
            self.shape = (len(self.data), len(self.data[0]))
        elif isinstance(args, tuple) is True:
            self.data = list("")
            for i in range(args[0], args[1]):
                self.data.append(float(i))
            self.shape = (len(self.data), len(self.data[0]))

    def __ad__(self, other):
        temp = Matrix(self.shape)
        if type(self) is type(other):
            if self.shape[0] is other.shape[0] and self.shape[1] is other.shape[1]:
                for i in range(0, self.shape[0]):
                    for j in range(0, self.shape[1]):
                        temp.data[i][j] = self.data[i][j] + other.data[i][j]
        else:
            for i in range(0, self.shape[0]):
                for j in range(0, self.shape[1]):
                    temp.data[i][j] = self.data[i][j] + other
        return(temp)
    def __sub__(self, other):
        temp = Matrix(self.shape)
        if type(self) is type(other):
            if self.shape[0] is other.shape[0] and self.shape[1] is other.shape[1]:
                for i in range(0, self.shape[0]):
                    for j in range(0, self.shape[1]):
                        temp.data[i][j] = self.data[i][j] - other.data[i][j]
        else:
            for i in range(0, self.shape[0]):
                for j in range(0, self.shape[1]):
                    temp.data[i][j] = self.data[i][j] - other
        return(temp)
    def __mul__(self, other):
        temp = Matrix(self.shape)
        if type(self) is type(other):
            if self.shape[0] is other.shape[1] and self.shape[1] is other.shape[0]:
                for x in range(0, self.shape[0])
                    for y in range(0, other.shape[0])
                    for i in range(0, self.shape[0]):
                        for j in range(0, self.shape[1]):
                            temp.data[i][j] = self.data[i][j] * other.data[j][i]
        else:
            for i in range(0, self.shape[0]):
                for j in range(0, self.shape[1]):
                    temp.data[i][j] = self.data[i][j] * other
        return(temp)

data = Matrix([[0.0, 1.0, 2.0],
                [0.0, 2.0, 4.0]], (2,2))
data1 = Matrix([[1.0, 0.0],
                [2.0, 0.0],
                [4.0, 0.0]], (2,2))
data2 = data1 * data
print(data2.data)
print(data.data)
print(data1.data)