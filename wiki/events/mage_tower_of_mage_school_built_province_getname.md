#Information
 - Title: Mage Tower of [mage_school_built_province.GetName]
 - ID: mages_estate_events.10
#Description
Mage Tower of [mage_school_built_province.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Allow it

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have treasury is 250
 - Multiplied by 2 if has trade goods is damestear, and has trade goods is precursor relics, and has trade goods is incense, and has trade goods is chinaware


###Efects:<ul><li>event target:mage school built province:</li><ul><li>add building construction:</li><ul><li>building = mage_tower</li><li>speed = 0.5</li><li>cost = 0.5</li></ul><li>hidden effect:</li><ul><li>add province modifier:</li><ul><li>name = mage_build_tower</li><li>duration = 1826</li><li>hidden = yes</li></ul><li>fire province event [mages_estate_events.25](mages_estate_events.25_slug) in 1825 days</li></ul></ul><li>add prestige = -10</li></ul>

___
##Stop them!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has estate influence has estate is estate mages, and estate influence has influence is 70; and  has treasury is 250


###Efects:<ul><li>reduce estate mages loyalty effect = yes</li><li>event target:mage school built province:</li><ul><li>add named unrest:</li><ul><li>name = mage_tower_rejected</li><li>value = 10</li></ul></ul></ul>
