#Information
 - Title: Lich Revival
 - ID: magic_project_lichdom.12
#Description
Lich Revival
#Options

___
##The lich assumes their rightful place as [Root.Monarch.GetTitle].

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>tooltip:</li><ul><li>If has country flag is [b38_entef_ruler](../flags/b38_entef_ruler.md):</li><ul><li>define ruler:</li><ul><li>age = 33</li><li>name = "Entef"</li><li>dynasty = "of Wibnuat"</li><li>male = yes</li><li>max random adm = 0</li><li>max random dip = 0</li><li>max random mil = 0</li><li>hide skills = yes</li></ul></ul><li>else:</li><ul><li>If has country flag is [lich_ruler_female](../flags/lich_ruler_female.md):</li><ul><li>define ruler:</li><ul><li>age = 33</li><li>dynasty = " "</li><li>female = yes</li><li>max random adm = 0</li><li>max random dip = 0</li><li>max random mil = 0</li><li>hide skills = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>age = 33</li><li>dynasty = " "</li><li>male = yes</li><li>max random adm = 0</li><li>max random dip = 0</li><li>max random mil = 0</li><li>hide skills = yes</li></ul></ul></ul></ul><li>restore ruler stats = yes</li><li>revival stat loss = yes</li><li>set heir = old_heir</li><li>set ruler flag [is_a_lich](../flags/is_a_lich.md)</li><li>set ruler flag [new_lich_setup](../flags/new_lich_setup.md)</li><li>clr country flag [interregnum](../flags/interregnum.md)</li><li>hidden effect:</li><ul><li>the event [A Lich Reborn](../events/a_lich_reborn.md) happens</li></ul></ul>
