This page has the same name as others. For full listing see bottom of [the base page](earthquake.md).

#Information
 - Title: Earthquake
 - ID: magic_siege.11
#Description
Earthquake
#Options

___
##Cast Earthquake

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>add mil power = -20</li><li>add adm power = -5</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_siege_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>increase witch king points medium = yes</li><li>add ruler modifier:</li><ul><li>name = magic_witch_king_earthquake</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>If has event target:spell target province has terrain is mountain; and  has ruler flag is [evocation_3](../flags/evocation_3.md):</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>80:</li><ul><li>the event ˻magic_siege.12˼ happens</li></ul><li>20:</li><ul><li>the event ˻magic_siege.13˼ happens</li></ul></ul></ul></ul><li>Else if has AND has has terrain is hills, and has terrain is highlands; and AND has ruler flag is [evocation_3](../flags/evocation_3.md); and has AND has event target:spell target province has terrain is mountain; and AND has ruler flag is [evocation_2](../flags/evocation_2.md):</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>70:</li><ul><li>the event ˻magic_siege.12˼ happens</li></ul><li>30:</li><ul><li>the event ˻magic_siege.13˼ happens</li></ul></ul></ul></ul><li>Else if has AND has has terrain is coastline, and has terrain is coastal desert; and AND has ruler flag is [evocation_3](../flags/evocation_3.md); and has AND has has terrain is hills, and has terrain is highlands; and AND has ruler flag is [evocation_2](../flags/evocation_2.md):</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>60:</li><ul><li>the event ˻magic_siege.12˼ happens</li></ul><li>40:</li><ul><li>the event ˻magic_siege.13˼ happens</li></ul></ul></ul></ul><li>Else if has has terrain is coastline, and has terrain is coastal desert; and  has ruler flag is [evocation_2](../flags/evocation_2.md):</li><ul><li>set country flag [spell_4](../flags/spell_4.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event ˻magic_siege.12˼ happens</li></ul><li>50:</li><ul><li>the event ˻magic_siege.13˼ happens</li></ul></ul></ul></ul><li>else:</li><ul><li>set country flag [spell_5](../flags/spell_5.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>40:</li><ul><li>the event ˻magic_siege.12˼ happens</li></ul><li>60:</li><ul><li>the event ˻magic_siege.13˼ happens</li></ul></ul></ul></ul><li>hidden effect:</li><ul><li>the event ˻magic_siege.104˼ happens</li></ul></ul>

___
##Go back

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if does not have mil power is 10


###Efects:<ul><li>hidden effect:</li><ul><li>If has ruler flag is [magic_siege_menu](../flags/magic_siege_menu.md):</li><ul><li>the event ˻magic_siege.1˼ happens</li></ul><li>else:</li><ul><li>the event ˻magic_ruler.5˼ happens</li></ul></ul></ul>
