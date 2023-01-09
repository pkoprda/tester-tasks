#!/usr/bin/python3.9
# coding=utf-8

# Task 5

import json


def write_prologue():
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

    with open('output.cpp', 'w') as cpp_file:
        cpp_file.write(prologue)
    
def write_def_collection():
    str_coll = """}
void DeviceAB::initCollections()
{
    std::shared_ptr<Iolink> Colection = Iolink::getInstance();
"""

    with open('output.cpp', 'a') as cpp_file:
        cpp_file.write(str_coll)

def append_item_file(item):
    with open('output.cpp', 'a') as cpp_file:
        cpp_file.write(f"\tinitDataItem(\"{item['name']}\", {item['tag']}, \"{item['type']}\", {item['size']});\n")

def append_collections(json_dict):
    for collection, items in json_dict.items():    
        for item in items:
            with open('output.cpp', 'a') as cpp_file:
                cpp_file.write(f"\tCollection.{collection}->push(\"{item['name']}\");\n")
    with open('output.cpp', 'a') as cpp_file:
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
