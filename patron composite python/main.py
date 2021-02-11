if name == "main":

topLevelMenu = CompositeElement("GeneralManager") 
subMenuItem1 = CompositeElement("Manager1") 
subMenuItem2 = CompositeElement("Manager2") 
subMenuItem11 = LeafElement("Developer11") 
subMenuItem12 = LeafElement("Developer12") 
subMenuItem21 = LeafElement("Developer21") 
subMenuItem22 = LeafElement("Developer22") 
subMenuItem1.add(subMenuItem11) 
subMenuItem1.add(subMenuItem12) 
subMenuItem2.add(subMenuItem22) 
subMenuItem2.add(subMenuItem22) 

topLevelMenu.add(subMenuItem1) 
topLevelMenu.add(subMenuItem2) 
topLevelMenu.showDetails() 