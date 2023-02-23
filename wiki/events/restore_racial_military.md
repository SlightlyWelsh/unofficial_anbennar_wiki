#Information
 - Title: Restore Racial Military
 - ID: racial_modifiers.6
#Description
Restore Racial Military
#Options

___
##[Root.Get1stMil]

###Available if:
<li>has country modifier orcish_military</li><li>None of the following:</li><ul><li>unit type is tech_orcish</li></ul><li>NOT:</li><ul><li>unit type is tech_east_orcish</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has capital scope has continent is asia, and does not have superregion is forbidden lands superregion; and has primary culture is brown orc, and has AND has accepted culture is brown orc, and does not have culture group is orcish:</li><ul><li>change unit type = tech_east_orcish</li></ul><li>else:</li><ul><li>change unit type = tech_orcish</li></ul></ul>

___
##[Root.Get2ndMil]

###Available if:
<li>has country modifier human_military</li><li>None of the following:</li><ul><li>unit type is tech_bulwari</li></ul><li>NOT:</li><ul><li>unit type is tech_salahadesi</li></ul><li>NOT:</li><ul><li>unit type is tech_cannorian</li></ul><li>NOT:</li><ul><li>unit type is tech_gerudian</li></ul><li>NOT:</li><ul><li>unit type is tech_raheni</li></ul><li>NOT:</li><ul><li>unit type is tech_halessi</li></ul><li>NOT:</li><ul><li>unit type is tech_islanders</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has capital scope has superregion is bulwar superregion:</li><ul><li>change unit type = tech_bulwari</li></ul><li>Else if has capital scope has superregion is salahad superregion:</li><ul><li>change unit type = tech_salahadesi</li></ul><li>Else if has capital scope has superregion is rahen superregion:</li><ul><li>change unit type = tech_raheni</li></ul><li>Else if has capital scope has superregion is yanshen superregion; and has capital scope has superregion is south haless superregion:</li><ul><li>change unit type = tech_halessi</li></ul><li>Else if has capital scope has superregion is forbidden lands superregion:</li><ul><li>change unit type = tech_islanders</li></ul><li>Else if has capital scope has superregion is gerudia superregion:</li><ul><li>change unit type = tech_gerudian</li></ul><li>else:</li><ul><li>change unit type = tech_cannorian</li></ul></ul>

___
##[Root.Get3rdMil]

###Available if:
<li>has country modifier elven_military</li><li>None of the following:</li><ul><li>unit type is tech_wood_elf</li></ul><li>NOT:</li><ul><li>unit type is tech_elven</li></ul><li>NOT:</li><ul><li>unit type is tech_east_elven</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has capital scope has superregion is deepwoods superregion; and has primary culture is wood elf, and has AND has accepted culture is wood elf, and does not have culture group is elven:</li><ul><li>change unit type = tech_wood_elf</li></ul><li>Else if has capital scope has continent is asia; and has capital scope has continent is africa; and has capital scope has continent is north america; and has capital scope has continent is south america; and AND has religion group is bulwari; and has primary culture is sun elf, and has primary culture is dawn elf, and has primary culture is desert elf, and has primary culture is sunrise elf, and has AND has accepted culture is sun elf, and does not have culture group is elven; and has AND has accepted culture is dawn elf, and does not have culture group is elven; and has AND has accepted culture is desert elf, and does not have culture group is elven; and has AND has accepted culture is sunrise elf, and does not have culture group is elven:</li><ul><li>change unit type = tech_east_elven</li></ul><li>else:</li><ul><li>change unit type = tech_elven</li></ul></ul>

___
##[Root.Get4thMil]

###Available if:
<li>has country flag [disabled](../flags/disabled.md)</li>

###AI weighting:
AI weights this option at 100


___
##[Root.Get5thMil]

###Available if:
<li>has country modifier half_orcish_military</li><li>None of the following:</li><ul><li>unit type is tech_cannorian</li></ul><li>NOT:</li><ul><li>unit type is tech_gerudian</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has capital scope has superregion is gerudia superregion; and has primary culture is grombar half orc, and has primary culture is grombar orc, and has primary culture is gray orc, and has AND has accepted culture is grombar half orc, and does not have culture is half orcish is yes; and has AND has accepted culture is grombar orc, and does not have culture is half orcish is yes; and has AND has accepted culture is gray orc, and does not have culture is half orcish is yes:</li><ul><li>change unit type = tech_gerudian</li></ul><li>else:</li><ul><li>change unit type = tech_cannorian</li></ul></ul>

___
##[Root.Get6thMil]

###Available if:
<li>has country modifier troll_military</li><li>None of the following:</li><ul><li>unit type is tech_troll</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change unit type = tech_troll</li></ul>

___
##[Root.Get7thMil]

###Available if:
<li>has country modifier gnollish_military</li><li>None of the following:</li><ul><li>unit type is tech_gnollish</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change unit type = tech_gnollish</li><li>If is not tribal:</li><ul><li>set country flag [gnoll_reformed_mil_flag](../flags/gnoll_reformed_mil_flag.md)</li></ul></ul>

___
##[Root.Get8thMil]

###Available if:
<li>has country modifier goblin_military</li><li>None of the following:</li><ul><li>unit type is tech_goblin</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change unit type = tech_goblin</li></ul>

___
##[Root.Get9thMil]

###Available if:
<li>has country modifier gnomish_military</li><li>None of the following:</li><ul><li>unit type is tech_gnomish</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change unit type = tech_gnomish</li></ul>

___
##[Root.Get10thMil]

###Available if:
<li>has country modifier dwarven_military</li><li>None of the following:</li><ul><li>unit type is tech_dwarven</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change unit type = tech_dwarven</li></ul>

___
##[Root.Get11thMil]

###Available if:
<li>has country modifier kobold_military</li><li>None of the following:</li><ul><li>unit type is tech_kobold</li></ul><li>NOT:</li><ul><li>unit type is tech_east_kobold</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has capital scope has superregion is yanshen superregion; and has capital scope has superregion is south haless superregion; and has capital scope has superregion is rahen superregion:</li><ul><li>change unit type = tech_east_kobold</li></ul><li>else:</li><ul><li>change unit type = tech_kobold</li></ul></ul>

___
##[Root.Get12thMil]

###Available if:
<li>has country modifier ruinborn_military</li><li>None of the following:</li><ul><li>unit type is tech_ynnic</li></ul><li>NOT:</li><ul><li>unit type is tech_eordand</li></ul><li>NOT:</li><ul><li>unit type is tech_kheionai</li></ul><li>NOT:</li><ul><li>unit type is tech_taychendi</li></ul><li>NOT:</li><ul><li>unit type is tech_north_aelantiri</li></ul><li>NOT:</li><ul><li>unit type is tech_south_aelantiri</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has capital scope has superregion is ynn superregion:</li><ul><li>change unit type = tech_ynnic</li></ul><li>Else if has capital scope has superregion is eordand superregion:</li><ul><li>change unit type = tech_eordand</li></ul><li>Else if has capital scope has superregion is kheionai superregion:</li><ul><li>change unit type = tech_kheionai</li></ul><li>Else if has capital scope has superregion is greater taychend superregion:</li><ul><li>change unit type = tech_taychendi</li></ul><li>Else if has capital scope has superregion is north aelantir superregion; and has capital scope has superregion is ruined sea superregion; and has capital scope has superregion is torn sea superregion:</li><ul><li>change unit type = tech_north_aelantiri</li></ul><li>Else if has capital scope has superregion is south aelantir superregion; and has capital scope has superregion is effelai superregion:</li><ul><li>change unit type = tech_south_aelantiri</li></ul><li>else:</li><ul><li>change unit type = tech_north_aelantiri</li></ul></ul>

___
##[Root.Get13thMil]

###Available if:
<li>has country modifier harpy_military</li><li>None of the following:</li><ul><li>unit type is tech_harpy</li></ul><li>NOT:</li><ul><li>unit type is tech_east_harpy</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has capital scope has superregion is yanshen superregion; and has capital scope has superregion is south haless superregion:</li><ul><li>change unit type = tech_east_harpy</li></ul><li>else:</li><ul><li>change unit type = tech_harpy</li></ul></ul>

___
##[Root.Get14thMil]

###Available if:
<li>has country modifier halfling_military</li><li>None of the following:</li><ul><li>unit type is tech_halfling</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change unit type = tech_halfling</li></ul>

___
##[Root.Get15thMil]

###Available if:
<li>has country modifier ogre_military</li><li>None of the following:</li><ul><li>unit type is tech_ogre</li></ul><li>NOT:</li><ul><li>unit type is tech_eastern_ogre</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has capital scope has superregion is yanshen superregion; and has capital scope has superregion is south haless superregion; and has capital scope has superregion is rahen superregion:</li><ul><li>change unit type = tech_eastern_ogre</li></ul><li>else:</li><ul><li>change unit type = tech_ogre</li></ul></ul>

___
##[Root.Get16thMil]

###Available if:
<li>has country modifier centaur_military</li><li>None of the following:</li><ul><li>unit type is tech_centaur</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change unit type = tech_centaur</li></ul>

___
##[Root.Get17thMil]

###Available if:
<li>has country modifier harimari_military</li><li>None of the following:</li><ul><li>unit type is tech_harimari</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change unit type = tech_harimari</li></ul>

___
##[Root.Get18thMil]

###Available if:
<li>has country modifier hobgoblin_military</li><li>None of the following:</li><ul><li>unit type is tech_hobgoblin</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change unit type = tech_hobgoblin</li></ul>
