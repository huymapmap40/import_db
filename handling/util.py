import inspect
import types

class Util:
    dictOrigin = {}

    @staticmethod
    def parseObject2Dict(obj): #Method not done
        if "models." in str(obj.__class__):
            dictObj = obj.__dict__
            for key, value in dictObj.items():
                if type(value) != list:
                    if "models." in str(value.__class__):
                        Util.parseObject2Dict(value)
                else:
                    for item in value:
                        if "models." in str(item.__class__):
                            Util.parseObject2Dict(item)
        pass
        return obj