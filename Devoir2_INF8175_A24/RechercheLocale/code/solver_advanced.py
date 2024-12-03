# LUCET (2413675)
# DELFORGE (2412494)

def solve(schedule):
    """
    Optimized solution using a local search algorithm to minimize conflicts.
    :param schedule: object describing the input (with courses and conflicts)
    :return: a dictionary of the form {course: time} where course is a course and time a time slot.
    """
    def nb_conflits(sol):
        return sum(1 for c1, c2 in conflicts if sol[c1] == sol[c2])

    # Initialisation : assigner chaque cours au créneau initial 0
    courses = list(schedule.course_list)
    conflicts = list(schedule.conflict_list)
    max_creneaux = len(courses)
    solution = {c: 0 for c in courses}

    nb_conflits_actuel = nb_conflits(solution)
    amelioration = True

    while amelioration and nb_conflits_actuel > 0:
        amelioration = False
        for c in courses:
            creneau_actuel = solution[c]
            nb_conflits_horaire = nb_conflits_actuel

            for nouveau_creneau in range(max_creneaux):  # Essayer d'autres créneaux
                if nouveau_creneau != creneau_actuel:
                    solution[c] = nouveau_creneau
                    nouveau_nb_conflits = nb_conflits(solution) # Calcul du nouveau nombre de conflits avec ce nouveau créneau
                    if nouveau_nb_conflits < nb_conflits_horaire:
                        creneau_actuel = nouveau_creneau
                        nb_conflits_horaire = nouveau_nb_conflits
                        amelioration = True

            solution[c] = creneau_actuel  # Appliquer le meilleur créneau trouvé
            nb_conflits_actuel = nb_conflits(solution)

    return solution
