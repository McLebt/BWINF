
class Data:
    data = [10,10,10,50,50,100,100,100,500,500,500,1000,1000,1000,5000]
    train_data = []

    def getData(self, dataFileName):
        text_file = open("./data/" + dataFileName + ".txt", "r")
        raw_data = text_file.read().splitlines()
        self.data = raw_data
        self.formatData()
        return self.data

    def formatData(self):
        form_data = []
        del self.data[0]
        for i in self.data:
            split = i.split(" ")
            ic = 0
            while int(split[1]) > ic:
                form_data.append(int(split[0]))
                ic += 1
        self.data = form_data
        return form_data

class Calculation:
    
    def trainData(self, data: Data):
        
        run = 0
        for one_data in data.data:
            for trainwith in data.data:
                data.train_data.append([one_data + trainwith, str(one_data) +":"+ str(trainwith)])
                data.train_data.append([one_data - trainwith, str(one_data) +":"+ str(trainwith)])
        

d = Data()
calc = Calculation()
calc.trainData(d)
print(d.train_data)
