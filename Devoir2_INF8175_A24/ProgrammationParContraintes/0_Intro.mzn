% LUCET (2413675)
% DELFORGE (2412494)

include "globals.mzn";

%-----------------------------------------------------------------------------%
% Variables de décisions
%-----------------------------------------------------------------------------%

% Nombre devant satisfaire les critères
var 1000..9999: nombre;

% Décomposition du nombre en un ensemble de chiffres
array[1..4] of var 1..9: chiffres;

%-----------------------------------------------------------------------------%
% Objectif
%-----------------------------------------------------------------------------%

% Variable à minimiser
var int: p;

%-----------------------------------------------------------------------------%
% Partie étudiant
%-----------------------------------------------------------------------------%
% 1 : C'est un nombre pair
constraint chiffres[4] mod 2 = 0;

% 2 : Il n'y a pas de 0 dans le nombre
constraint forall(i in 1..4)(chiffres[i] != 0);

% 3 : Tous les chiffres sont différents
constraint alldifferent(chiffres);

% 4 : Le chiffre des milliers est supérieur à celui des centaines
constraint chiffres[1] > chiffres[2];

% 5 : Le chiffre des dizaines est inférieur à celui des unités
constraint chiffres[3] < chiffres[4];

% 6 : Le chiffre des centaines est supérieur à celui des unités
constraint chiffres[2] > chiffres[4];

% 7 : La somme des quatre chiffres este supérieure à 15
constraint sum(i in 1..4)(chiffres[i]) > 15;


% 8 : Minimiser le produit des trois derniers chiffres
p = product(i in 2..4)(chiffres[i]);
solve minimize p;

nombre = sum(i in 1..4)(chiffres[i]*10^(4-i));
%-----------------------------------------------------------------------------%

output [
  show(nombre)
];

