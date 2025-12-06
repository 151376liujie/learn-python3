from collections import OrderedDict

if __name__ == '__main__':
    di = OrderedDict()
    di['abc'] = 123
    di['cdb'] = 244
    di['ddd'] = 543
    di['cab'] = 245
    di['gds'] = 643

    for k, v in di.items():
        print(k, "==", v)
