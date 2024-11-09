% LUCET (2413675)
% DELFORGE (2412494)

include "globals.mzn";

%-----------------------------------------------------------------------------%
% Données
%-----------------------------------------------------------------------------%

% Nombre d'acteurs et de rôles
int: n;
% Couleurs des costumes
enum costumes; 
% Costume démandé pour un rôle i (première dimension) par un acteur j (seconde dimension)
array[1..n,1..n] of costumes: choix_costume;

%-----------------------------------------------------------------------------%
% Variables de décisions
%-----------------------------------------------------------------------------%

% Variables de décision pour assigner un acteur à un rôle
array [1..n] of var 1..n: assignation_role;

%-----------------------------------------------------------------------------%
% Partie étudiant
%-----------------------------------------------------------------------------%

% 1 : S'assurer que deux acteurs différents n'ont pas le même rôle ou le même costume
constraint forall(i in 1..n, j in 1..n where i != j)(assignation_role[i] != assignation_role[j] \/ choix_costume[assignation_role[i], i] != choix_costume[assignation_role[j], j]);

% 2 : Vérification que les rôles donnés aux acteurs voisins ne sont pas adjacents
constraint forall(i in 1..(n-1))(abs(assignation_role[i] - assignation_role[i+1]) >= 2);

% 3 : Chaque acteur reçoit un rôle différent
constraint alldifferent(assignation_role);

% 4 : Chaque costume n'est utilisé qu'une seule fois
constraint forall(c in costumes)(sum(i in 1..n)(choix_costume[assignation_role[i], i] = c) = 1);

solve satisfy;
%-----------------------------------------------------------------------------%

output	
  ["L'acteur " ++ format(i) ++ 
   " prendra le rôle " ++ format(fix(assignation_role[i])) ++ 
   " (costume " ++ format(choix_costume[fix(assignation_role[i]), i]) ++ ")" ++"\n" 
  | i in 1..n];