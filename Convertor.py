import coremltools

class MessageLog:
    @staticmethod
    def bluePrint(text, appendNewline):
        log = "\033[1;36;40m" + text + "\033[0m"
        if appendNewline == True:
            log += "\n"
        print(log)

    @staticmethod
    def errorPrint(text):
        print("\n\033[1;31;40m" + text + "\033[0m\n")

class CoreMLConverter:
    _kerasModelPath = None
    _description = """
    Welcome to CoreML Converter
    Author: Geektree0101 2017.12.17

    [MENU]
    1. Create Simple CoreML Model
    2. add trained model file path
    3. exit [any key]"""

    def __init__(self):
        MessageLog.bluePrint(self._description, True)
        while(1):
            insertedKey = raw_input("\033[1;37;40mInsert: \033[0m")
            if insertedKey == "1":
                self.convertCoreMLModel()
            elif insertedKey == "2":
                self.appendFilePath()
            else:
                break

    def convertCoreMLModel(self):
        if type(self._kerasModelPath) != str:
            MessageLog.errorPrint("Plz insert model file path")
        elif type(self._kerasModelPath) == str and len(a) < 1:
            MessageLog.errorPrint("file path is too short")
        else:
            modelName = raw_input("\033[1;37;40mInsert model name: \033[0m")
            description = raw_input("\033[1;37;40mshort description: \033[0m")
            inputDescription = raw_input("\033[1;37;40minput description: \033[0m")
            outputDescription = raw_input("\033[1;37;40moutput description: \033[0m")
            model = coremltools.converters.keras.convert(self._kerasModelPath)

            model.author = 'Geektree0101'
            model.license = 'MIT'
            model.short_description = description
            model.input_description['image'] = inputDescription
            model.output_description['output'] = outputDescription
            model.save("./CoreMLModels/" + modelName + ".mlmodel")

    def appendFilePath(self):
        self._kerasModelPath = raw_input("\033[1;37;40mInsert file path: \033[0m")

if __name__ == '__main__':
    appInstance = CoreMLConverter()


