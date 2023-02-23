This is a list of all [decisions](decisions.md) in the category "Halessi_Formables_Decisions"

| Decision | Completion requirements | Effects | Requirements to appear |
| ----- | ------ | ----- | ------ |
| <a name="heirs_of_bhengudak">Heirs of Bhengudak</a><br />*Long ago the Great Kusheng Bhengudak conquered the kingdom of Odheongu in the east, ushering in the mighty empire of Guwaamud, which would stand for nearly 900 years before it was torn down by their disloyal subjects. We have since repeated Bhengudak's grand feat, crushing the Odheongun and not only returning to Bhengudak's capital, but once again laying claim to the fallen capital of Odheongu. With such great successes, we can now rightfully declare ourselves the sovereigns of Guwaamud, heirs to the glory of Bhengudak!* | <li>is free or tributary trigger is yes</li><li>is not at war</li><li>does not have regency</li><li>None of the following:</li><ul><li>exists is Y96</li></ul><li>total development is at least 140</li><li>num of owned provinces with:</li><ul><li>value is at least 12</li><li>region is odheongu_region</li></ul><li>owns core province 5348</li><li>owns 5355</li><li>NOT:</li><ul><li>has ruler modifier faceless_queen_modifier</li></ul> | <li>set country flag [formed_guwaamud_flag](../flags/formed_guwaamud_flag.md)</li><li>set ruler flag [guwaamud_former](../flags/guwaamud_former.md)</li><li>add ruler modifier:</li><ul><li>name = Y91_guwaamud_fomer_mod</li><li>duration = -1</li></ul><li>change tag = Y96</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>If has primary culture is chimbija:</li><ul><li>override country name = GUNGAMU</li></ul><li>remove non electors emperors from empire effect = yes</li><li>swap non generic missions = yes</li><li>add prestige = 20</li><li>If does not have government rank is 2:</li><ul><li>set government rank = 2</li></ul><li>change government = monarchy</li><li>add government reform = guwaamud_harem_reform</li><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>If does not have primary culture is chimbija:</li><ul><li>custom tooltip = Our Horde Heritage will lessen.</li><li>hidden effect:</li><ul><li>country gets the modifier Y91_horde_heritage_1 until otherwise removed</li></ul></ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 5348</li></ul><li>hidden effect:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = 5406</li><li>province id = 5348</li></ul></ul><li>If does not have primary culture is chimbija:</li><ul><li>5348:</li><ul><li>move capital effect = yes</li><li>change culture = shuvuush</li><li>change province name = "Bhengutai"</li></ul></ul><li>If odheongu region does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | <li>None of the following:</li><ul><li>Country is Y98</li></ul><li>NOT:</li><ul><li>has country flag [formed_guwaamud_flag](../flags/formed_guwaamud_flag.md)</li></ul><li>Any of the following:</li><ul><li>primary culture is shuvuush</li><li>primary culture  is guwaadun</li><li>primary culture   is chimbija</li></ul><li>was never end game tag trigger is yes</li> |
| <a name="the_great_empire">The Great Empire</a><br />*The Yan have long looked down on our people, haughtily dismissing us as savages from the decadent opulence of their cities and confident in the security of their walls. How they must be reeling now that our hordes have overrun their most important cities, our banners flying proud over their markets and palaces. Our time in this land has changed us however, with many of our people adopting the traditions and culture of the Yan; our warlords wear Yansheni silk and many speak the native language as their tongue of birth. It is time for us to accept the winds of change and establish a grand empire that shall finally unify all of Yanshen under a single throne.* | <li>is not subject</li><li>is not at war</li><li>does not have regency</li><li>None of the following:</li><ul><li>exists is Y98</li></ul><li>adm tech is at least 7</li><li>num of owned provinces with:</li><ul><li>value is at least 100</li><li>superregion is yanshen_superregion</li></ul><li>owns core province 4925</li><li>owns core province  4859</li><li>owns core province   4879</li><li>owns core province    4871</li><li>owns core province     4868</li><li>NOT:</li><ul><li>has ruler modifier faceless_queen_modifier</li></ul><li>custom trigger tooltip:</li><ul><li>tooltip is not_guwaamud_former</li><li>None of the following:</li><ul><li>has ruler flag [guwaamud_former](../flags/guwaamud_former.md)</li></ul></ul> | <li>change tag = Y98</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>remove non electors emperors from empire effect = yes</li><li>swap non generic missions = yes</li><li>add prestige = 25</li><li>set country flag [formed_daxugo_flag](../flags/formed_daxugo_flag.md)</li><li>set ruler flag [daxugo_former](../flags/daxugo_former.md)</li><li>add ruler modifier:</li><ul><li>name = Y91_daxugo_fomer_mod</li><li>duration = -1</li></ul><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>change government = monarchy</li><li>If does not have reform is guwaamud harem reform:</li><ul><li>add government reform = autocracy_reform</li></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>hidden effect:</li><ul><li>If has country modifier is Y91 horde heritage 1:</li><ul><li>remove country modifier = Y91_horde_heritage_1</li></ul></ul><li>custom tooltip = Our Horde Heritage will lessen.</li><li>hidden effect:</li><ul><li>country gets the modifier Y91_horde_heritage_2 until otherwise removed</li></ul><li>If yanshen superregion does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If does not have technology group is tech halessi:</li><ul><li>change technology group = tech_halessi</li></ul><li>If does not have unit type is tech halessi:</li><ul><li>change unit type = tech_halessi</li></ul><li>change primary culture = daxug</li><li>set ruler culture = daxug</li><li>set heir culture = daxug</li><li>If does not have government rank is 3:</li><ul><li>set government rank = 3</li></ul><li>hidden effect:</li><ul><li>If every owned province has culture is shuvuush:</li><ul><li>change culture = daxug</li></ul><li>If has Y90 is subject of is ROOT:</li><ul><li>Y90:</li><ul><li>change primary culture = daxug</li><li>set ruler culture = daxug</li><li>set heir culture = daxug</li><li>If every owned province has culture is shuvuush:</li><ul><li>change culture = daxug</li></ul></ul></ul><li>If has Y92 is subject of is ROOT:</li><ul><li>Y92:</li><ul><li>change primary culture = daxug</li><li>set ruler culture = daxug</li><li>set heir culture = daxug</li><li>If every owned province has culture is shuvuush:</li><ul><li>change culture = daxug</li></ul></ul></ul></ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 4871</li></ul><li>the event [Rebellion And Compromise](../events/rebellion_and_compromise.md) happens</li><li>4871:</li><ul><li>move capital effect = yes</li><li>If does not have culture is shuvuush:</li><ul><li>change culture = daxug</li></ul><li>change province name = "Duzhekho"</li><li>change religion = ROOT</li></ul> | <li>None of the following:</li><ul><li>has country flag [formed_daxugo_flag](../flags/formed_daxugo_flag.md)</li></ul><li>Any of the following:</li><ul><li>primary culture is shuvuush</li><li>primary culture  is guwaadun</li><li>All of the following:</li><ul><li>primary culture is chimbija</li><li>Country is Y96</li></ul></ul> |
| <a name="form_baihon_xinh">Reform the Baihon Xinh</a><br />*The Baihon Xihn once defied fate itself, routing Jaher's forces and saving southern Haless from his foriegn empire. Since then, many have tried to recreate the alliance of old, but it has always faltered, shatterning into feuding warlords. Now, we can reform the Baihon Xihn, and return to our primordial role as defenders of Thidinkai.* | <li>is not at war</li><li>is free or tributary trigger is yes</li><li>owns core province 4697</li><li>owns core province  4701</li><li>owns core province   4703</li><li>owns core province    4764</li><li>owns core province     5429</li> | <li>change tag = Y97</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>hidden effect:</li><ul><li>If every owned province is part of hre:</li><ul><li>set in empire = no</li></ul></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>If does not have government rank is 2:</li><ul><li>set government rank = 2</li></ul><li>add prestige = 25</li><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>set country flag [formed_baihon_flag](../flags/formed_baihon_flag.md)</li> | <li>Any of the following:</li><ul><li>primary culture is khom</li><li>primary culture  is phonan</li><li>All of the following:</li><ul><li>primary culture is gon</li><li>None of the following:</li><ul><li>Country is Y57</li></ul></ul></ul><li>None of the following:</li><ul><li>exists is Y97</li></ul><li>is using normal or historical nations</li><li>was never end game tag trigger is yes</li><li>NOT:</li><ul><li>has country flag [formed_baihon_flag](../flags/formed_baihon_flag.md)</li></ul> |
| <a name="form_thangoya">Unite the Townships</a><br />*While all of the Kai are notoriously combative and divisive, none are more so than our own people. Our land has been contested by fiercely independent towns for as long as anyone can remember, only being briefly united to defend from invasion or under the boot of foreign conquerors. For too long have others looked at us as disorderly lords ruling over a wartorn land, we now stand in a position to end this squabbling among the Sikai and forge a new republic capable of standing against our enemies as one people.* | <li>is not at war</li><li>is free or tributary trigger is yes</li><li>adm tech is at least 7</li><li>owns core province 4777</li><li>owns core province  4788</li><li>owns core province   4778</li><li>owns core province    4789</li><li>num of owned provinces with:</li><ul><li>value is at least 10</li><li>culture is sikai</li></ul> | <li>change tag = Z62</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>hidden effect:</li><ul><li>If every owned province is part of hre:</li><ul><li>set in empire = no</li></ul></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>set government rank = 2</li><li>add prestige = 15</li><li>If has government is republic:</li><ul><li>add government reform = kai_republic</li></ul><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>set country flag [formed_thangoya_flag](../flags/formed_thangoya_flag.md)</li><li>If thirabnir area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If phakphon area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If ngoen area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If kaiden area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | <li>primary culture is sikai</li><li>None of the following:</li><ul><li>exists is Z62</li></ul><li>NOT:</li><ul><li>ruler culture is sunrise_elf</li></ul><li>NOT:</li><ul><li>has country flag [formed_thangoya_flag](../flags/formed_thangoya_flag.md)</li></ul><li>is using normal or historical nations</li><li>was never end game tag trigger is yes</li> |
| <a name="unite_thidinkai">Empire of the Kai</a><br />*Thidinkai has always been known as a land of "savagery" and bloodthirsty warlords, dismissed as a worthless land where one can only find their own death. They do not see the true wealth of these lands, for they are looking in the wrong place. The true wealth of the Thidinkai is in her people, strong and ferocious, diligent and steadfast, honest and courageous. Divided, other peoples knew to fear us. United, they shall learn to respect the Kai.* | <li>is not at war</li><li>is free or tributary trigger is yes</li><li>adm tech is at least 7</li><li>owns core province 4751</li><li>owns core province  4955</li><li>owns core province   4779</li><li>num of owned provinces with:</li><ul><li>value is at least 5</li><li>culture is bokai</li></ul><li>num of owned provinces with:</li><ul><li>value is at least 5</li><li>culture is binhrung</li></ul><li>num of owned provinces with:</li><ul><li>value is at least 5</li><li>culture is sikai</li></ul><li>Any of the following:</li><ul><li>num of owned provinces with:</li><ul><li>value is at least 5</li><li>culture is phonan</li></ul><li>num of owned provinces with:</li><ul><li>value is at least 5</li><li>culture is hinphat</li></ul></ul> | <li>change tag = Z63</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>hidden effect:</li><ul><li>If every owned province is part of hre:</li><ul><li>set in empire = no</li></ul></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>set government rank = 3</li><li>add prestige = 25</li><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>If has primary culture is binhrung:</li><ul><li>override country name = CHAKKAD_YONHRUNG</li></ul><li>set country flag [formed_thidinkai_flag](../flags/formed_thidinkai_flag.md)</li><li>If thidinkai region does not have core is ROOT; and does not have owned by is ROOT; and does not have province id is 5424:</li><ul><li>add permanent claim = ROOT</li></ul><li>If non chien area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If thuongidut area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | <li>culture group is kai</li><li>None of the following:</li><ul><li>primary culture is phonan</li></ul><li>NOT:</li><ul><li>primary culture is khom</li></ul><li>NOT:</li><ul><li>ruler culture is sunrise_elf</li></ul><li>NOT:</li><ul><li>exists is Z63</li></ul><li>NOT:</li><ul><li>has country flag [formed_thidinkai_flag](../flags/formed_thidinkai_flag.md)</li></ul><li>is using normal or historical nations</li><li>was never end game tag trigger is yes</li> |
| <a name="king_of_kings_form">King of Kings</a><br />*The Lupulan is home to dozens of tribal chiefs calling themselves kings, though none have ever earned the right to call themselves the King of Kings. Until now that is. With our dominance over the jungle firmly cemented and our rule decorated with tales with glory and victory, we can now lay claim to the most vaunted title among the Yanglam.* | <li>is not at war</li><li>is free or tributary trigger is yes</li><li>prestige is at least 75</li><li>legitimacy is at least 100</li><li>num of owned provinces with:</li><ul><li>value is at least 20</li><li>region is lupulan_rainforest_region</li></ul> | <li>change tag = Z64</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>hidden effect:</li><ul><li>If every owned province is part of hre:</li><ul><li>set in empire = no</li></ul></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>set government rank = 2</li><li>add prestige = 15</li><li>If has primary culture is sirtana:</li><ul><li>override country name = GEHET_SIRTAN</li></ul><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>set country flag [formed_damoh_yangla_flag](../flags/formed_damoh_yangla_flag.md)</li><li>If lupulan rainforest region does not have core is ROOT; and does not have owned by is ROOT; and does not have area is amkamsek area; and does not have area is hoangdesinh area:</li><ul><li>add permanent claim = ROOT</li></ul> | <li>culture group is yanglam</li><li>None of the following:</li><ul><li>exists is Z64</li></ul><li>NOT:</li><ul><li>has country flag [formed_damoh_yangla_flag](../flags/formed_damoh_yangla_flag.md)</li></ul><li>is using normal or historical nations</li><li>was never end game tag trigger is yes</li> |
| <a name="form_yanshen">Unite the Yan</a><br />*Yanshen is a diverse and vibrant land, rich in culture and coin. Despite this, we have only been "unified" by conquerors, our divided land proving easy to conquer and her wealth a tempting target. If Yanshen is to survive and prosper, we must end this divisiveness and come together as a united people.* | <li>is not at war</li><li>is free or tributary trigger is yes</li><li>adm tech is at least 7</li><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>owns core province 4871</li><li>capital is at least 4871</li></ul><li>capital scope:</li><ul><li>development is at least 45</li></ul></ul><li>num of owned provinces with:</li><ul><li>value is at least 50</li><li>superregion is yanshen_superregion</li></ul> | <li>change tag = Z65</li><li>hidden effect:</li><ul><li>If has was tag is Y20:</li><ul><li>save global event target as = feiten_or_was_feiten_target</li></ul></ul><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>hidden effect:</li><ul><li>If every owned province is part of hre:</li><ul><li>set in empire = no</li></ul></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>set government rank = 3</li><li>add prestige = 35</li><li>set country flag [formed_yanshen_flag](../flags/formed_yanshen_flag.md)</li><li>If does not have capital is 4871, and does not have primary culture is forest yan, and does not have primary culture is coastal yan:</li><ul><li>capital scope:</li><ul><li>change province name = "Tongyi Cheng"</li></ul></ul><li>Else if does not have capital is 4871; and  has primary culture is forest yan:</li><ul><li>capital scope:</li><ul><li>change province name = "Tungjat Cing"</li></ul></ul><li>Else if does not have capital is 4871; and  has primary culture is coastal yan:</li><ul><li>capital scope:</li><ul><li>change province name = "Thung Siang"</li></ul></ul><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>If has primary culture is forest yan:</li><ul><li>override country name = YANSING</li></ul><li>Else if has primary culture is coastal yan:</li><ul><li>override country name = YANSENG</li></ul><li>If yanshen superregion does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | <li>government is republic</li><li>culture group is yan</li><li>None of the following:</li><ul><li>exists is Z65</li></ul><li>NOT:</li><ul><li>Any of the following:</li><ul><li>has country flag [formed_yanshen_flag](../flags/formed_yanshen_flag.md)</li><li>has country flag  formed_liang_flag</li><li>has country flag   formed_di_yichan_flag</li><li>primary culture is western_yan</li><li>primary culture  is southern_yan</li><li>primary culture   is eastern_yan</li></ul></ul><li>is using normal or historical nations</li><li>was never end game tag trigger is yes</li> |
| <a name="form_liang">An Imperial Yanshen</a><br />*Nearly forgotten are the days when kingdoms reigned in Yanshen, the days of legendary dynasties and heroes, brought to an end by the hands of Harimar. Though we were never fully united, the machinations of the Harimari and their eunuchized officials served to partition us even further. The petty disputes between the eunuch lords and merchant princes have left the Yan weak and divided for long enough, it is time for an emperor to be crowned, and guide our people to a bright and glorious future.* | <li>is not at war</li><li>is free or tributary trigger is yes</li><li>adm tech is at least 7</li><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>owns core province 4871</li><li>capital is at least 4871</li></ul><li>capital scope:</li><ul><li>development is at least 45</li></ul></ul><li>num of owned provinces with:</li><ul><li>value is at least 50</li><li>superregion is yanshen_superregion</li></ul> | <li>change tag = Z66</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>hidden effect:</li><ul><li>If every owned province is part of hre:</li><ul><li>set in empire = no</li></ul></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>set government rank = 3</li><li>add prestige = 35</li><li>set country flag [formed_liang_flag](../flags/formed_liang_flag.md)</li><li>If does not have capital is 4871, and does not have primary culture is forest yan, and does not have primary culture is coastal yan:</li><ul><li>capital scope:</li><ul><li>change province name = "Zhaoming"</li></ul></ul><li>Else if does not have capital is 4871; and  has primary culture is forest yan:</li><ul><li>capital scope:</li><ul><li>change province name = "Ciuming"</li></ul></ul><li>Else if does not have capital is 4871; and  has primary culture is coastal yan:</li><ul><li>capital scope:</li><ul><li>change province name = "Chiaubeng"</li></ul></ul><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>If has primary culture is forest yan:</li><ul><li>override country name = DAAIFAI</li></ul><li>Else if has primary culture is coastal yan:</li><ul><li>override country name = DUAHUI</li></ul><li>If does not have reform is eunuch dynasty reform:</li><ul><li>add government reform = yan_empire_reform</li></ul><li>If yanshen superregion does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>swap non generic missions = yes</li> | <li>government is monarchy</li><li>culture group is yan</li><li>None of the following:</li><ul><li>exists is Z66</li></ul><li>NOT:</li><ul><li>Any of the following:</li><ul><li>has country flag [formed_yanshen_flag](../flags/formed_yanshen_flag.md)</li><li>has country flag  formed_liang_flag</li><li>has country flag   formed_di_yichan_flag</li><li>primary culture is western_yan</li><li>primary culture  is southern_yan</li><li>primary culture   is eastern_yan</li></ul></ul><li>is using normal or historical nations</li><li>was never end game tag trigger is yes</li> |
| <a name="form_di_yichan">Ascend to the Tiger Throne</a><br />*Centuries ago our forefathers ruled this land, ushering in the greatest era Yanshen has ever seen. The plotting of the Yan eunuchs steadily saw our rule undermined however, with Harimari rule being virtually ended by 500 AA. In the time since the Yan have allowed themselves to be ravaged by their own petty wars and the armies of yet another great conqueror. The only way they will see unity and prosperity again is under our reign. It is time for a new Harimari empire of Yanshen.* | <li>is not at war</li><li>is free or tributary trigger is yes</li><li>adm tech is at least 7</li><li>owns core province 4871</li><li>num of owned provinces with:</li><ul><li>value is at least 50</li><li>superregion is yanshen_superregion</li></ul> | <li>change tag = Z67</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>hidden effect:</li><ul><li>If every owned province is part of hre:</li><ul><li>set in empire = no</li></ul></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>set government rank = 3</li><li>add prestige = 35</li><li>set country flag [formed_di_yichan_flag](../flags/formed_di_yichan_flag.md)</li><li>If does not have capital is 4871:</li><ul><li>4871:</li><ul><li>move capital effect = yes</li></ul></ul><li>If does not have government is monarchy:</li><ul><li>change government = monarchy</li><li>add government reform = liangzhu_reform</li></ul><li>Else if has government is monarchy, and does not have reform is liangzhu reform, and does not have reform is flame custodian reform:</li><ul><li>add government reform = liangzhu_reform</li></ul><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>If yanshen superregion does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | <li>primary culture is east_harimari</li><li>None of the following:</li><ul><li>exists is Z67</li></ul><li>NOT:</li><ul><li>Any of the following:</li><ul><li>has country flag [formed_yanshen_flag](../flags/formed_yanshen_flag.md)</li><li>has country flag  formed_liang_flag</li><li>has country flag   formed_di_yichan_flag</li><li>has reform xiaken</li><li>has reform  one_xia</li><li>has reform   xia_parliament_reform</li><li>has reform    wulin</li><li>has reform     indep_xiaken</li></ul></ul><li>is using normal or historical nations</li><li>was never end game tag trigger is yes</li> |
| <a name="form_sunrise_empire">Mantle of the Phoenix</a><br />*When Jaher was murdered, his son Jaerel the Sunrise Emperor inherited a crumbling empire, and his societal reforms came too few and too late to save it. Both father and son met their ends at an assassin's blade, and elven rule in Haless died with them. Most of the sun elves left behind in the wake of the two tragedies were forced to fight their way back west, however a few remained in these hostile lands. For centuries we lived forgotten and mistrusted.\n\nNow, as monsters and warlords bring devastation and tribulation to the land, we stand at the head of a vast and mighty domain, rich in culture, arms, and wealth. It is time to proclaim a new empire, built on the principles of Jaerel and his short lived realm. It is time for Haless to be unified not under a conqueror but under a protector. It is time, for a new Sunrise Empire to ascend, and may she never fall.* | <li>is not at war</li><li>is free or tributary trigger is yes</li><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>owns core province 4871</li><li>capital is at least 4871</li></ul><li>capital scope:</li><ul><li>development is at least 60</li></ul></ul><li>num of owned provinces with:</li><ul><li>value is at least 150</li><li>Any of the following:</li><ul><li>superregion is yanshen_superregion</li><li>superregion  is south_haless_superregion</li></ul></ul> | <li>change tag = Y00</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>hidden effect:</li><ul><li>If every owned province is part of hre:</li><ul><li>set in empire = no</li></ul></ul><li>country gets the modifier "centralization_modifier" for 20 years</li><li>set government rank = 3</li><li>add prestige = 35</li><li>set country flag [formed_sunrise_empire_flag](../flags/formed_sunrise_empire_flag.md)</li><li>If does not have capital is 4871:</li><ul><li>capital scope:</li><ul><li>change province name = "Azka Nurdazin"</li></ul></ul><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>If has capital scope has superregion is yanshen superregion:</li><ul><li>If yanshen superregion does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If south haless superregion does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add claim = ROOT</li></ul></ul><li>Else if has capital scope has superregion is south haless superregion:</li><ul><li>If yanshen superregion does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add claim = ROOT</li></ul><li>If south haless superregion does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul></ul><li>If does not have government is republic:</li><ul><li>change government = republic</li><li>add government reform = sunrise_court_reform</li></ul><li>Else if has government is republic, and does not have reform is sunrise court reform:</li><ul><li>add government reform = sunrise_court_reform</li></ul> | <li>Any of the following:</li><ul><li>ruler culture is sun_elf</li><li>ruler culture  is sunrise_elf</li></ul><li>capital scope:</li><ul><li>Any of the following:</li><ul><li>superregion is yanshen_superregion</li><li>superregion  is north_haless_superregion</li><li>superregion   is south_haless_superregion</li></ul></ul><li>None of the following:</li><ul><li>Country is Y86</li></ul><li>NOT:</li><ul><li>exists is Y00</li></ul><li>NOT:</li><ul><li>Country is Phoenix Empire</li></ul><li>NOT:</li><ul><li>has country flag [formed_sunrise_empire_flag](../flags/formed_sunrise_empire_flag.md)</li></ul><li>is using normal or historical nations</li> |
| <a name="form_yanszin">Unify The Yanszin</a><br />*Be it by cooperation or by force, the disparate states of the League of Yanszin have been unified under one banner.* | <li>is not at war</li><li>is free or tributary trigger is yes</li><li>original yanszin:</li><ul><li>type is all</li><li>owned by is this nation</li></ul> | <li>override country name = Yanszin</li><li>hidden effect:</li><ul><li>set country flag [yanszin_unification](../flags/yanszin_unification.md)</li></ul><li>swap non generic missions = yes</li> | <li>capital scope:</li><ul><li>region is upper_yanshen_region</li></ul><li>Any of the following:</li><ul><li>Country is Y10</li><li>tag  is Y04</li><li>tag   is Y08</li><li>tag    is Y07</li><li>tag     is Y06</li></ul><li>None of the following:</li><ul><li>has country flag [yanszin_unification](../flags/yanszin_unification.md)</li></ul> |