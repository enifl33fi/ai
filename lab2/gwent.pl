% Fact: Type of cards
type('close combat').
type('ranged combat').
type('siege combat').
type('special').

% Fact: Special cards
card('biting frost').
card('clear weather').
card('impenetrable fog').
card('torrential rain').

% Fact: Close combat cards
card('redanian foot soldier').
card('poor fucking infantry').
card('siegfried of densele').
card('veron roche').

% Fact: Ranged combat cards
card('sabrina glevissig').
card('keira metz').
card('dethmold').
card('philippa elhart').

% Fact: Siege combat cards
card('thaler').
card('ballista').
card('trebuchet').
card('catapult').

% Fact: Type of characters
char_types('biting frost', 'special').
char_types('clear weather', 'special').
char_types('impenetrable fog', 'special').
char_types('torrential rain', 'special').

char_types('redanian foot soldier', 'close combat').
char_types('poor fucking infantry', 'close combat').
char_types('siegfried of densele', 'close combat').
char_types('veron roche', 'close combat').

char_types('sabrina glevissig', 'ranged combat').
char_types('keira metz', 'ranged combat').
char_types('dethmold', 'ranged combat').
char_types('philippa elhart', 'ranged combat').

char_types('thaler', 'siege combat').
char_types('ballista', 'siege combat').
char_types('trebuchet', 'siege combat').
char_types('catapult', 'siege combat').

% Fact: Strength of characters
char_power('redanian foot soldier', 1).
char_power('poor fucking infantry', 1).
char_power('siegfried of densele', 5).
char_power('veron roche', 10).

char_power('sabrina glevissig', 4).
char_power('keira metz', 5).
char_power('dethmold', 6).
char_power('philippa elhart', 10).

char_power('thaler', 1).
char_power('ballista', 6).
char_power('trebuchet', 6).
char_power('catapult', 8).

% Fact: Character with resistance to weather conditions
char_resistance('veron roche').
char_resistance('philippa elhart').

% Rules:

% Rule: is close combat affected by weather
close_weather_affected(SpecialCards) :-
    length(SpecialCards, N),
    N >= 0, N =< 4,
    \+ member('clear weather', SpecialCards),
    member('biting frost', SpecialCards).
% Rule: is ranged combat affected by weather
ranged_weather_affected(SpecialCards) :-
    length(SpecialCards, N),
    N >= 0, N =< 4,
    \+ member('clear weather', SpecialCards),
    member('impenetrable fog', SpecialCards).
% Rule: is siege combat affected by weather
siege_weather_affected(SpecialCards) :-
    length(SpecialCards, N),
    N >= 0, N =< 4,
    \+ member('clear weather', SpecialCards),
    member('torrential rain', SpecialCards).
% Rule: is character affected by weather
char_weather_affected(Char, SpecialCards) :-
    length(SpecialCards, N),
    N >= 0, N =< 4,
    \+ char_resistance(Char),
    \+ char_types(Char, 'special'),
    ((char_types(Char, 'close combat'), close_weather_affected(SpecialCards));
    (char_types(Char, 'ranged combat'), ranged_weather_affected(SpecialCards));
    (char_types(Char, 'siege combat'), siege_weather_affected(SpecialCards))).
% Rule: get character strength
character_strength(Char, Strength) :-
    char_power(Char, Strength).
character_strength(Char, DefaultStrength) :-
    \+ char_types(Char, _),
    DefaultStrength = 0.
character_strength(Char, Strength, SpecialCards) :-
    length(SpecialCards, N),
    N >= 0, N =< 4,
    (char_weather_affected(Char, SpecialCards), Strength = 1);
    char_power(Char, Strength).



