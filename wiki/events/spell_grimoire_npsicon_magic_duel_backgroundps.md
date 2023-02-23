#Information
 - Title: Spell Grimoire\n£icon_magic_duel_background£
 - ID: magic_duel.2
#Description
Spell Grimoire\n£icon_magic_duel_background£
#Options

___
##Go Back

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>highlight = yes</li><li>hidden effect:</li><ul><li>the event ˻magic_duel.1˼ happens</li></ul></ul>

___
##Snare

###Available if:
<li>has ruler flag [casting_abjuration](../flags/casting_abjuration.md)</li>

###AI weighting:
AI weights this option at 5
 - Multiplied by 20 if has want to reduce enemy evasion is yes


###Efects:<ul><li>custom tooltip = casting_abjuration_0</li><li>cast spell:</li><ul><li>value = 2.5</li><li>debuff spell evasion = yes</li><li>cost = 0</li></ul><li>process magical turn = yes</li></ul>

___
##Mage Armour

###Available if:
<li>has ruler flag [casting_abjuration](../flags/casting_abjuration.md)</li><li>has ruler flag  abjuration_1</li><li>check variable:</li><ul><li>current mana is at least 30</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 20 if has want to increase shield is yes


###Efects:<ul><li>custom tooltip = casting_abjuration_1</li><li>cast spell:</li><ul><li>value = 40</li><li>shield = yes</li><li>cost = 30</li></ul><li>process magical turn = yes</li></ul>

___
##Freedom

###Available if:
<li>has ruler flag [casting_abjuration](../flags/casting_abjuration.md)</li><li>has ruler flag  abjuration_2</li><li>check variable:</li><ul><li>current mana is at least 50</li></ul>

###AI weighting:
AI weights this option at 35
 - Multiplied by 20 if has want to incrase evasion is yes
 - Multiplied by 20 if has want to incrase evasion big is yes
 - Multiplied by 0 if has never increase evasion is yes


###Efects:<ul><li>custom tooltip = casting_abjuration_2</li><li>cast spell:</li><ul><li>value = 20</li><li>buff spell evasion = yes</li><li>cost = 50</li></ul><li>process magical turn = yes</li></ul>

___
##Awakening

###Available if:
<li>has ruler flag [casting_abjuration](../flags/casting_abjuration.md)</li><li>has ruler flag  abjuration_3</li><li>check variable:</li><ul><li>current mana is at least 80</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 20 if has want to increase accuracy is yes
 - Multiplied by 20 if has want to increase accuracy big is yes
 - Multiplied by 0 if has never increase accuracy is yes


###Efects:<ul><li>custom tooltip = casting_abjuration_3</li><li>cast spell:</li><ul><li>value = 0.2</li><li>buff spell power = yes</li><li>cost = 60</li></ul><li>cast spell:</li><ul><li>value = 5</li><li>buff spell accuracy = yes</li><li>cost = 20</li></ul><li>process magical turn = yes</li></ul>

___
##Acid Splash

###Available if:
<li>has ruler flag [casting_conjuration](../flags/casting_conjuration.md)</li>

###AI weighting:
AI weights this option at 5
 - Multiplied by 20 if has want to apply dot is yes
 - Multiplied by 10 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_conjuration_0</li><li>cast spell:</li><ul><li>value = 0.4</li><li>dot = yes</li><li>cost = 0</li></ul><li>cast spell:</li><ul><li>value = 8</li><li>damage = yes</li><li>cost = 0</li></ul><li>process magical turn = yes</li></ul>

___
##Flaming Sphere

###Available if:
<li>has ruler flag [casting_conjuration](../flags/casting_conjuration.md)</li><li>has ruler flag  conjuration_1</li><li>check variable:</li><ul><li>current mana is at least 20</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 10 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_conjuration_1</li><li>cast spell:</li><ul><li>value = 22</li><li>damage = yes</li><li>cost = 20</li></ul><li>process magical turn = yes</li></ul>

___
##Insect Plague

###Available if:
<li>has ruler flag [casting_conjuration](../flags/casting_conjuration.md)</li><li>has ruler flag  conjuration_2</li><li>check variable:</li><ul><li>current mana is at least 35</li></ul>

###AI weighting:
AI weights this option at 35
 - Multiplied by 10 if has want to deal damage is yes
 - Multiplied by 20 if has want to apply dot is yes
 - Multiplied by 20 if has want to reduce enemy accuracy is yes


###Efects:<ul><li>custom tooltip = casting_conjuration_2</li><li>cast spell:</li><ul><li>value = 6</li><li>dot = yes</li><li>cost = 25</li></ul><li>cast spell:</li><ul><li>value = 3</li><li>debuff spell accuracy = yes</li><li>cost = 10</li></ul><li>process magical turn = yes</li></ul>

___
##Reality Shift

###Available if:
<li>has ruler flag [casting_conjuration](../flags/casting_conjuration.md)</li><li>has ruler flag  conjuration_3</li><li>check variable:</li><ul><li>current mana is at least 60</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 20 if has want to increase shield is yes
 - Multiplied by 20 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_conjuration_3</li><li>cast spell:</li><ul><li>value = 43.5</li><li>shield = yes</li><li>cost = 30</li></ul><li>cast spell:</li><ul><li>value = 40</li><li>damage = yes</li><li>cost = 30</li></ul><li>process magical turn = yes</li></ul>

___
##Gift of Alacrity

###Available if:
<li>has ruler flag [casting_divination](../flags/casting_divination.md)</li>

###AI weighting:
AI weights this option at 5
 - Multiplied by 0 if has never increase evasion is yes
 - Multiplied by 20 if has want to incrase evasion is yes


###Efects:<ul><li>custom tooltip = casting_divination_0</li><li>cast spell:</li><ul><li>value = 6.5</li><li>buff spell evasion = yes</li><li>cost = 0</li></ul><li>process magical turn = yes</li></ul>

___
##Detect Thoughts

###Available if:
<li>has ruler flag [casting_divination](../flags/casting_divination.md)</li><li>has ruler flag  divination_1</li><li>check variable:</li><ul><li>current mana is at least 30</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 20 if has want to reduce enemy accuracy is yes


###Efects:<ul><li>custom tooltip = casting_divination_1</li><li>cast spell:</li><ul><li>value = 10</li><li>debuff spell accuracy = yes</li><li>cost = 30</li></ul><li>process magical turn = yes</li></ul>

___
##Insect Plague

###Available if:
<li>has ruler flag [casting_divination](../flags/casting_divination.md)</li><li>has ruler flag  divination_2</li><li>check variable:</li><ul><li>current mana is at least 30</li></ul>

###AI weighting:
AI weights this option at 35
 - Multiplied by 20 if has want to increase accuracy is yes
 - Multiplied by 20 if has want to increase accuracy big is yes
 - Multiplied by 0 if has never increase accuracy is yes


###Efects:<ul><li>custom tooltip = casting_divination_2</li><li>cast spell:</li><ul><li>value = 12</li><li>buff spell accuracy = yes</li><li>cost = 30</li></ul><li>process magical turn = yes</li></ul>

___
##Foresight

###Available if:
<li>has ruler flag [casting_divination](../flags/casting_divination.md)</li><li>has ruler flag  divination_3</li><li>check variable:</li><ul><li>current mana is at least 50</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 20 if has want to increase accuracy is yes
 - Multiplied by 20 if has want to increase accuracy big is yes
 - Multiplied by 0 if has never increase accuracy is yes


###Efects:<ul><li>custom tooltip = casting_divination_3</li><li>cast spell:</li><ul><li>value = 25</li><li>buff spell accuracy = yes</li><li>cost = 30</li></ul><li>cast spell:</li><ul><li>value = 0.05</li><li>buff spell power = yes</li><li>cost = 20</li></ul><li>process magical turn = yes</li></ul>

___
##Encode Thoughts

###Available if:
<li>has ruler flag [casting_enchantment](../flags/casting_enchantment.md)</li>

###AI weighting:
AI weights this option at 5
 - Multiplied by 20 if has want to increase accuracy is yes
 - Multiplied by 0 if has never increase accuracy is yes


###Efects:<ul><li>custom tooltip = casting_enchantment_0</li><li>cast spell:</li><ul><li>value = 2.5</li><li>buff spell accuracy = yes</li><li>cost = 0</li></ul><li>process magical turn = yes</li></ul>

___
##Power Word: Shield

###Available if:
<li>has ruler flag [casting_enchantment](../flags/casting_enchantment.md)</li><li>has ruler flag  enchantment_1</li><li>check variable:</li><ul><li>current mana is at least 25</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 20 if has want to increase shield is yes


###Efects:<ul><li>custom tooltip = casting_enchantment_1</li><li>cast spell:</li><ul><li>value = 27.5</li><li>shield = yes</li><li>cost = 25</li></ul><li>process magical turn = yes</li></ul>

___
##Power Word: Pain

###Available if:
<li>has ruler flag [casting_enchantment](../flags/casting_enchantment.md)</li><li>has ruler flag  enchantment_2</li><li>check variable:</li><ul><li>current mana is at least 40</li></ul>

###AI weighting:
AI weights this option at 35
 - Multiplied by 20 if has want to reduce enemy accuracy is yes
 - Multiplied by 20 if has want to apply dot is yes


###Efects:<ul><li>custom tooltip = casting_enchantment_2</li><li>cast spell:</li><ul><li>value = 5</li><li>dot = yes</li><li>cost = 20</li></ul><li>cast spell:</li><ul><li>value = 7.5</li><li>debuff spell accuracy = yes</li><li>cost = 20</li></ul><li>process magical turn = yes</li></ul>

___
##Psychic Scream

###Available if:
<li>has ruler flag [casting_enchantment](../flags/casting_enchantment.md)</li><li>has ruler flag  enchantment_3</li><li>check variable:</li><ul><li>current mana is at least 65</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 20 if has want to reduce enemy accuracy is yes
 - Multiplied by 20 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_enchantment_3</li><li>cast spell:</li><ul><li>value = 10</li><li>debuff spell accuracy = yes</li><li>cost = 25</li></ul><li>cast spell:</li><ul><li>value = 50</li><li>damage = yes</li><li>cost = 40</li></ul><li>process magical turn = yes</li></ul>

___
##Fireball

###Available if:
<li>has ruler flag [casting_evocation](../flags/casting_evocation.md)</li>

###AI weighting:
AI weights this option at 5
 - Multiplied by 20 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_evocation_0</li><li>cast spell:</li><ul><li>value = 13</li><li>damage = yes</li><li>cost = 0</li></ul><li>process magical turn = yes</li></ul>

___
##Lightning Bolt

###Available if:
<li>has ruler flag [casting_evocation](../flags/casting_evocation.md)</li><li>has ruler flag  evocation_1</li><li>check variable:</li><ul><li>current mana is at least 25</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 20 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_evocation_1</li><li>cast spell:</li><ul><li>value = 0.025</li><li>buff spell power = yes</li><li>cost = 10</li></ul><li>cast spell:</li><ul><li>value = 20</li><li>damage = yes</li><li>cost = 15</li></ul><li>process magical turn = yes</li></ul>

___
##Ice Storm

###Available if:
<li>has ruler flag [casting_evocation](../flags/casting_evocation.md)</li><li>has ruler flag  evocation_2</li><li>check variable:</li><ul><li>current mana is at least 55</li></ul>

###AI weighting:
AI weights this option at 35
 - Multiplied by 20 if has want to reduce enemy evasion is yes
 - Multiplied by 20 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_evocation_2</li><li>cast spell:</li><ul><li>value = 6</li><li>debuff spell evasion = yes</li><li>cost = 20</li></ul><li>cast spell:</li><ul><li>value = 45</li><li>damage = yes</li><li>cost = 35</li></ul><li>process magical turn = yes</li></ul>

___
##Power Word: Heal

###Available if:
<li>has ruler flag [casting_evocation](../flags/casting_evocation.md)</li><li>has ruler flag  evocation_3</li><li>check variable:</li><ul><li>current mana is at least 75</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 50 if has want to heal is yes
 - Multiplied by 50 if has want to heal big is yes


###Efects:<ul><li>custom tooltip = casting_evocation_3</li><li>cast spell:</li><ul><li>value = 50</li><li>heal = yes</li><li>cost = 50</li></ul><li>cast spell:</li><ul><li>value = 6.5</li><li>hot = yes</li><li>cost = 25</li></ul><li>process magical turn = yes</li></ul>

___
##Minor Illusions

###Available if:
<li>has ruler flag [casting_illusion](../flags/casting_illusion.md)</li>

###AI weighting:
AI weights this option at 5
 - Multiplied by 20 if has want to reduce enemy accuracy is yes


###Efects:<ul><li>custom tooltip = casting_illusion_0</li><li>cast spell:</li><ul><li>value = 2.5</li><li>debuff spell accuracy = yes</li><li>cost = 0</li></ul><li>process magical turn = yes</li></ul>

___
##Phantasmal Killer

###Available if:
<li>has ruler flag [casting_illusion](../flags/casting_illusion.md)</li><li>has ruler flag  illusion_1</li><li>check variable:</li><ul><li>current mana is at least 20</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 20 if has want to incrase evasion is yes
 - Multiplied by 20 if has want to incrase evasion big is yes
 - Multiplied by 20 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_illusion_1</li><li>cast spell:</li><ul><li>value = 3.5</li><li>buff spell evasion = yes</li><li>cost = 10</li></ul><li>cast spell:</li><ul><li>value = 11</li><li>damage = yes</li><li>cost = 10</li></ul><li>process magical turn = yes</li></ul>

___
##Mislead

###Available if:
<li>has ruler flag [casting_illusion](../flags/casting_illusion.md)</li><li>has ruler flag  illusion_2</li><li>check variable:</li><ul><li>current mana is at least 40</li></ul>

###AI weighting:
AI weights this option at 35
 - Multiplied by 20 if has want to incrase evasion is yes
 - Multiplied by 20 if has want to incrase evasion big is yes
 - Multiplied by 0 if has never increase evasion is yes


###Efects:<ul><li>custom tooltip = casting_illusion_2</li><li>cast spell:</li><ul><li>value = 15</li><li>buff spell evasion = yes</li><li>cost = 40</li></ul><li>process magical turn = yes</li></ul>

___
##Mirror Images

###Available if:
<li>has ruler flag [casting_illusion](../flags/casting_illusion.md)</li><li>has ruler flag  illusion_3</li><li>check variable:</li><ul><li>current mana is at least 120</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 20 if has want to incrase evasion is yes
 - Multiplied by 20 if has want to incrase evasion big is yes
 - Multiplied by 2 if has never increase evasion is yes


###Efects:<ul><li>custom tooltip = casting_illusion_3</li><li>cast spell:</li><ul><li>value = 0.15</li><li>buff spell power = yes</li><li>cost = 60</li></ul><li>cast spell:</li><ul><li>value = 25</li><li>buff spell evasion = yes</li><li>cost = 60</li></ul><li>process magical turn = yes</li></ul>

___
##Necro Touch

###Available if:
<li>has ruler flag [casting_necromancy](../flags/casting_necromancy.md)</li>

###AI weighting:
AI weights this option at 5
 - Multiplied by 20 if has want to apply dot is yes


###Efects:<ul><li>custom tooltip = casting_necromancy_0</li><li>cast spell:</li><ul><li>value = 3</li><li>dot = yes</li><li>cost = 0</li></ul><li>process magical turn = yes</li></ul>

___
##Bestow Curse

###Available if:
<li>has ruler flag [casting_necromancy](../flags/casting_necromancy.md)</li><li>has ruler flag  necromancy_1</li><li>check variable:</li><ul><li>current mana is at least 25</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 20 if has want to apply dot is yes
 - Multiplied by 20 if has want to reduce enemy accuracy is yes


###Efects:<ul><li>custom tooltip = casting_necromancy_1</li><li>cast spell:</li><ul><li>value = 4.2</li><li>dot = yes</li><li>cost = 15</li></ul><li>cast spell:</li><ul><li>value = 2.75</li><li>debuff spell accuracy = yes</li><li>cost = 10</li></ul><li>process magical turn = yes</li></ul>

___
##Contagion

###Available if:
<li>has ruler flag [casting_necromancy](../flags/casting_necromancy.md)</li><li>has ruler flag  necromancy_2</li><li>check variable:</li><ul><li>current mana is at least 35</li></ul>

###AI weighting:
AI weights this option at 35
 - Multiplied by 20 if has want to apply dot is yes
 - Multiplied by 20 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_necromancy_2</li><li>cast spell:</li><ul><li>value = 10.5</li><li>dot = yes</li><li>cost = 35</li></ul><li>process magical turn = yes</li></ul>

___
##Enervation

###Available if:
<li>has ruler flag [casting_necromancy](../flags/casting_necromancy.md)</li><li>has ruler flag  necromancy_3</li><li>check variable:</li><ul><li>current mana is at least 80</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 30 if has want to apply dot is yes
 - Multiplied by 30 if has want to deal damage is yes


###Efects:<ul><li>custom tooltip = casting_necromancy_3</li><li>cast spell:</li><ul><li>value = 16</li><li>dot = yes</li><li>cost = 50</li></ul><li>cast spell:</li><ul><li>value = 0.08</li><li>debuff spell power = yes</li><li>cost = 30</li></ul><li>process magical turn = yes</li></ul>

___
##Thorn Whip

###Available if:
<li>has ruler flag [casting_transmutation](../flags/casting_transmutation.md)</li>

###AI weighting:
AI weights this option at 5
 - Multiplied by 20 if has want to deal damage is yes
 - Multiplied by 20 if has want to apply dot is yes


###Efects:<ul><li>custom tooltip = casting_transmutation_0</li><li>cast spell:</li><ul><li>value = 0.2</li><li>dot = yes</li><li>cost = 0</li></ul><li>cast spell:</li><ul><li>value = 10</li><li>damage = yes</li><li>cost = 0</li></ul><li>process magical turn = yes</li></ul>

___
##Guardian

###Available if:
<li>has ruler flag [casting_transmutation](../flags/casting_transmutation.md)</li><li>has ruler flag  transmutation_1</li><li>check variable:</li><ul><li>current mana is at least 35</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 20 if has want to increase shield is yes


###Efects:<ul><li>custom tooltip = casting_transmutation_1</li><li>cast spell:</li><ul><li>value = 42</li><li>shield = yes</li><li>cost = 35</li></ul><li>process magical turn = yes</li></ul>

___
##Magic Empowerment

###Available if:
<li>has ruler flag [casting_transmutation](../flags/casting_transmutation.md)</li><li>has ruler flag  transmutation_2</li><li>check variable:</li><ul><li>current mana is at least 50</li></ul>

###AI weighting:
AI weights this option at 35
 - Multiplied by 20 if has want to increase spell power big is yes
 - Multiplied by 0.01 if has stop increase spell power is yes


###Efects:<ul><li>custom tooltip = casting_transmutation_2</li><li>cast spell:</li><ul><li>value = 0.13</li><li>buff spell power = yes</li><li>cost = 50</li></ul><li>process magical turn = yes</li></ul>

___
##Regenerate

###Available if:
<li>has ruler flag [casting_transmutation](../flags/casting_transmutation.md)</li><li>has ruler flag  transmutation_3</li><li>check variable:</li><ul><li>current mana is at least 75</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 50 if has want to heal is yes
 - Multiplied by 50 if has want to heal big is yes


###Efects:<ul><li>custom tooltip = casting_transmutation_3</li><li>cast spell:</li><ul><li>value = 21</li><li>hot = yes</li><li>cost = 75</li></ul><li>process magical turn = yes</li></ul>
