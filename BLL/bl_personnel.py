from DAL.Repository import Ripository


class bl_personnel():
    def Add(self, obj):
        print(str(obj))
        if int(obj.age) >= 18:
            n = Ripository()
            return n.Add(obj)
        else:
            return "2"

    def Read(self, obj):
        pass

    def Update(self, obj, id):
        pass

    def Delete(self, obj):
        pass

    def ReadById(self, obj, id):
        pass
