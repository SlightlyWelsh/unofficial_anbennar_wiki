This page has the same name as others. For full listing see bottom of [the base page](heir_needed_in_country.md).

#Information
 - Title: Heir needed in $COUNTRY$
 - ID: magocracy.1
#Description
Heir needed in $COUNTRY$
#Options

___
##A Gifted Academic

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>set heir mage effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul></ul>

###Efects:<ul><li>goto = gifted_academic_province</li><li>set country flag [mago_gifted_academic_flag](../flags/mago_gifted_academic_flag.md)</li><li>If has saved event target is gifted academic province, and has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>culture = event_target:gifted_academic_province</li><li>change adm = 2</li><li>female = yes</li></ul></ul><li>Else if has saved event target is gifted academic province:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>culture = event_target:gifted_academic_province</li><li>change adm = 2</li></ul></ul><li>Else if has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>change adm = 2</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>change adm = 2</li></ul></ul><li>add adm power = 20</li><li>add dip power = 20</li><li>add mil power = 20</li><li>clr country flag [in_magocracy_heir_selection](../flags/in_magocracy_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A Charismatic Sorcerer

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>set heir mage effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul></ul>

###Efects:<ul><li>goto = charismatic_sorcerer_province</li><li>set country flag [mago_talented_sorcerer_flag](../flags/mago_talented_sorcerer_flag.md)</li><li>If has saved event target is charismatic sorcerer province, and has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>culture = event_target:charismatic_sorcerer_province</li><li>change dip = 2</li><li>female = yes</li></ul></ul><li>Else if has saved event target is charismatic sorcerer province:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>culture = event_target:charismatic_sorcerer_province</li><li>change dip = 2</li></ul></ul><li>Else if has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>change dip = 2</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>change dip = 2</li></ul></ul><li>add devotion = 10</li><li>clr country flag [in_magocracy_heir_selection](../flags/in_magocracy_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A Noble Scion

###Available if:
<li>any neighbor country:</li><ul><li>government is monarchy</li><li>does not have regency</li><li>religion is this nation</li></ul>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>set heir mage effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul></ul>

###Efects:<ul><li>add estate nobles loyalty effect = yes</li><li>reduce estate mages loyalty effect = yes</li><li>set country flag [mago_noble_scion_flag](../flags/mago_noble_scion_flag.md)</li><li>If random neighbor country has government is monarchy, and  does not have regency, and  has religion is ROOT:</li><ul><li>ROOT:</li><ul><li>If has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>dynasty = PREV</li><li>age = 55</li><li>culture = PREV</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>define heir:</li><ul><li>dynasty = PREV</li><li>age = 55</li><li>culture = PREV</li><li>hidden = yes</li></ul></ul></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_magocracy_noble</li></ul></ul><li>clr country flag [in_magocracy_heir_selection](../flags/in_magocracy_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A prominent member of the $ESTATE_MAGES$ Estate

###Available if:
<li>has estate estate_mages</li>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>set heir mage effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul></ul>

###Efects:<ul><li>goto = estate_heir_province</li><li>If has estate is estate mages:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_HEIR_SELECTED_MAGE_ESTATE_MEMBER</li><li>loyalty = 10</li><li>duration = 3650</li></ul></ul><li>set country flag [mago_prominent_estate_member_flag](../flags/mago_prominent_estate_member_flag.md)</li><li>If has saved event target is estate heir province, and has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>culture = event_target:estate_heir_province</li><li>female = yes</li></ul></ul><li>Else if has saved event target is estate heir province:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>culture = event_target:estate_heir_province</li></ul></ul><li>Else if has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>define heir:</li><ul><li>age = 55</li><li>hidden = yes</li></ul></ul><li>add devotion = -5</li><li>clr country flag [in_magocracy_heir_selection](../flags/in_magocracy_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li></ul>

___
##A inexperienced but Powerful Mage

###Available if:
<li>has estate estate_mages</li>

###Efects:<ul><li>goto = estate_heir_province</li><li>set country flag [mago_young_mage_flag](../flags/mago_young_mage_flag.md)</li><li>If has saved event target is estate heir province, and has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>max random adm = 3</li><li>max random dip = 3</li><li>max random mil = 3</li><li>hidden = yes</li><li>culture = event_target:estate_heir_province</li><li>female = yes</li></ul></ul><li>Else if has saved event target is estate heir province:</li><ul><li>define heir:</li><ul><li>age = 30</li><li>max random adm = 3</li><li>max random dip = 3</li><li>max random mil = 3</li><li>hidden = yes</li><li>culture = event_target:estate_heir_province</li></ul></ul><li>Else if has culture group is harpy, and has culture group is gnollish:</li><ul><li>define heir:</li><ul><li>age = 40</li><li>max random adm = 3</li><li>max random dip = 3</li><li>max random mil = 3</li><li>hidden = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>define heir:</li><ul><li>age = 40</li><li>max random adm = 3</li><li>max random dip = 3</li><li>max random mil = 3</li><li>hidden = yes</li></ul></ul><li>add devotion = -5</li><li>clr country flag [in_magocracy_heir_selection](../flags/in_magocracy_heir_selection.md)</li><li>custom tooltip = theocracy.1.tt</li><li>set heir mage effect = yes</li></ul>
