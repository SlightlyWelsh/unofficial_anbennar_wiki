#Information
 - Title: Siege Magic\n£siege_magic_bg£
 - ID: magic_siege.1
#Description
Siege Magic\n£siege_magic_bg£
#Options

___
##£magic_button_close£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>highlight = yes</li><li>close single menu = yes</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>clr ruler flag [magic_siege_menu](../flags/magic_siege_menu.md)</li></ul>

___
##£spell_elemantal£

###Available if:
<li>has ruler flag [conjuration_1](../flags/conjuration_1.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have adm power is 20; and does not have dip power is 20; and does not have mil power is 20


###Efects:<ul><li>the event [Summon Siege Elemental](../events/summon_siege_elemental.md) happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_elemental_besieger</li><li>duration = 84</li></ul></ul><li>custom tooltip = magic_elemental_desc_tt</li></ul>

___
##£spell_elemantal_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [conjuration_1](../flags/conjuration_1.md)</li></ul>

###Efects:<ul><li>set country flag [siege_magic_menu](../flags/siege_magic_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_elemental_besieger</li><li>duration = 84</li></ul></ul><li>custom tooltip = magic_elemental_desc_tt</li></ul>

___
##£spell_fireball£

###Available if:
<li>has ruler flag [evocation_1](../flags/evocation_1.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have mil power is 10


###Efects:<ul><li>the event [Greater Fireball](../events/greater_fireball.md) happens</li><li>If has ruler flag is [rakshasa_patron](../flags/rakshasa_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 1</li></ul><li>custom tooltip = magic_fireball_desc_tt</li></ul>

___
##£spell_fireball_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [evocation_1](../flags/evocation_1.md)</li></ul>

###Efects:<ul><li>set country flag [siege_magic_menu](../flags/siege_magic_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 1</li></ul><li>custom tooltip = magic_fireball_desc_tt</li></ul>

___
##£spell_thunderstorm£

###Available if:
<li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have adm power is 20; and does not have dip power is 20; and does not have mil power is 20


###Efects:<ul><li>the event [Thunderstorm](../events/thunderstorm.md) happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 5</li><li>add devastation = 5</li><li>add province modifier:</li><ul><li>name = siege_magic_thunderstorm</li><li>duration = 182</li></ul></ul><li>custom tooltip = magic_thunderstorm_desc_tt</li></ul>

___
##£spell_thunderstorm_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li></ul>

###Efects:<ul><li>set country flag [siege_magic_menu](../flags/siege_magic_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 5</li><li>add devastation = 5</li><li>add province modifier:</li><ul><li>name = siege_magic_thunderstorm</li><li>duration = 182</li></ul></ul><li>custom tooltip = magic_thunderstorm_desc_tt</li></ul>

___
##£spell_earthquake£

###Available if:
<li>has ruler flag [evocation_2](../flags/evocation_2.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have adm power is 20; and does not have mil power is 5


###Efects:<ul><li>the event [Earthquake](../events/earthquake.md) happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 3</li><li>add province modifier:</li><ul><li>name = siege_magic_earthquake</li><li>duration = 365</li></ul><li>add devastation = 10</li></ul><li>custom tooltip = magic_earthquake_desc_tt</li></ul>

___
##£spell_earthquake_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li></ul>

###Efects:<ul><li>set country flag [siege_magic_menu](../flags/siege_magic_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 3</li><li>add province modifier:</li><ul><li>name = siege_magic_earthquake</li><li>duration = 365</li></ul><li>add devastation = 10</li></ul><li>custom tooltip = magic_earthquake_desc_tt</li></ul>

___
##£spell_giant£

###Available if:
<li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has current age is age of revolutions


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 5</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_giant_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>the event [Shapechange into Giant](../events/shapechange_into_giant.md) happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_giant_desc_tt</li></ul>

___
##£spell_giant_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li></ul>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 5</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_giant_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>set country flag [siege_magic_menu](../flags/siege_magic_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_giant_desc_tt</li></ul>

___
##£spell_dominate_surrender£

###Available if:
<li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have adm power is 20; and does not have dip power is 20


###Efects:<ul><li>the event [Dominate to Surrender](../events/dominate_to_surrender.md) happens</li><li>If has ruler flag is [baku_patron](../flags/baku_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change controller = ROOT</li></ul><li>custom tooltip = magic_dominate_desc_tt</li></ul>

___
##£spell_dominate_surrender_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>set country flag [siege_magic_menu](../flags/siege_magic_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change controller = ROOT</li></ul><li>custom tooltip = magic_dominate_desc_tt</li></ul>

___
##£spell_meteor£

###Available if:
<li>Any of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li><li>has ruler flag  rakshasa_patron</li></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have mil power is 50


###Efects:<ul><li>the event [Meteor Strike](../events/meteor_strike.md) happens</li><li>If has ruler flag is [rakshasa_patron](../flags/rakshasa_patron.md), and does not have ruler flag is [evocation_3](../flags/evocation_3.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 10</li><li>add devastation = 50</li></ul><li>custom tooltip = magic_meteor_desc_tt</li></ul>

___
##£spell_meteor_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul><li>NOT:</li><ul><li>All of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li><li>has ruler flag  rakshasa_patron</li></ul></ul>

###Efects:<ul><li>set country flag [siege_magic_menu](../flags/siege_magic_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 10</li><li>add devastation = 50</li></ul><li>custom tooltip = magic_meteor_desc_tt</li></ul>

___
##£spell_dragon£

###Available if:
<li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li>

###AI weighting:
AI weights this option at 50


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 10</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_dragon_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>the event [Shapechange into Dragon](../events/shapechange_into_dragon.md) happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_dragon_desc_tt</li></ul>

___
##£spell_dragon_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 10</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_dragon_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>set country flag [siege_magic_menu](../flags/siege_magic_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_dragon_desc_tt</li></ul>
