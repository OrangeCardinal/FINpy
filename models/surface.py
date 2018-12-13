class Surface:
    def __init__(self, x_axis, y_axis, values):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.values = values


    def __call__(self, x, y):
        i1,i2 = bound(x, self.x_axis)
        j1,j2 = bound(y, self.y_axis)
        
        x1 = self.x_axis[i1]
        x2 = self.x_axis[i2]
        y1 = self.y_axis[j1]
        y2 = self.y_axis[j2]
        
        r = (x2-x1) * (y2-y1)
        result  = (self.values[i1, j1] / r) * (x2 - x) * (y2 - y)
        result += (self.values[i2, j1] / r) * (x - x1) * (y2 - y) 
        result += (self.values[i1, j2] / r) * (x2 - x) * (y - y1)
        result += (self.values[i2, j2] / r) * (x - x1) * (y - y1)
        
        return result