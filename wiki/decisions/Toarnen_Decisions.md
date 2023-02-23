This is a list of all [decisions](decisions.md) in the category "Toarnen_Decisions"

| Decision | Completion requirements | Effects | Requirements to appear |
| ----- | ------ | ----- | ------ |
| <a name="toarnen_chess_training_mil">Chess Focus: Military Tactics</a><br />*Pawns, like infantry, are mostly used to defend the core of the chessboard but they can also be used to pressure the enemy : the Thorn-Pawns Attack, the Harpy Attack and the Modern Bennoni are good teachings that a strong defense can become a powerful attack.* | <li>has mil advisor 2 yes</li><li>custom trigger tooltip:</li><ul><li>tooltip is toarnen_ruler_before_training_tooltip</li><li>None of the following:</li><ul><li>has ruler flag [toarnen_ruler_after_training](../flags/toarnen_ruler_after_training.md)</li></ul></ul><li>mil power is at least 150</li><li>None of the following:</li><ul><li>mil is at least 6</li></ul><li>does not have regency</li> | <li>add mil power = -150</li><li>increase ruler mil effect = yes</li><li>set ruler flag [toarnen_ruler_after_training](../flags/toarnen_ruler_after_training.md)</li> | <li>has country flag [toarnen_unlock_chess_training](../flags/toarnen_unlock_chess_training.md)</li> |
| <a name="toarnen_chess_training_dip">Chess Focus: Diplomatic Cunning</a><br />*Chess is a game of exchange, not unlike negotiation. The King must always protected and never wander too far from his court. His guards can be sent to missions far away, and even be sacrificed, all for the greater gain of the King.* | <li>has dip advisor 2 yes</li><li>custom trigger tooltip:</li><ul><li>tooltip is toarnen_ruler_before_training_tooltip</li><li>None of the following:</li><ul><li>has ruler flag [toarnen_ruler_after_training](../flags/toarnen_ruler_after_training.md)</li></ul></ul><li>dip power is at least 150</li><li>None of the following:</li><ul><li>dip is at least 6</li></ul><li>does not have regency</li> | <li>add dip power = -150</li><li>increase ruler dip effect = yes</li><li>set ruler flag [toarnen_ruler_after_training](../flags/toarnen_ruler_after_training.md)</li> | <li>has country flag [toarnen_unlock_chess_training](../flags/toarnen_unlock_chess_training.md)</li> |
| <a name="toarnen_host_chess_contest">Host a Ruler's Chess Contest</a><br />*Toarnen must know that it is not ruled by a idiotic ruler, but that of Roilsardi blood granted with superior intelligence. Let's call other rulers to prove our might!* | <li>dip power is at least 50</li><li>treasury is at least 250</li><li>None of the following:</li><ul><li>has country modifier A57_toarnen_chess_tournament_cooldown</li></ul> | <li>add dip power = -50</li><li>add treasury = -250</li><li>the event [The Ruler's Chess Tournament](../events/the_ruler_s_chess_tournament.md) happens</li><li>country gets the modifier A57_toarnen_chess_tournament_cooldown for 10 years</li> | <li>has country flag [toarnen_unlock_chess_tournament](../flags/toarnen_unlock_chess_tournament.md)</li> |