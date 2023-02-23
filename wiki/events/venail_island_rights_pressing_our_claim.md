#Information
 - Title: Venáil Island Rights - Pressing Our Claim
 - ID: venail.21
#Description
Venáil Island Rights - Pressing Our Claim
#Mean Time to Happen:
Base time = 15 years
 - Multiplied by 2 if is at war
 - Multiplied by 0.5 if has A21 has any subject country has capital scope has colonial region is colonial noruin
 - Multiplied by 0.5 if has A21 has institution is new world i
 - Multiplied by 10 if has A21 is controlled by the AI; and does not have year is 1555

#Options

___
##Send the Demand

###Available if:
<li>A21:</li><ul><li>Any of the following:</li><ul><li>owns 93</li><li>owns  94</li><li>owns   127</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>A21:</li><ul><li>the event [The Demands of [venail_purchaser.GetName]](../events/the_demands_of_venail_purchaser_getname.md) happens</li></ul><li>If venail area does not have core is event target:venail purchaser; and does not have permanent claim is event target:venail purchaser:</li><ul><li>add permanent claim = event_target:venail_purchaser</li></ul></ul>

___
##We will make our claims known

###Available if:
<li>None of the following:</li><ul><li>owns 93</li><li>owns  94</li><li>owns   127</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if is at war


###Efects:<ul><li>If venail area does not have core is event target:venail purchaser; and does not have permanent claim is event target:venail purchaser:</li><ul><li>add permanent claim = event_target:venail_purchaser</li></ul></ul>

___
##A wise investment!

###Available if:
<li>Any of the following:</li><ul><li>owns 93</li><li>owns  94</li><li>owns   127</li></ul><li>A21:</li><ul><li>None of the following:</li><ul><li>owns 93</li><li>owns  94</li><li>owns   127</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set country flag [bought_venail](../flags/bought_venail.md)</li><li>If venail area has owned by is event target:venail purchaser:</li><ul><li>change religion = ROOT</li><li>set province flag [venail_resettle](../flags/venail_resettle.md)</li><li>fire province event [venail.23](venail.23_slug) in 30 days</li></ul><li>If does not have owned by is event target:venail purchaser:</li><ul><li>If venail area does not have core is event target:venail purchaser; and does not have permanent claim is event target:venail purchaser:</li><ul><li>add permanent claim = event_target:venail_purchaser</li></ul></ul></ul>
