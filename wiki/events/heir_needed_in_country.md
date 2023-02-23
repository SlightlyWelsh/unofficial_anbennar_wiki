#Information
 - Title: Heir needed in $COUNTRY$
 - ID: adventurer.1
#Description
Heir needed in $COUNTRY$
#Options

___
##A Skilled Adventurer Captain

###Efects:<ul><li>set country flag [adv_adventure_captain_flag](../flags/adv_adventure_captain_flag.md)</li><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul><li>add militarised society = 5</li><li>clr country flag [in_adventurer_heir_selection](../flags/in_adventurer_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A Powerful Marcher

###Efects:<ul><li>set country flag [adv_marcher_flag](../flags/adv_marcher_flag.md)</li><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul><li>add faction influence:</li><ul><li>faction = adv_marchers</li><li>influence = 10</li></ul><li>add militarised society = -5</li><li>clr country flag [in_adventurer_heir_selection](../flags/in_adventurer_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A Charismatic Pioneer

###Efects:<ul><li>set country flag [adv_pioneer_flag](../flags/adv_pioneer_flag.md)</li><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul><li>add faction influence:</li><ul><li>faction = adv_pioneers</li><li>influence = 10</li></ul><li>add militarised society = -5</li><li>clr country flag [in_adventurer_heir_selection](../flags/in_adventurer_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A Shrewd Fortune-Seeker

###Efects:<ul><li>set country flag [adv_fortune_seeker_flag](../flags/adv_fortune_seeker_flag.md)</li><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul><li>add faction influence:</li><ul><li>faction = adv_fortune_seekers</li><li>influence = 10</li></ul><li>add militarised society = -5</li><li>clr country flag [in_adventurer_heir_selection](../flags/in_adventurer_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A Lilac Wars Veteran

###Available if:
<li>None of the following:</li><ul><li>is year is at least 1480</li></ul><li>NOT:</li><ul><li>has reform dwarovar_adventurer_reform</li></ul>

###Efects:<ul><li>set country flag [adv_lilac_wars_veteran_flag](../flags/adv_lilac_wars_veteran_flag.md)</li><li>hidden effect:</li><ul><li>If does not have year is 1450:</li><ul><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>change mil = 4</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>change mil = 4</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>change mil = 4</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul></ul><li>Else if does not have year is 1460:</li><ul><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 40</li><li>change mil = 4</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 40</li><li>change mil = 4</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 40</li><li>change mil = 4</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul></ul><li>Else if does not have year is 1470:</li><ul><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 50</li><li>change mil = 4</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 50</li><li>change mil = 4</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 50</li><li>change mil = 4</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul></ul><li>else:</li><ul><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 60</li><li>change mil = 4</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 60</li><li>change mil = 4</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 60</li><li>change mil = 4</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul></ul></ul><li>If does not have year is 1450:</li><ul><li>custom tooltip = marcher.1.tt</li></ul><li>Else if does not have year is 1460:</li><ul><li>custom tooltip = marcher.1.tt2</li></ul><li>Else if does not have year is 1470:</li><ul><li>custom tooltip = marcher.1.tt3</li></ul><li>else:</li><ul><li>custom tooltip = marcher.1.tt4</li></ul><li>add militarised society = -5</li><li>clr country flag [in_adventurer_heir_selection](../flags/in_adventurer_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A Noble from our Homeland

###Available if:
<li>any country:</li><ul><li>government is monarchy</li><li>religion is this nation</li><li>primary culture is this nation</li><li>capital scope:</li><ul><li>None of the following:</li><ul><li>continent is north_america</li></ul><li>NOT:</li><ul><li>continent is south_america</li></ul><li>NOT:</li><ul><li>continent is serpentspine</li></ul><li>NOT:</li><ul><li>region is west_castanor_region</li></ul><li>NOT:</li><ul><li>region is inner_castanor_region</li></ul><li>NOT:</li><ul><li>region is south_castanor_region</li></ul></ul></ul>

###Efects:<ul><li>set country flag [adv_noble_flag](../flags/adv_noble_flag.md)</li><li>If random country has government is monarchy, and  has religion is ROOT, and  has primary culture is ROOT, and  does not have continent is north america; and does not have continent is south america; and does not have continent is serpentspine; and does not have region is west castanor region; and does not have region is inner castanor region; and does not have region is south castanor region:</li><ul><li>ROOT:</li><ul><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>dynasty = PREV</li><li>age = 30</li><li>culture = PREV</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>dynasty = PREV</li><li>age = 30</li><li>culture = PREV</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>dynasty = PREV</li><li>age = 30</li><li>culture = PREV</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_theocracy_noble</li></ul></ul><li>add prestige = 10</li><li>add militarised society = -5</li><li>clr country flag [in_adventurer_heir_selection](../flags/in_adventurer_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A Native Escanni

###Available if:
<li>capital scope:</li><ul><li>superregion is escann_superregion</li></ul>

###Efects:<ul><li>set country flag [adv_escanni_native_flag](../flags/adv_escanni_native_flag.md)</li><li>If has capital scope has region is inner castanor region:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>culture = castellyrian</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>female = yes</li><li>culture = castellyrian</li></ul></ul></ul></ul><li>Else if has capital scope has region is west castanor region:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>culture = adenner</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>female = yes</li><li>culture = adenner</li></ul></ul></ul></ul><li>Else if has capital scope has region is south castanor region:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>culture = marcher</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>female = yes</li><li>culture = marcher</li></ul></ul></ul></ul><li>add yearly manpower = 2</li><li>add militarised society = -5</li><li>clr country flag [in_adventurer_heir_selection](../flags/in_adventurer_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A Powerful Mage

###Available if:
<li>Any of the following:</li><ul><li>Country is Order of the Iron Sceptre</li><li>tag  is Sword Covenant</li><li>prestige is at least 50</li></ul>

###Efects:<ul><li>set country flag [adv_mage_flag](../flags/adv_mage_flag.md)</li><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>hidden = yes</li></ul></ul><li>30:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>female = yes</li><li>hidden = yes</li></ul></ul></ul></ul><li>set heir mage effect = yes</li><li>add militarised society = -10</li><li>add prestige = -10</li><li>clr country flag [in_adventurer_heir_selection](../flags/in_adventurer_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [heir_needed_in_country_1](heir_needed_in_country_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [heir_needed_in_country_1](heir_needed_in_country_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [heir_needed_in_country_1](heir_needed_in_country_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [heir_needed_in_country_1](heir_needed_in_country_1.md)
