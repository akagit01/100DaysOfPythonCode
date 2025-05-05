def life_in_weeks(age):
    # if you lived for 90 yrs
    years_left = 90 - age
    total_weeks_in_a_year = round(365 / 7)
    weeks_left = years_left * total_weeks_in_a_year
    days_left = years_left*365

    print(f"you have {weeks_left} weeks left and {days_left}")


life_in_weeks(35)