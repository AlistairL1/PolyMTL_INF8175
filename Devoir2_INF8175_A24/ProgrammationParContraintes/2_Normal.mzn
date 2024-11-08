% LUCET (2413675)
% DELFORGE (2412494)

include "globals.mzn"; 

%-----------------------------------------------------------------------------%
% Données
%-----------------------------------------------------------------------------%

% Nombre de tâches
int: n;
% Durée maximal du projet
int: m;
% Limite de ressources pouvant être partagées entre les tâches en cours
int: limite;

% Durée des tâches
array[1..n] of 1..m: duree_tache;
% Ressources requises par les tâches
array[1..n] of 1..m: ressource_tache;

%-----------------------------------------------------------------------------%
% Variables de décisions
%-----------------------------------------------------------------------------%

array[1..n] of var 1..m: debut_tache; % Début des tâches
array[1..n] of var 1..m: fin_tache; % Fin des tâches

%-----------------------------------------------------------------------------%
% Objectif
%-----------------------------------------------------------------------------%

% Fin du projet
var int: fin_projet;

%-----------------------------------------------------------------------------%
% Partie étudiant
%-----------------------------------------------------------------------------%
% 1. Calcul de la fin de chaque tâche
constraint forall(i in 1..n)(fin_tache[i] = debut_tache[i] + duree_tache[i]);

% 2. Contrainte pour la consommation d'énergie
constraint cumulative(debut_tache, duree_tache, ressource_tache, limite);

% 3. Limite des démarrages simultanés
constraint forall(v in debut_tache) (sum([1 | i in 1..n where debut_tache[i] = v]) <= 2);

% Minimiser la fin du projet
fin_projet = max(i in 1..n)(fin_tache[i]);
solve minimize fin_projet;
%-----------------------------------------------------------------------------%

output [
  "Envergure du projet  : ", show(fin_projet), "\n",
  "Début des tâches     : ", show(debut_tache), "\n",
  "Fin des tâches       : ", show(fin_tache), "\n",
];