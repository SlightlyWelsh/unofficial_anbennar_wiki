#Information
 - Title: The Artificers of $COUNTRY$
 - ID: estate_organization.5
#Description
The Artificers of $COUNTRY$
#Options

___
##Independent artificer unions.

###Available if:
<li>None of the following:</li><ul><li>All of the following:</li><ul><li>has country flag [nsc_sun_elf_artificery](../flags/nsc_sun_elf_artificery.md)</li><li>religion is bulwari_sun_cult</li></ul></ul><li>NOT:</li><ul><li>has estate estate_dragon_command</li></ul>

###AI weighting:
AI weights this option at 34


###Efects:<ul><li>set estate privilege = estate_artificers_organization_independent_unions</li></ul>

___
##State controlled artificers.

###Available if:
<li>Any of the following:</li><ul><li>adm tech is at least 12</li><li>has estate estate_dragon_command</li></ul><li>None of the following:</li><ul><li>All of the following:</li><ul><li>has country flag [nsc_sun_elf_artificery](../flags/nsc_sun_elf_artificery.md)</li><li>religion is bulwari_sun_cult</li></ul></ul>

###AI weighting:
AI weights this option at 33
 - Multiplied by 10 if has current age is age of absolutism


###Efects:<ul><li>set estate privilege = estate_artificers_organization_state</li></ul>

___
##Invite the International Gommo.

###Available if:
<li>None of the following:</li><ul><li>All of the following:</li><ul><li>has country flag [nsc_sun_elf_artificery](../flags/nsc_sun_elf_artificery.md)</li><li>religion is bulwari_sun_cult</li></ul></ul><li>NOT:</li><ul><li>has estate estate_dragon_command</li></ul>

###AI weighting:
AI weights this option at 33


###Efects:<ul><li>set estate privilege = estate_artificers_organization_international_gommo</li></ul>

___
##The Ravelian Church will oversee them.

###Available if:
<li>religion is ravelian</li><li>None of the following:</li><ul><li>has estate estate_dragon_command</li></ul>

###AI weighting:
AI weights this option at 33
 - Multiplied by 100 if has religion is ravelian


###Efects:<ul><li>set estate privilege = estate_artificers_organization_ravelian_control</li></ul>

___
##The Chosen will oversee artificery.

###Available if:
<li>has country flag [nsc_sun_elf_artificery](../flags/nsc_sun_elf_artificery.md)</li><li>None of the following:</li><ul><li>has estate estate_dragon_command</li></ul>

###AI weighting:
AI weights this option at 33


###Efects:<ul><li>set estate privilege = estate_artificers_organization_sun_elf</li></ul>
