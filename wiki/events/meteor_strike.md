#Information
 - Title: Meteor Strike
 - ID: magic_siege.14
#Description
Meteor Strike
#Options

___
##Cast Meteor Strike

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>add mil power = -50</li><li>increase witch king points large = yes</li><li>add ruler modifier:</li><ul><li>name = magic_witch_king_meteor_strike</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_siege_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>If has event target:spell target province has fort level is 1, and does not have fort level is 4:</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>90:</li><ul><li>the event [Meteor Strike Successful](../events/meteor_strike_successful.md) happens</li></ul><li>10:</li><ul><li>the event [Meteor Strike Breaks](../events/meteor_strike_breaks.md) happens</li></ul></ul></ul></ul><li>If has event target:spell target province has fort level is 4, and does not have fort level is 6:</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>80:</li><ul><li>the event [Meteor Strike Successful](../events/meteor_strike_successful.md) happens</li></ul><li>20:</li><ul><li>the event [Meteor Strike Breaks](../events/meteor_strike_breaks.md) happens</li></ul></ul></ul></ul><li>If has event target:spell target province has fort level is 6, and does not have fort level is 8:</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>the event [Meteor Strike Successful](../events/meteor_strike_successful.md) happens</li></ul><li>30:</li><ul><li>the event [Meteor Strike Breaks](../events/meteor_strike_breaks.md) happens</li></ul></ul></ul></ul><li>If has event target:spell target province has fort level is 8:</li><ul><li>set country flag [spell_4](../flags/spell_4.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>60:</li><ul><li>the event [Meteor Strike Successful](../events/meteor_strike_successful.md) happens</li></ul><li>40:</li><ul><li>the event [Meteor Strike Breaks](../events/meteor_strike_breaks.md) happens</li></ul></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_siege_100_t](../events/missing_localisation_magic_siege_100_t.md) happens</li></ul></ul>

___
##Go back

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if does not have mil power is 10


###Efects:<ul><li>hidden effect:</li><ul><li>If has ruler flag is [magic_siege_menu](../flags/magic_siege_menu.md):</li><ul><li>the event [Siege Magic\n£siege_magic_bg£](../events/siege_magic_npssiege_magic_bgps.md) happens</li></ul><li>else:</li><ul><li>the event [    Evocation\n£ruler_magic_evocation_bg£\n\n[Root.GetSchoolMasteryEvocation]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    ](../events/evocation_npsruler_magic_evocation_bgps_n_n_root_getschoolmasteryevocation_n_n_n_root_getmagicstudyschoolbis_root_getmagicstudybarbis.md) happens</li></ul></ul></ul>
