#Information
 - Title: Reconstruction of the Old Canals
 - ID: bulwar_flavour.24
#Description
Reconstruction of the Old Canals
#Options

___
##Dredge the Old Canals

###Available if:
<li>601:</li><ul><li>has province modifier old_bulwari_canals</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add treasury = -500</li><li>601:</li><ul><li>add building construction:</li><ul><li>building = bulwari_canals</li><li>speed = 1</li><li>cost = 1</li></ul><li>hidden effect:</li><ul><li>set variable:</li><ul><li>which = cons_prog</li><li>value = 0.5</li></ul></ul></ul></ul>

___
##Repair the locks and lifts

###Available if:
<li>601:</li><ul><li>has province modifier bulwari_canals</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add treasury = -1000</li><li>601:</li><ul><li>add building construction:</li><ul><li>building = bulwari_locks_and_lifts</li><li>speed = 1</li><li>cost = 1</li></ul><li>hidden effect:</li><ul><li>set variable:</li><ul><li>cons prog = 0.5</li></ul></ul></ul></ul>

___
##Build the Great Bulwari Watercourse 

###Available if:
<li>601:</li><ul><li>has province modifier bulwari_locks_and_lifts</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add treasury = -1500</li><li>601:</li><ul><li>add building construction:</li><ul><li>building = great_bulwari_watercourse</li><li>speed = 1</li><li>cost = 1</li></ul><li>hidden effect:</li><ul><li>set variable:</li><ul><li>cons prog = 0.5</li></ul></ul></ul></ul>

___
##Perhaps we should delay this project...

###AI weighting:
AI weights this option at 0

