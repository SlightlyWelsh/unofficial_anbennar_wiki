#Information
 - Title: The Demands of [venail_purchaser.GetName]
 - ID: venail.22
#Description
The Demands of [venail_purchaser.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We Won't surrender.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has owns is 93:</li><ul><li>event target:venail purchaser:</li><ul><li>declare war with cb:</li><ul><li>who = A21</li><li>casus belli = cb_conquest</li><li>war goal province = 93</li></ul></ul></ul><li>Else if has owns is 94:</li><ul><li>event target:venail purchaser:</li><ul><li>declare war with cb:</li><ul><li>who = A21</li><li>casus belli = cb_conquest</li><li>war goal province = 94</li></ul></ul></ul><li>Else if has owns is 127:</li><ul><li>event target:venail purchaser:</li><ul><li>declare war with cb:</li><ul><li>who = A21</li><li>casus belli = cb_conquest</li><li>war goal province = 127</li></ul></ul></ul><li>country gets the modifier population_leaving_for_aelantir for 10 years</li><li>custom tooltip = colonies_declare_independence</li><li>hidden effect:</li><ul><li>If every subject country is colonial nation, and  has capital scope has colonial region is colonial noruin:</li><ul><li>declare war with cb:</li><ul><li>who = A21</li><li>casus belli = cb_independence_war</li></ul></ul><li>If every subject country is colonial nation:</li><ul><li>random list:</li><ul><li>30:</li><ul><li>declare war with cb:</li><ul><li>who = A21</li><li>casus belli = cb_independence_war</li></ul></ul><li>70:</li><ul><li>add liberty desire = 60</li></ul></ul></ul></ul></ul>

___
##We must give up the island.

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If venail area has tag is A21, and has was tag is A21:</li><ul><li>cede province = event_target:venail_purchaser</li></ul></ul>
