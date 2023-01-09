#include "modules/TestDevice.hpp"
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
	// generated code here
}
void DeviceAB::initCollections(){
	std::shared_ptr<Iolink> Colection = Iolink::getInstance();
	// generated code here    
}
