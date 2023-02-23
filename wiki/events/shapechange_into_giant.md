#Information
 - Title: Shapechange into Giant
 - ID: magic_siege.20
#Description
Shapechange into Giant
#Options

___
##Cast Shapechange

###AI weighting:
AI weights this option at 90
 - Multiplied by 0 if has current age is age of revolutions


###Efects:<ul><li>add adm power = -30</li><li>add dip power = -10</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_siege_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>If has event target:spell target province does not have mil tech is 7:</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>95:</li><ul><li>the event [Attack on [spell_target_province.GetName]](../events/attack_on_spell_target_province_getname.md) happens</li></ul><li>5:</li><ul><li>the event [The Bigger They Are...](../events/the_bigger_they_are.md) happens</li></ul></ul></ul></ul><li>If has event target:spell target province has owner has mil tech is 7, and does not have mil tech is 13:</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>90:</li><ul><li>the event [Attack on [spell_target_province.GetName]](../events/attack_on_spell_target_province_getname.md) happens</li></ul><li>10:</li><ul><li>the event [The Bigger They Are...](../events/the_bigger_they_are.md) happens</li></ul></ul></ul></ul><li>If has event target:spell target province has owner has mil tech is 13, and does not have mil tech is 18:</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>80:</li><ul><li>the event [Attack on [spell_target_province.GetName]](../events/attack_on_spell_target_province_getname.md) happens</li></ul><li>20:</li><ul><li>the event [The Bigger They Are...](../events/the_bigger_they_are.md) happens</li></ul></ul></ul></ul><li>If has event target:spell target province has owner has mil tech is 18, and does not have mil tech is 22:</li><ul><li>set country flag [spell_4](../flags/spell_4.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>the event [Attack on [spell_target_province.GetName]](../events/attack_on_spell_target_province_getname.md) happens</li></ul><li>30:</li><ul><li>the event [The Bigger They Are...](../events/the_bigger_they_are.md) happens</li></ul></ul></ul></ul><li>If has event target:spell target province has owner has mil tech is 22, and does not have mil tech is 29:</li><ul><li>set country flag [spell_5](../flags/spell_5.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>60:</li><ul><li>the event [Attack on [spell_target_province.GetName]](../events/attack_on_spell_target_province_getname.md) happens</li></ul><li>40:</li><ul><li>the event [The Bigger They Are...](../events/the_bigger_they_are.md) happens</li></ul></ul></ul></ul><li>If has event target:spell target province has owner has mil tech is 29:</li><ul><li>set country flag [spell_6](../flags/spell_6.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event [Attack on [spell_target_province.GetName]](../events/attack_on_spell_target_province_getname.md) happens</li></ul><li>50:</li><ul><li>the event [The Bigger They Are...](../events/the_bigger_they_are.md) happens</li></ul></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_siege_100_t](../events/missing_localisation_magic_siege_100_t.md) happens</li></ul></ul>

___
##Go back

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if does not have mil power is 10


###Efects:<ul><li>hidden effect:</li><ul><li>If has ruler flag is [magic_siege_menu](../flags/magic_siege_menu.md):</li><ul><li>the event [Siege Magic\n£siege_magic_bg£](../events/siege_magic_npssiege_magic_bgps.md) happens</li></ul><li>else:</li><ul><li>the event [    Transmutation\n£ruler_magic_transmutation_bg£\n\n[Root.GetSchoolMasteryTransmutation]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    ](../events/transmutation_npsruler_magic_transmutation_bgps_n_n_root_getschoolmasterytransmutation_n_n_n_root_getmagicstudyschoolbis_root_getmagicstudybarbis.md) happens</li></ul></ul></ul>
