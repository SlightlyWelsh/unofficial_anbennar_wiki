#Information
 - Title: Capture of Elecast
 - ID: flavor_castanor.210
#Description
Capture of Elecast
#Options

___
##They will die for their insurrection.

###Efects:<ul><li>B61:</li><ul><li>kill leader:</li><ul><li>type = "Elecast, the Burnished Wing"</li></ul></ul><li>add prestige excess to splendour effect:</li><ul><li>VAL = 10</li></ul></ul>

___
##Offer them a chance to atone through service.

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 100
 - Multiplied by 5 if has check variable has which is battlesWonAgainstElecast, and check variable has value is 5

This outcome causes the following effects:<ul><li>define general:</li><ul><li>name = "Elecast, the Burnished Wing"</li><li>shock = 4</li><li>fire = 4</li><li>manuever = 4</li><li>siege = 2</li></ul><li>hidden effect:</li><ul><li>B61:</li><ul><li>kill leader:</li><ul><li>type = "Elecast, the Burnished Wing"</li></ul></ul></ul><li>set country flag [castanor_succession_war_elecast_defected](../flags/castanor_succession_war_elecast_defected.md)</li><li>castanor succession war increase castan legitimacy small = yes</li></ul>
Outcome 2:

The weight of this outcome is 100 
 - Multiplied by 5 if has country flag is [castanor_succession_war_erella_defected](../flags/castanor_succession_war_erella_defected.md)

The weight of this outcome is 100 
 - Multiplied by 5 if has country flag is [castanor_succession_war_elecast_defected](../flags/castanor_succession_war_elecast_defected.md)

The weight of this outcome is 100 
 - Multiplied by 5 if has country flag is [castanor_succession_war_gracos_defected](../flags/castanor_succession_war_gracos_defected.md)

This outcome causes the following effects:<ul><li>reduce stability or adm power = yes</li><li>B61:</li><ul><li>kill leader:</li><ul><li>type = "Elecast, the Burnished Wing"</li></ul></ul></ul>
