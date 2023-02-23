This page has the same name as others. For full listing see bottom of [the base page](the_passage.md).

#Information
 - Title: The Passage Complete
 - ID: CliffsOfRuin_events.5
#Description
The Passage Complete
#Options

___
##A great success, carry on then

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = root</li><li>remove province modifier = ruin_cliff_passage_potential</li><li>add permanent province modifier:</li><ul><li>name = m_arca_venaan</li><li>duration = -1</li></ul><li>set province flag [prov_ruin_cliff_passage](../flags/prov_ruin_cliff_passage.md)</li><li>If has province id is 1031:</li><ul><li>2757:</li><ul><li>discover country = owner</li><li>remove province modifier = ruin_cliff_passage_potential</li><li>add permanent province modifier:</li><ul><li>name = ruin_cliff_passage_link</li><li>duration = -1</li></ul></ul></ul><li>else:</li><ul><li>1031:</li><ul><li>discover country = owner</li><li>remove province modifier = ruin_cliff_passage_potential</li><li>add permanent province modifier:</li><ul><li>name = ruin_cliff_passage_link</li><li>duration = -1</li></ul></ul></ul><li>owner:</li><ul><li>add prestige = 5</li><li>clr country flag [ruin_cliff_finished](../flags/ruin_cliff_finished.md)</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [the_passage_complete22_1](the_passage_complete22_1.md)
