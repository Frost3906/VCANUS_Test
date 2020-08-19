import json
class JSONDataExtractor:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

Q1 =  JSONDataExtractor('VCANUS_Test\\resource\\bread.json').parsed_data
for i in Q1:
    for j in i.keys():
        if type(i[j])!=dict:
            print("{}: {}".format(j,i[j]))
        else:
            print("{}".format(j))
            for k in i[j]:
                print("{}: {}".format(k,i[j][k]))
    print()
