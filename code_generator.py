#!/usr/bin/python3.9
# coding=utf-8

# Task 5 - Code generator

import json


def write_prologue(output_file: str='output.cpp'):
    """Writes first part of the template to the `output_file`

    Parameters
    ---------------------------
    output_file : (str, optional)
        File where generated code will be printed. Default value: `output.cpp`.
    """

    prologue = """#include "modules/TestDevice.hpp"
#include "iolink/iolink.hpp"

#define True true
#define False false

DeviceAB::DeviceAB(uint8_t slot):
    Module(slot, "IODevice")
{
    initItems();
    initCollections();
}

DeviceAB::~DeviceAB()
{
}

void DeviceAB::initItems()
{
"""

    with open(output_file, 'w') as cpp_file:
        cpp_file.write(prologue)
    
def write_def_collection(output_file: str='output.cpp'):
    """Writes second part of the template to the `output_file`

    Parameters
    ---------------------------
    output_file : (str, optional)
        File where generated code will be printed. Default value: `output.cpp`.
    """

    str_coll = """}
void DeviceAB::initCollections()
{
    std::shared_ptr<Iolink> Colection = Iolink::getInstance();
"""

    with open(output_file, 'a') as cpp_file:
        cpp_file.write(str_coll)

def append_item_file(item: dict, output_file: str='output.cpp'):
    """Writes details of item to the `initItems()` function
    
    Parameters
    ---------------------------
    item : dict
        details of item which will be printed to the output file
    output_file : (str, optional)
        File where generated code will be printed. Default value: `output.cpp`.
    """

    with open(output_file, 'a') as cpp_file:
        cpp_file.write(f"\tinitDataItem(\"{item['name']}\", {item['tag']}, \"{item['type']}\", {item['size']});\n")

def append_collections(json_dict: dict, output_file: str='output.cpp'):
    """Writes collections to the `initCollections()` function
    
    Parameters
    ---------------------------
    json_dict : dict
        dictionary of collection names with names of items
    output_file : (str, optional)
        File where generated code will be printed. Default value: `output.cpp`.
    """

    for collection, items in json_dict.items():    
        for item in items:
            with open(output_file, 'a') as cpp_file:
                cpp_file.write(f"\tCollection.{collection}->push(\"{item['name']}\");\n")
    with open(output_file, 'a') as cpp_file:
        cpp_file.write('}\n')

if __name__ == "__main__":
    write_prologue()

    with open('input_example.json', 'r') as json_file:
        file_contents = json_file.read()

    json_dict = json.loads(file_contents)
    for collection, items in json_dict.items():
        for item in items:
            append_item_file(item)

    write_def_collection()
    append_collections(json_dict)
