#Information
 - Title: Forced Marriage
 - ID: flavor_grombar.15
#Description
Forced Marriage
#Options

___
##Begin the wedding preparations.

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has opinion has who is Z18, and has opinion has value is 100
 - Multiplied by 0.5 if does not have opinion has who is Z18, and has opinion has value is 0
 - Multiplied by 4 if has truce with is Z18


###Efects:<ul><li>If has consort:</li><ul><li>remove consort = yes</li></ul><li>If has heir:</li><ul><li>remove heir:</li><ul></ul></ul><li>capital scope:</li><ul><li>add orcish minority size effect = yes</li><li>ROOT:</li><ul><li>largest increase of orcish tolerance effect = yes</li></ul></ul><li>define consort:</li><ul><li>country of origin = Z18</li><li>religion = old_dookan</li><li>culture = gray_orc</li></ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>religion = old_dookan</li><li>change mil = 2</li></ul><li>set heir culture = half_orc</li><li>set heir flag [set_heir_race](../flags/set_heir_race.md)</li><li>largest increase of orcish tolerance effect = yes</li><li>hidden effect:</li><ul><li>set country flag [frozenmaw_reachman_vassal](../flags/frozenmaw_reachman_vassal.md)</li></ul></ul>

___
##I refuse!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has opinion has who is Z18, and has opinion has value is 100
 - Multiplied by 2 if does not have opinion has who is Z18, and has opinion has value is 0
 - Multiplied by 0.75 if has truce with is Z18


###Efects:<ul><li>add liberty desire = 10</li></ul>
