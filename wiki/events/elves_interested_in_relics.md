#Information
 - Title: Elves Interested in Relics
 - ID: flavor_ameion.121
#Description
Elves Interested in Relics
#Mean Time to Happen:
Base time = 180 months
 - Multiplied by 2 if has any owned province has province modifier is G52 excavated, and any owned province has elven minority trigger is yes
 - Multiplied by 2 if has any owned province has province modifier is G52 excavated, and any owned province has large elven minority trigger is yes

#Options

___
##They are also descended from these lands.

###Efects:<ul><li>medium increase of elven tolerance effect = yes</li><li>If random owned province has province modifier is G52 excavated, and does not have large elven minority trigger is yes:</li><ul><li>add elven minority size effect = yes</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -5</li></ul><li>If has estate is estate artificers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = -10</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 10</li></ul></ul>

___
##They abandoned these lands, and are not welcome.

###Efects:<ul><li>medium decrease of elven tolerance effect = yes</li><li>increase legitimacy small effect = yes</li></ul>

___
##They will never be welcome here.

###Efects:<ul><li>large decrease of elven tolerance effect = yes</li><li>increase legitimacy medium effect = yes</li><li>custom tooltip = ameion_no_elves</li><li>set country flag [ameion_no_elf](../flags/ameion_no_elf.md)</li></ul>
