#Information
 - Title: Crossroad of Faiths
 - ID: flavour_reuyel.3
#Description
Crossroad of Faiths
#Mean Time to Happen:
Base time = 180 days

#Options

___
##The Jadd Know the Truth - let us invite Kamnaril and spread the faith.

###AI weighting:
AI weights this option at 0.33
 - Multiplied by 2 if has any enemy country has primary culture is sun elf


###Efects:<ul><li>define general:</li><ul><li>name = "Camnaril of the Sands"</li><li>shock = 5</li><li>fire = 2</li><li>manuever = 5</li><li>siege = 3</li><li>trait = hardy_warrior_personality</li></ul><li>set country flag [reuyel_jadd](../flags/reuyel_jadd.md)</li><li>If every country has religion is the jadd:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = the_jadd_converted_to_jadd</li></ul></ul><li>If every country has religion is bulwari sun cult:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulwari_converted_to_jadd</li></ul></ul><li>swap non generic missions = yes</li></ul>

___
##Let us join Dartaxâgerdim in rebelling against the lies of the elves.

###AI weighting:
AI weights this option at 0.33
 - Multiplied by 2 if has any enemy country has primary culture is sun elf
 - Multiplied by 2 if has any enemy country has primary culture is exodus goblin


###Efects:<ul><li>define advisor:</li><ul><li>type = theologian</li><li>name = "Sepeh of Kuzak"</li><li>skill = 2</li><li>discount = yes</li><li>culture = bahari</li><li>religion = old_bulwari_sun_cult</li></ul><li>set country flag [reuyel_osc](../flags/reuyel_osc.md)</li><li>If every country has religion is old bulwari sun cult:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = osc_converted_to_jadd</li></ul></ul><li>If every country has religion is bulwari sun cult:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulwari_converted_to_jadd</li></ul></ul><li>swap non generic missions = yes</li></ul>

___
##The truth remains the same. Jaher was Surael reborn and the elves are keepers of His light.

###AI weighting:
AI weights this option at 0.33
 - Multiplied by 2 if has any ally has primary culture is sun elf


###Efects:<ul><li>set country flag [reuyel_nsc](../flags/reuyel_nsc.md)</li><li>If every country has religion is bulwari sun cult:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = refused_conversion_to_jadd</li></ul></ul><li>swap non generic missions = yes</li></ul>
