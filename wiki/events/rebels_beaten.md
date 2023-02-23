#Information
 - Title: Rebels Beaten
 - ID: flavor_sugamber.13
#Description
Rebels Beaten
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Order has finally been restored.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has country flag is [sugamber_baldwin_rebellion](../flags/sugamber_baldwin_rebellion.md), and does not have ruler is "Ethelbert":</li><ul><li>define ruler:</li><ul><li>name = "Baldwin"</li><li>dynasty = "Lockcastle"</li><li>adm = 4</li><li>dip = 3</li><li>mil = 4</li><li>age = 39</li></ul><li>set country flag [sugamber_lisolette_avenged](../flags/sugamber_lisolette_avenged.md)</li></ul><li>Else if has country flag is [sugamber_ethelbert_rebellion](../flags/sugamber_ethelbert_rebellion.md), and does not have calc true if has ruler is "Ewald II", and calc true if has ruler is "Lisolette", and calc true if has ruler is "Baldwin", and calc true if has amount is 1:</li><ul><li>define ruler:</li><ul><li>name = "Ethelbert"</li><li>dynasty = "of Rupellion"</li><li>adm = 4</li><li>dip = 4</li><li>mil = 5</li><li>age = 40</li></ul><li>set country flag [sugamber_ethelbert_restored](../flags/sugamber_ethelbert_restored.md)</li></ul><li>else:</li><ul><li>set country flag [rebels_lost](../flags/rebels_lost.md)</li></ul><li>set country flag [had_sugamber_succession_war](../flags/had_sugamber_succession_war.md)</li><li>disband rebels = pretender_rebels</li></ul>
