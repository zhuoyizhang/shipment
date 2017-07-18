import configparser
import openpyxl
from openpyxl.utils import coordinate_from_string, column_index_from_string

def tolist(str):
    lst=list()
    for i in str.split(','):
        lst.append(i)
    return lst


def getConfigTree(cycle,config):
    tree = dict(config)
    subtree = dict()
    for section in tree:
        if section.startswith(cycle):
            subtree[section] = tree[section]
    print(subtree)
    return subtree

#new conf change here
def getConfigParent(subtree):
    for section in subtree:
        if section.find('.') != -1:continue
        print(section)
        config = subtree[section]
    dict1 = dict()

    dict1['apps'] = tolist(config['apps'])
    dict1['shipment'] = config['shipment'].strip('\'')

    return dict1


def getConfigChildren(subtree):
    dict1 = dict()

    for section in subtree:
        if section.find('.') != -1:
            dict1[section] = subtree[section]
    return dict1

#new conf change here
def getConfigChild(section):

    config = section
    print(type(config))
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
    #
    dict1['type'] = config['type']
    dict1['mapping'] = config['mapping']

    print(dict1['exclude'])

    return dict1


def loadConfig(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

def getCycle(coordinate, dictCycle, config):
    xy = coordinate_from_string(coordinate)
    col=xy[0]
    cycle = ''
    types=tolist(config['type'])
    mapping=tolist(config['mapping'])
    #print(types)
    #print(mapping)
    for i in range(len(types)):
        #print(dictCycle[col].upper() + '|' + types[i])
        if dictCycle[col].upper() == types[i].upper():
            cycle = mapping[i]
            #print(cycle)
            break
    return cycle