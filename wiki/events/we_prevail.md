#Information
 - Title: We Prevail
 - ID: fed_religious.25
#Description
We Prevail
#Options

___
##For Kalyin!

###Available if:
<li>religion is kalyin_worshippers</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>every owned province:</li><ul><li>change religion = kalyin_worshippers</li></ul><li>lake federation gain 10 points = yes</li><li>add stability = 3</li><li>add prestige = 50</li><li>country gets the modifier victor_fed_religious_war until otherwise removed</li><li>If every known country has religion is kalyin worshippers, and  has country modifier is lake federation member:</li><ul><li>capital scope:</li><ul><li>change religion = kalyin_worshippers</li></ul><li>every owned province:</li><ul><li>random:</li><ul><li>chance = 80</li><li>change religion = kalyin_worshippers</li></ul></ul><li>add prestige = 25</li><li>add stability = 1</li><li>lake federation gain 5 points = yes</li><li>country gets the modifier victor_fed_religious_war until otherwise removed</li></ul><li>If every known country has country modifier is lake federation member, and does not have religion is kalyin worshippers:</li><ul><li>change religion = kalyin_worshippers</li><li>capital scope:</li><ul><li>change religion = kalyin_worshippers</li></ul><li>add stability = -1</li><li>add prestige = -25</li><li>lake federation lose 2 points = yes</li><li>country gets the modifier loser_fed_religious_war until otherwise removed</li></ul><li>hidden effect:</li><ul><li>clr country flag [debug_fed_religious](../flags/debug_fed_religious.md)</li></ul></ul>

___
##The Usuper is finished!

###Available if:
<li>None of the following:</li><ul><li>religion is kalyin_worshippers</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>lake federation gain 10 points = yes</li><li>add stability = 3</li><li>add prestige = 50</li><li>country gets the modifier victor_fed_religious_war until otherwise removed</li><li>If every known country has country modifier is lake federation member, and does not have religion is kalyin worshippers:</li><ul><li>add prestige = 25</li><li>add stability = 1</li><li>lake federation gain 5 points = yes</li><li>If has religion is kodave followers:</li><ul><li>every owned province:</li><ul><li>change religion = kodave_followers</li></ul></ul><li>Else if has religion is yukel followers:</li><ul><li>every owned province:</li><ul><li>change religion = yukel_followers</li></ul></ul><li>Else if has religion is enuuk followers:</li><ul><li>every owned province:</li><ul><li>change religion = enuuk_followers</li></ul></ul><li>country gets the modifier victor_fed_religious_war until otherwise removed</li></ul><li>If every known country has country modifier is lake federation member, and  has religion is kalyin worshippers:</li><ul><li>If has country flag is [old_yukel](../flags/old_yukel.md):</li><ul><li>change religion = yukel_followers</li><li>every owned province:</li><ul><li>random:</li><ul><li>chance = 90</li><li>change religion = yukel_followers</li></ul></ul></ul><li>Else if has country flag is [old_enuuk](../flags/old_enuuk.md):</li><ul><li>change religion = enuuk_followers</li><li>every owned province:</li><ul><li>random:</li><ul><li>chance = 90</li><li>change religion = enuuk_followers</li></ul></ul></ul><li>Else if has country flag is [old_kodave](../flags/old_kodave.md):</li><ul><li>change religion = kodave_followers</li><li>every owned province:</li><ul><li>random:</li><ul><li>chance = 90</li><li>change religion = kodave_followers</li></ul></ul></ul><li>add stability = -1</li><li>add prestige = -25</li><li>lake federation lose 2 points = yes</li><li>country gets the modifier loser_fed_religious_war until otherwise removed</li></ul><li>hidden effect:</li><ul><li>clr country flag [debug_fed_religious](../flags/debug_fed_religious.md)</li></ul></ul>
