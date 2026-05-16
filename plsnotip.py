def totcal(tobill, tipper):
    totalam= tobill*(1+0.01*tipper)
    return totalam

print(totcal(500, 2000))