#Information
 - Title: Missing localisation: racial_pop_events_elven_0_t
 - ID: racial_pop_events_elven.0
#Description

#Mean Time to Happen:
Base time = 1 days

#Options

___
##Missing localisation: racial_pop_events_elven_0_a

###One of the following randomly happens:
Outcome 1:

Available if <li>None of the following:</li><ul><li>has country modifier elven_administration</li></ul><li>any owned province:</li><ul><li>None of the following:</li><ul><li>local autonomy is at least 50</li></ul><li>is not a capital</li><li>has elven minority trigger yes</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Elven Minorities Demand Representation](../events/elven_minorities_demand_representation.md) happens</li></ul>
Outcome 2:

Available if <li>None of the following:</li><ul><li>has country modifier elven_administration</li></ul><li>Any of the following:</li><ul><li>stability is at least 1</li><li>is in golden age</li><li>ruler has personality is tolerant_personality</li><li>ruler has personality  is kind_hearted_personality</li><li>ruler has personality   is benevolent_personality</li><li>has idea group humanist_ideas</li><li>any ally:</li><ul><li>has country modifier elven_administration</li></ul></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Increase of Elven Tolerance](../events/increase_of_elven_tolerance.md) happens</li></ul>
Outcome 3:

Available if <li>None of the following:</li><ul><li>has country modifier elven_administration</li></ul><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>stability is at least 0</li></ul><li>is bankrupt</li><li>inflation is at least 25</li><li>All of the following:</li><ul><li>is at war</li><li>None of the following:</li><ul><li>war score is at least 20</li></ul></ul><li>war exhaustion is at least 10</li><li>ruler has personality is cruel_personality</li><li>ruler has personality  is malevolent_personality</li><li>ruler has personality   is conqueror_personality</li><li>any rival country:</li><ul><li>has country modifier elven_administration</li></ul></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Decrease of Elven Tolerance](../events/decrease_of_elven_tolerance.md) happens</li></ul>
Outcome 4:

Available if <li>any owned province:</li><ul><li>has small elven minority trigger yes</li><li>Any of the following:</li><ul><li>is prosperous</li><li>development is at least 20</li></ul></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Elven Minority Grows](../events/elven_minority_grows.md) happens</li></ul>
Outcome 5:

Available if <li>any owned province:</li><ul><li>has elven minority trigger yes</li><li>Any of the following:</li><ul><li>unrest is at least 15</li><li>devastation is at least 50</li><li>has oppressed elven minority trigger yes</li></ul></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Elven Minority Dwindles](../events/elven_minority_dwindles.md) happens</li></ul>
Outcome 6:

Available if <li>num of cities is at least 2</li><li>any owned province:</li><ul><li>has elven minority trigger yes</li><li>Any of the following:</li><ul><li>devastation is at least 33</li><li>unrest is at least 10</li><li>None of the following:</li><ul><li>development is at least 10</li></ul></ul></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Internal Migration of Elven Minority](../events/internal_migration_of_elven_minority.md) happens</li></ul>
Outcome 7:

Available if <li>num of cities is at least 2</li><li>any neighbor country:</li><ul><li>None of the following:</li><ul><li>low tolerance elven race trigger is yes</li></ul></ul><li>any owned province:</li><ul><li>has elven minority trigger yes</li><li>Any of the following:</li><ul><li>devastation is at least 33</li><li>unrest is at least 10</li><li>None of the following:</li><ul><li>development is at least 10</li></ul><li>has oppressed elven minority trigger yes</li></ul></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Elven Minorities Emigrate Elsewhere](../events/elven_minorities_emigrate_elsewhere.md) happens</li></ul>
Outcome 8:

Available if <li>num of cities is at least 2</li><li>any subject country:</li><ul><li>is colonial nation</li></ul><li>any owned province:</li><ul><li>has elven minority trigger yes</li><li>Any of the following:</li><ul><li>devastation is at least 33</li><li>unrest is at least 10</li><li>None of the following:</li><ul><li>development is at least 10</li></ul><li>has oppressed elven minority trigger yes</li></ul></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Elven Minority Migrates to Colony](../events/elven_minority_migrates_to_colony.md) happens</li></ul>
