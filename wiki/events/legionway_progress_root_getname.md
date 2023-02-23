#Information
 - Title: Legionway Progress: [Root.GetName]
 - ID: flavor_castanor.4
#Description
Legionway Progress: [Root.GetName]
#Mean Time to Happen:
Base time = 1825 days
 - Multiplied by 0.75 if has owner has full idea group is economic ideas
 - Multiplied by 0.8 if has owner has full idea group is administrative ideas
 - Multiplied by 0.9 if has development is 10
 - Multiplied by 0.9 if has development is 15
 - Multiplied by 0.8 if has development is 20
 - Multiplied by 0.7 if has development is 30
 - Multiplied by 0.7 if is prosperous
 - Multiplied by 2 if has devastation is 1
 - Multiplied by 0.8 if has any neighbor province has province modifier is castanor legionway
 - Multiplied by 0.8 if has has province modifier is castanorian citadel, and has province modifier is castanor new citadel, and has province modifier is castanor citadel local admin center
 - Multiplied by 1.1 if has province distance has who is 840, and province distance has distance is 150
 - Multiplied by 1.2 if has province distance has who is 840, and province distance has distance is 250
 - Multiplied by 1.3 if has province distance has who is 840, and province distance has distance is 350
 - Multiplied by 1.3 if has terrain is mountain, and has terrain is highlands, and has terrain is marsh, and has terrain is jungle
 - Multiplied by 1.2 if has terrain is forest, and has terrain is hills, and has terrain is woods, and has terrain is desert
 - Multiplied by 0.7 if has B32 has template is merc castanorian legion 1, and has template is merc castanorian legion 2, and has template is merc castanorian legion 3, and has template is merc castanorian legion 4, and has template is merc castanorian legion 5, and has template is merc castanorian legion 6, and has template is merc castanorian legion 7, and has template is merc castanorian legion 8; and any hired mercenary company has location has province flag is [legionway_construction_prov_@ROOT](../flags/legionway_construction_prov_root.md)

#Options

___
##Start construction!

###Available if:
<li>None of the following:</li><ul><li>has province modifier castanor_legionway</li></ul><li>NOT:</li><ul><li>has province modifier castanor_building_legionway_construction</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>remove province modifier = castanor_building_legionway_survey</li><li>add permanent province modifier:</li><ul><li>name = castanor_building_legionway_construction</li><li>duration = -1</li></ul><li>owner:</li><ul><li>add treasury = -50</li></ul></ul>

___
##We can't spare any resources, leave it for later

###Available if:
<li>None of the following:</li><ul><li>has province modifier castanor_legionway</li></ul><li>NOT:</li><ul><li>has province modifier castanor_building_legionway_construction</li></ul>

###AI weighting:
AI weights this option at 1
 - Multiplied by 0 if does not have owner has treasury is 100


###Efects:<ul><li>owner:</li><ul><li>add prestige = -5</li></ul></ul>

___
##Legionway Complete!

###Available if:
<li>has province modifier castanor_building_legionway_construction</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>remove province modifier = castanor_building_legionway_construction</li><li>clr province flag [legionway_construction_prov_@ROOT](../flags/legionway_construction_prov_root.md)</li><li>add permanent province modifier:</li><ul><li>name = castanor_legionway</li><li>duration = -1</li></ul><li>owner:</li><ul><li>add prestige excess to splendour effect:</li><ul><li>VAL = 1</li></ul></ul><li>If does not have owned by is B32:</li><ul><li>B32:</li><ul><li>the event [Legionway Complete in Subject](../events/legionway_complete_in_subject.md) happens</li></ul></ul></ul>
