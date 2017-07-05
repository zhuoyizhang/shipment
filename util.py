import configparser

def tolist(str):
    lst=list()
    for i in str.split(','):
        lst.append(i)
    return lst

def getConfigParent(config):
    dict1 = dict()

    dict1['apps'] = tolist(config['apps'])
    dict1['shipment'] = config['shipment'].strip('\'')


    return dict1


def getConfigChild(config):
    dict1 = dict()

    print(config['filename'])
    dict1['filename'] = config['filename'].strip('\'')

    # platform
    dict1['startCol'] = config['startCol']
    dict1['endCol'] = config['endCol']
    dict1['exclude'] = tolist(config['exclude'])
    dict1['cyclerow'] = config['cyclerow']
    dict1['platformrow'] = config['platformrow']

    # option code
    dict1['startCol_loc'] = config['startCol_loc']
    dict1['endCol_loc'] = config['endCol_loc']
    dict1['exclude_loc'] = tolist(config['exclude_loc'])
    dict1['optioncode_row'] = config['optioncode_row']
    print(dict1['exclude'])

    return dict1


def loadConfig(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

