#Information
 - Title: Thunderstorm
 - ID: magic_siege.17
#Description
Thunderstorm
#Options

___
##Cast Thunderstorm

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>add mil power = -10</li><li>add adm power = -15</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_siege_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>increase witch king points small = yes</li><li>add ruler modifier:</li><ul><li>name = magic_witch_king_thunderstorm</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>If has has climate is tropical, and has province modifier is mild winter; and event target:spell target province has ROOT has ruler flag is [conjuration_3](../flags/conjuration_3.md):</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>90:</li><ul><li>the event [Thunderstorm Succeeds](../events/thunderstorm_succeeds.md) happens</li></ul><li>10:</li><ul><li>the event [Thunderstorm Wanders](../events/thunderstorm_wanders.md) happens</li></ul></ul></ul></ul><li>Else if has AND has province modifier is normal winter, and AND has ROOT has ruler flag is [conjuration_3](../flags/conjuration_3.md); and has has climate is tropical, and has province modifier is mild winter; and AND has ROOT has ruler flag is [conjuration_2](../flags/conjuration_2.md):</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>80:</li><ul><li>the event [Thunderstorm Succeeds](../events/thunderstorm_succeeds.md) happens</li></ul><li>20:</li><ul><li>the event [Thunderstorm Wanders](../events/thunderstorm_wanders.md) happens</li></ul></ul></ul></ul><li>Else if has AND has province modifier is severe winter, and AND has ROOT has ruler flag is [conjuration_3](../flags/conjuration_3.md); and has AND has province modifier is normal winter, and AND has ROOT has ruler flag is [conjuration_2](../flags/conjuration_2.md):</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>the event [Thunderstorm Succeeds](../events/thunderstorm_succeeds.md) happens</li></ul><li>30:</li><ul><li>the event [Thunderstorm Wanders](../events/thunderstorm_wanders.md) happens</li></ul></ul></ul></ul><li>Else if has has climate is arid, and has climate is arctic; and AND has ROOT has ruler flag is [conjuration_3](../flags/conjuration_3.md); and has AND has province modifier is severe winter, and AND has ROOT has ruler flag is [conjuration_2](../flags/conjuration_2.md):</li><ul><li>set country flag [spell_4](../flags/spell_4.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>60:</li><ul><li>the event [Thunderstorm Succeeds](../events/thunderstorm_succeeds.md) happens</li></ul><li>40:</li><ul><li>the event [Thunderstorm Wanders](../events/thunderstorm_wanders.md) happens</li></ul></ul></ul></ul><li>Else if has has climate is arid, and has climate is arctic, and has ROOT has ruler flag is [conjuration_2](../flags/conjuration_2.md):</li><ul><li>set country flag [spell_5](../flags/spell_5.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event [Thunderstorm Succeeds](../events/thunderstorm_succeeds.md) happens</li></ul><li>50:</li><ul><li>the event [Thunderstorm Wanders](../events/thunderstorm_wanders.md) happens</li></ul></ul></ul></ul><li>else:</li><ul><li>set country flag [spell_6](../flags/spell_6.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>40:</li><ul><li>the event [Thunderstorm Succeeds](../events/thunderstorm_succeeds.md) happens</li></ul><li>60:</li><ul><li>the event [Thunderstorm Wanders](../events/thunderstorm_wanders.md) happens</li></ul></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_siege_100_t](../events/missing_localisation_magic_siege_100_t.md) happens</li></ul></ul>

___
##Go back

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if does not have mil power is 20; and does not have adm power is 30


###Efects:<ul><li>hidden effect:</li><ul><li>If has ruler flag is [magic_siege_menu](../flags/magic_siege_menu.md):</li><ul><li>the event [Siege Magic\n£siege_magic_bg£](../events/siege_magic_npssiege_magic_bgps.md) happens</li></ul><li>else:</li><ul><li>the event [    Conjuration\n£ruler_magic_conjuration_bg£\n\n[Root.GetSchoolMasteryConjuration]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    ](../events/conjuration_npsruler_magic_conjuration_bgps_n_n_root_getschoolmasteryconjuration_n_n_n_root_getmagicstudyschoolbis_root_getmagicstudybarbis.md) happens</li></ul></ul></ul>
