def DagDeel(uur):
    if uur < 6:
        dag_deel = "Nacht."
    elif uur < 12:
        dag_deel = "Ochtend."
    elif uur < 18:
        dag_deel = "Middag."
    else:
        dag_deel = "Avond."
    return dag_deel