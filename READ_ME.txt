##running this script##

Python 3 is required to run this script. 

to run this script:
1. in the directory containing a copy of all SBC files you want to edit, place the following files:
auto_mod.py
available_list.txt
2. in powershell, navigate to this directory
3. execute the python script

##current status##

Currently, there are two functioning features. They are as follows:

#auto replacement of non-basic component requirements
This functionality removes any non-basic component requirements for blocks. Essentially, this entails removing any requirement for components that cannot be created from a survival kit, replacing them with components that can be created from a survival kit. The only exception is that any component requirements for power cells will not be changed.

#manual editing of required components
Currently, the following can be manually edited:
-the component types of required components
-the required quantity of required components
-the critical component

At the moment, these two values can be changed, but a component requirement cannot be removed.

The following cannot be edited as of this update, however implementation of these capababilities is planned:
-secondary values specific to certain blocks: for example, power consumption, assembly speed, refining speed, etc

##Using this script##
This is a command line utility. There is no graphical interface. Currently, this script only works on files in the "CubeBlocks" folder. The text file "available_list" must contain the file names of any SBC files you want to edit. Do not include the file extension. Each file name must be on a separate line. Avoid placing any blank lines in this file. If a file is listed, the corresponding SBC file must be in the directory containing the script files. 

#Using the auto-replacement feature
select the file you want to edit, then select the auto-replacement option.

#using the manual edit option
At the manual editing menu, type in the name of the block you want to edit. This must be the name of the block as it is called in the SBC file, not the block's in game name. Once you make a valid selection, the component requirements will be displayed, along with the critical component requirement. To edit any of these properties, use the following input formats:

To edit the component type, use the following format for the input: line_number-component-value. Available line numbers will be displayed alongside the related component requirements. Examples are below:
0-component-SteelPlate
2-component-Computer

To edit the required quantity, use the following format for the input: line_number-quantity-value. Examples are below:
2-quantity-33
4-quantity-23

To edit a critical component, use the following format for input: critical-value. Examples are below:
critical-SteelPlate
critical-Computer

#making SBC files available for editing
Example contents of available_list.txt:
CubeBlocks_ArmorPanels
CubeBlocks_Automation
CubeBlocks_Communications
CubeBlocks_Control
CubeBlocks_DecorativePack
CubeBlocks_DecorativePack2
CubeBlocks_Doors
CubeBlocks_Economy
CubeBlocks_Energy
CubeBlocks_Extras
CubeBlocks_Frostbite
CubeBlocks_Gravity
CubeBlocks_IndustrialPack
CubeBlocks_Interiors
CubeBlocks_LCDPanels
CubeBlocks_Lights
CubeBlocks_Logistics
CubeBlocks_Mechanical
CubeBlocks_Medical
CubeBlocks_Production
CubeBlocks_ScrapRacePack
CubeBlocks_SparksOfTheFuturePack
CubeBlocks_Symbols
CubeBlocks_Thrusters
CubeBlocks_Tools
CubeBlocks_Utility
CubeBlocks_Warfare1
CubeBlocks_Weapons
CubeBlocks_Wheels
CubeBlocks_Windows
