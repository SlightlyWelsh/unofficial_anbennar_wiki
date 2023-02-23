This page has the same name as others. For full listing see bottom of [the base page](magical_complications2.md).

#Information
 - Title: Magical Complications
 - ID: magic_estate.16
#Description
Magical Complications
#Options

___
##This child is our new heir!

###Efects:<ul><li>If has heir:</li><ul><li>If has reform is magical elite reform:</li><ul><li>custom tooltip = magic_estate_magical_elite_heir</li></ul><li>else:</li><ul><li>custom tooltip = magic_estate_disinherit_heir</li><li>add prestige = -50</li></ul></ul><li>If has ruler flag is [boy_child](../flags/boy_child.md):</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li></ul></ul><li>If has ruler flag is [girl_child](../flags/girl_child.md):</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>female = yes</li></ul></ul><li>set heir mage effect = yes</li><li>If is female:</li><ul><li>kill ruler = yes</li></ul><li>else:</li><ul><li>kill consort = yes</li></ul></ul>

___
##Our existing heir will serve us better.

###Available if:
<li>has heir</li>

###Efects:<ul><li>If is female:</li><ul><li>kill ruler = yes</li></ul><li>else:</li><ul><li>kill consort = yes</li></ul></ul>
