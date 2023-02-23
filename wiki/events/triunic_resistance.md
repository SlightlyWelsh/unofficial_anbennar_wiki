#Information
 - Title: Triunic Resistance
 - ID: centaur.24
#Description
Triunic Resistance
#Mean Time to Happen:
Base time = 1 years

#Options

___
##Just walk on them

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:triunic rebel province:</li><ul><li>If area has owned by is ROOT, and  has culture group is triunic, and does not have province modifier is triunic resistance:</li><ul><li>nationalist rebels = 3</li><li>add province modifier:</li><ul><li>name = triunic_resistance</li><li>duration = 3650</li></ul><li>random list:</li><ul><li>33:</li><ul><li>add base tax = -1</li></ul><li>33:</li><ul><li>add base production = -1</li></ul><li>34:</li><ul><li>add base manpower = -1</li></ul></ul></ul></ul></ul>

___
##Perhaps we should grant them some local autonomy

###Available if:
<li>event target:triunic rebel province:</li><ul><li>any core country:</li><ul><li>None of the following:</li><ul><li>exists</li></ul></ul></ul><li>has country flag [centaur_special_cb](../flags/centaur_special_cb.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:triunic rebel province:</li><ul><li>If random core country does not have exists:</li><ul><li>ROOT:</li><ul><li>release = PREV</li><li>create subject:</li><ul><li>subject type = centaur_dominion</li><li>subject = PREV</li></ul></ul><li>hidden effect:</li><ul><li>change religion = event_target:triunic_rebel_province</li><li>change government = republic</li><li>add government reform = lake_republic</li></ul></ul></ul></ul>
