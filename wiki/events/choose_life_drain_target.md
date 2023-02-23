#Information
 - Title: Choose Life Drain Target
 - ID: magic_ruler.13
#Description
Choose Life Drain Target
#Options

___
##Drain Heir

###Available if:
<li>has ruler flag [necromancy_1](../flags/necromancy_1.md)</li><li>has heir</li><li>government is monarchy</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has government is monarchy, and has heir adm is 3, and has heir dip is 3, and has heir mil is 3


###Efects:<ul><li>reduce legitimacy medium effect = yes</li><li>increase witch king points small = yes</li><li>add ruler modifier:</li><ul><li>name = magic_witch_king_drain_life</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_drain_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>set country flag [spell_4](../flags/spell_4.md)</li><li>tooltip:</li><ul><li>random:</li><ul><li>chance = 25</li><li>kill heir:</li><ul><li>allow new heir = no</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>33:</li><ul><li>add adm power = 30</li></ul><li>33:</li><ul><li>add dip power = 30</li></ul><li>33:</li><ul><li>add mil power = 30</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul></ul>

___
##Drain Consort

###Available if:
<li>has ruler flag [necromancy_1](../flags/necromancy_1.md)</li><li>has consort</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has consort adm is 3, and has consort dip is 3, and has consort mil is 3


###Efects:<ul><li>reduce legitimacy small effect = yes</li><li>add prestige = -2</li><li>increase witch king points small = yes</li><li>add ruler modifier:</li><ul><li>name = magic_witch_king_drain_life</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_drain_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>set country flag [spell_5](../flags/spell_5.md)</li><li>tooltip:</li><ul><li>random:</li><ul><li>chance = 25</li><li>remove consort = yes</li></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>33:</li><ul><li>add adm power = 20</li></ul><li>33:</li><ul><li>add dip power = 20</li></ul><li>33:</li><ul><li>add mil power = 20</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul></ul>

___
##Drain Advisor

###Available if:
<li>has ruler flag [necromancy_1](../flags/necromancy_1.md)</li><li>has advisor</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add prestige = -5</li><li>increase witch king points small = yes</li><li>add ruler modifier:</li><ul><li>name = magic_witch_king_drain_life</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_drain_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>set country flag [spell_6](../flags/spell_6.md)</li><li>tooltip:</li><ul><li>random:</li><ul><li>chance = 25</li><li>kill advisor = random</li></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>33:</li><ul><li>add adm power = 20</li></ul><li>33:</li><ul><li>add dip power = 20</li></ul><li>33:</li><ul><li>add mil power = 20</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul></ul>

___
##Drain the Populace

###Available if:
<li>has ruler flag [necromancy_1](../flags/necromancy_1.md)</li><li>any owned province:</li><ul><li>base tax is at least 2</li><li>base production is at least 2</li><li>base manpower is at least 2</li><li>None of the following:</li><ul><li>devastation is at least 50</li></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.75 if does not have num of cities is 20


###Efects:<ul><li>increase witch king points medium = yes</li><li>add ruler modifier:</li><ul><li>name = magic_witch_king_drain_life</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_drain_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>If random owned province has base tax is 2, and  has base production is 2, and  has base manpower is 2, and does not have devastation is 50:</li><ul><li>tooltip:</li><ul><li>random list:</li><ul><li>10:</li><ul><li>add base tax = -1</li></ul><li>10:</li><ul><li>add base production = -1</li></ul><li>10:</li><ul><li>add base manpower = -1</li></ul></ul></ul><li>hidden effect:</li><ul><li>fire province event [magic_ruler.16](magic_ruler.16_slug) immediately </li></ul><li>add devastation = 20</li></ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>10:</li><ul><li>add adm power = 50</li></ul><li>10:</li><ul><li>add dip power = 50</li></ul><li>10:</li><ul><li>add mil power = 50</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul></ul>

___
##Go back

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>add adm power = 5</li><li>add mil power = 5</li></ul>
