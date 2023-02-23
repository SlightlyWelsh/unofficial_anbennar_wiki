#Information
 - Title: Independent $ESTATE_NOMADIC_TRIBES$
 - ID: tribal_estate_events.13
#Description
Independent $ESTATE_NOMADIC_TRIBES$
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We must leave them alone then.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>custom tooltip = tribal_estate_events.13.a.tt</li><li>hidden effect:</li><ul><li>If while does not have development in provinces has province flag is [add_autonomy_tmp_flag](../flags/add_autonomy_tmp_flag.md), and development in provinces has value is estate, and development in provinces has estate is estate nomadic tribes; and  does not have province flag is [add_autonomy_tmp_flag](../flags/add_autonomy_tmp_flag.md); and any owned province is not a capital, and any owned province is city:</li><ul><li>If random owned province does not have province flag is [add_autonomy_tmp_flag](../flags/add_autonomy_tmp_flag.md); and  is not a capital, and  is city:</li><ul><li>add local autonomy = 35</li><li>set province flag [add_autonomy_tmp_flag](../flags/add_autonomy_tmp_flag.md)</li></ul></ul></ul><li>add estate influence modifier:</li><ul><li>desc = EST_VAL_TRIBES_AUTONOMY</li><li>estate = estate_nomadic_tribes</li><li>influence = 10</li><li>duration = 3650</li></ul></ul>

___
##We can tolerate no states within our state!

###AI weighting:
AI weights this option at 99
 - Multiplied by 0.01 if does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 45


###Efects:<ul><li>add estate influence modifier:</li><ul><li>desc = EST_VAL_REFUSED_TRIBES_AUTONOMY</li><li>estate = estate_nomadic_tribes</li><li>influence = -10</li><li>duration = 3650</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nomadic_tribes</li><li>loyalty = -20</li></ul></ul>
