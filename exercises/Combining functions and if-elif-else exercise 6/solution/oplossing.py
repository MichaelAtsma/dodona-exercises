def DagType(dag):
    if dag == "Zaterdag":
        dagtype = "Weekend"
    elif dag == "Zondag":
        dagtype = "Weekend"
    else:
        dagtype = "Weekdag"
    return dagtype