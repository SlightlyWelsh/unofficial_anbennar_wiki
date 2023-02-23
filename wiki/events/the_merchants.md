#Information
 - Title: The Merchants
 - ID: flavor_krak.53
#Description
The Merchants
#Options

___
##We do not need their help reforming as there won't be a republic to reform.

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>krak add clan monarchy support = yes</li><li>reduce stability or adm power = yes</li><li>If random owned province has province has center of trade of level is 1:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 0.75</li></ul></ul><li>If random owned province has province has center of trade of level is 1:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 0.75</li></ul></ul><li>If random owned province has province has center of trade of level is 1:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 0.75</li></ul></ul></ul>

___
##Their help in this process would be greatly appreciated.

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>krak add clan republic support = yes</li><li>If does not have calc true if has amount is 5, and calc true if has estate privilege is estate burghers land rights, and calc true if has estate privilege is estate burghers land of commerce, and calc true if has estate privilege is estate burghers free enterprise, and calc true if has estate privilege is estate burghers patronage of the arts, and calc true if has estate privilege is estate burghers control over monetary policy, and calc true if has estate privilege is estate burghers commercial board of advice:</li><ul><li>custom tooltip = flavor_krak.53.tooltip</li><li>hidden effect:</li><ul><li>set variable:</li><ul><li>which = temp_privilege_counter</li><li>value = 2</li></ul><li>If while has check variable has which is temp privilege counter, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = temp_privilege_counter</li><li>value = -1</li></ul><li>If does not have estate privilege is estate burghers patronage of the arts:</li><ul><li>set estate privilege = estate_burghers_patronage_of_the_arts</li></ul><li>Else if does not have estate privilege is estate burghers commercial board of advice:</li><ul><li>set estate privilege = estate_burghers_commercial_board_of_advice</li></ul><li>Else if does not have estate privilege is estate burghers free enterprise:</li><ul><li>set estate privilege = estate_burghers_free_enterprise</li></ul><li>Else if does not have estate privilege is estate burghers control over monetary policy:</li><ul><li>set estate privilege = estate_burghers_control_over_monetary_policy</li></ul><li>Else if does not have estate privilege is estate burghers land of commerce:</li><ul><li>set estate privilege = estate_burghers_land_of_commerce</li></ul><li>Else if does not have estate privilege is estate burghers land rights:</li><ul><li>set estate privilege = estate_burghers_land_rights</li></ul></ul></ul></ul><li>else:</li><ul><li>add dip power = -300</li></ul><li>add disaster modifier:</li><ul><li>name = krak_merchant_support</li><li>duration = -1</li><li>disaster = krakdhumvror_borduz_az_stun</li></ul></ul>
