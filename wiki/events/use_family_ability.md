#Information
 - Title: Use Family Ability
 - ID: flavour_bulwar_tag.25
#Description
Use Family Ability
#Options

___
##Ruqašah ability: Launch an archaeological expedition.

###Available if:
<li>601:</li><ul><li>check variable:</li><ul><li>which is ruqasah_power_progress</li><li>value is at least 100</li></ul></ul>

###Efects:<ul><li>tooltip:</li><ul><li>the event [Missing localisation: flavour_bulwar_tag_27_t](../events/missing_localisation_flavour_bulwar_tag_27_t.md) happens</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: flavour_bulwar_tag_27_t](../events/missing_localisation_flavour_bulwar_tag_27_t.md) happens</li><li>601:</li><ul><li>set variable:</li><ul><li>which = ruqasah_power_progress</li><li>value = 0</li></ul></ul></ul></ul>

___
##§gRuqašah ability: Launch an archaeological expedition.§!

###Available if:
<li>601:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is ruqasah_power_progress</li><li>value is at least 100</li></ul></ul></ul>

###Efects:<ul><li>tooltip:</li><ul><li>the event [Missing localisation: flavour_bulwar_tag_27_t](../events/missing_localisation_flavour_bulwar_tag_27_t.md) happens</li></ul><li>hidden effect:</li><ul><li>the event [Use Family Ability](../events/use_family_ability_1.md) happens</li></ul></ul>

___
##Huš-Nekar ability: Increase our influence over a country.

###Available if:
<li>601:</li><ul><li>check variable:</li><ul><li>which is husnekar_power_progress</li><li>value is at least 100</li></ul></ul>

###Efects:<ul><li>country gets the modifier bulwar_husnekar_ability for 5 years</li><li>hidden effect:</li><ul><li>601:</li><ul><li>set variable:</li><ul><li>which = husnekar_power_progress</li><li>value = 0</li></ul></ul></ul></ul>

___
##§gHuš-Nekar ability: Increase our influence over a country.§!

###Available if:
<li>601:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is husnekar_power_progress</li><li>value is at least 100</li></ul></ul></ul>

###Efects:<ul><li>tooltip:</li><ul><li>country gets the modifier bulwar_husnekar_ability for 5 years</li></ul><li>hidden effect:</li><ul><li>the event [Use Family Ability](../events/use_family_ability_1.md) happens</li></ul></ul>

___
##szal-Lekad ability: Launch a recruitment campaign.

###Available if:
<li>601:</li><ul><li>check variable:</li><ul><li>which is lekad_power_progress</li><li>value is at least 100</li></ul></ul>

###Efects:<ul><li>capital scope:</li><ul><li>build to forcelimit:</li><ul><li>infantry = 0.09</li><li>cavalry = 0.01</li></ul></ul><li>hidden effect:</li><ul><li>601:</li><ul><li>set variable:</li><ul><li>which = lekad_power_progress</li><li>value = 0</li></ul></ul></ul></ul>

___
##§gszal-Lekad ability: Launch a recruitment campaign.§!

###Available if:
<li>601:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is lekad_power_progress</li><li>value is at least 100</li></ul></ul></ul>

###Efects:<ul><li>tooltip:</li><ul><li>capital scope:</li><ul><li>build to forcelimit:</li><ul><li>infantry = 0.09</li><li>cavalry = 0.01</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Use Family Ability](../events/use_family_ability_1.md) happens</li></ul></ul>

___
##Belatis ability: Research Unconventional Practices.

###Available if:
<li>601:</li><ul><li>check variable:</li><ul><li>which is belatis_power_progress</li><li>value is at least 100</li></ul></ul>

###Efects:<ul><li>change government reform progress = 50</li><li>hidden effect:</li><ul><li>601:</li><ul><li>set variable:</li><ul><li>which = belatis_power_progress</li><li>value = 0</li></ul></ul></ul></ul>

___
##§gBelatis ability: Research Unconventional Practices.§!

###Available if:
<li>601:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is belatis_power_progress</li><li>value is at least 100</li></ul></ul></ul>

###Efects:<ul><li>tooltip:</li><ul><li>change government reform progress = 50</li></ul><li>hidden effect:</li><ul><li>the event [Use Family Ability](../events/use_family_ability_1.md) happens</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [use_family_ability_1](use_family_ability_1.md)
