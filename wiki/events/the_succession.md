#Information
 - Title: The succession
 - ID: bim_lau_flavour.3
#Description
The succession
#Options

___
##My eldest son will lead the nation.

###Available if:
<li>has country flag [bim_lau_eldest_son_succession](../flags/bim_lau_eldest_son_succession.md)</li>

###Efects:<ul><li>custom tooltip = bim_lau_new_missions_tt</li><li>kill ruler = yes</li><li>add stability = 1</li><li>hidden effect:</li><ul><li>set country flag [bim_lau_normal_missions](../flags/bim_lau_normal_missions.md)</li><li>swap non generic missions = yes</li></ul></ul>

___
##This warlord will lead Bim Lau to greatness.

###Available if:
<li>has country flag [harimari_warlord_succession](../flags/harimari_warlord_succession.md)</li>

###Efects:<ul><li>custom tooltip = bim_lau_new_missions_tt</li><li>kill ruler = yes</li><li>add stability = 1</li><li>hidden effect:</li><ul><li>set country flag [harimari_supremacy_succession](../flags/harimari_supremacy_succession.md)</li><li>swap non generic missions = yes</li></ul><li>change primary culture = royal_harimari</li><li>country gets the modifier "army_reform" for 25 years</li></ul>

___
##Follow the advice of the estates.

###Available if:
<li>has country flag [bim_lau_estates_succession](../flags/bim_lau_estates_succession.md)</li>

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>custom tooltip = bim_lau_new_missions_tt</li><li>define ruler:</li><ul><li>culture = ranilau</li><li>dynasty = "Ang Rang"</li><li>age = 16</li><li>adm = 4</li><li>dip = 5</li><li>mil = 4</li><li>claim = 70</li></ul><li>hidden effect:</li><ul><li>set country flag [bim_lau_normal_missions](../flags/bim_lau_normal_missions.md)</li><li>set country flag [bim_lau_becomes_human](../flags/bim_lau_becomes_human.md)</li><li>swap non generic missions = yes</li></ul></ul>

___
##This is unacceptable. Our dynasty must continue.

###Available if:
<li>has country flag [bim_lau_estates_succession](../flags/bim_lau_estates_succession.md)</li>

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>custom tooltip = bim_lau_new_missions_tt</li><li>add legitimacy = -30</li><li>If every owned province has culture is ranilau:</li><ul><li>add unrest = 15</li></ul><li>define heir:</li><ul><li>culture = royal_harimari</li><li>dynasty = ROOT</li><li>age = 23</li><li>hidden = yes</li></ul><li>hidden effect:</li><ul><li>set country flag [bim_lau_normal_missions](../flags/bim_lau_normal_missions.md)</li><li>set country flag [bim_lau_stays_harimari](../flags/bim_lau_stays_harimari.md)</li><li>swap non generic missions = yes</li></ul></ul>
