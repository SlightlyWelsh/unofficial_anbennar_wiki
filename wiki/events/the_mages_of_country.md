#Information
 - Title: The Mages of $COUNTRY$
 - ID: estate_organization.1
#Description
The Mages of $COUNTRY$
#Options

___
##Welcome the Magical Guilds.

###Available if:
<li>is not part of hre</li><li>None of the following:</li><ul><li>Country is Magisterium</li></ul>

###AI weighting:
AI weights this option at 34


###Efects:<ul><li>set estate privilege = estate_mages_organization_guilds</li></ul>

___
##Centralize the Mages under the state.

###Available if:
<li>adm tech is at least 12</li><li>None of the following:</li><ul><li>Country is Magisterium</li></ul>

###AI weighting:
AI weights this option at 33
 - Multiplied by 10 if has current age is age of absolutism, and does not have part of hre


###Efects:<ul><li>set estate privilege = estate_mages_organization_state</li></ul>

___
##Invite the Magisterium.

###Available if:
<li>Any of the following:</li><ul><li>is part of hre</li><li>if:</li><ul><li>limit:</li><ul><li>exists is Magisterium</li></ul><li>A85:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 100</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 33
 - Multiplied by 100 if is part of hre


###Efects:<ul><li>set estate privilege = estate_mages_organization_magisterium</li></ul>

___
##The [Root.GetClergyName] will oversee the Mages.

###Available if:
<li>Any of the following:</li><ul><li>religion is ravelian</li><li>religion  is the_jadd</li><li>religion   is bulwari_sun_cult</li><li>religion    is old_bulwari_sun_cult</li><li>religion     is xhazobkult</li><li>religion      is skaldhyrric_faith</li></ul><li>None of the following:</li><ul><li>Country is Magisterium</li></ul>

###AI weighting:
AI weights this option at 33
 - Multiplied by 100 if has religion is ravelian, and has religion is the jadd, and has religion is bulwari sun cult, and has religion is old bulwari sun cult, and has religion is xhazobkult, and has religion is skaldhyrric faith


###Efects:<ul><li>set estate privilege = estate_mages_organization_religious</li></ul>

___
##Mages are banned here!

###Available if:
<li>religion is ravelian</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>set country flag [banned_magic](../flags/banned_magic.md)</li></ul>
