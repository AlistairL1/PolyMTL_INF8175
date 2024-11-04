import numpy as np

def solve(schedule):
    """
    Optimized solution using a local search algorithm to minimize conflicts.
    :param schedule: object describing the input (with courses and conflicts)
    :return: a dictionary of the form {course: time} where course is a course and time a time slot.
    """
    # Initialisation : assigner chaque cours au créneau initial 0
    courses = schedule.course_list
    conflicts = schedule.conflict_list
    max_time_slots = len(courses) // 2
    solution = {course: 0 for course in courses}

    # Fonction pour calculer le nombre de conflits
    def nb_conflits(solution):
        return sum(1 for course1, course2 in conflicts if solution[course1] == solution[course2])

    nb_conflits_actuel = nb_conflits(solution)
    amelioration = True

    while amelioration and nb_conflits_actuel > 0:
        amelioration = False
        for course in courses:
            creneau_actuel = solution[course]
            nb_conflits_tempo = nb_conflits_actuel
            for nouveau_creneau in range(max_time_slots):  # Essayer d'autres créneaux
                if nouveau_creneau != creneau_actuel:
                    solution[course] = nouveau_creneau
                    noubeau_nb_conflits = nb_conflits(solution)
                    if noubeau_nb_conflits < nb_conflits_tempo:
                        creneau_actuel = nouveau_creneau
                        nb_conflits_tempo = noubeau_nb_conflits
                        amelioration = True
                    # Pas besoin de revenir à l'état initial ici, car on applique directement le meilleur créneau
            solution[course] = creneau_actuel  # Appliquer le meilleur créneau trouvé
        nb_conflits_actuel = nb_conflits(solution)

    return solution

