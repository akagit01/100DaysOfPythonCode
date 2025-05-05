travel_log={
    "France":['Paris','Dijon','Lille'],
    "Germany":['Stuttgart','Berlin']
}

print(travel_log['France'][2])

nested_list=['A','B',['C','D']]
print(nested_list[2][1])

travel_log_dict={
    'France':{
        'num_times_visited':8,
        'cities_visited':['Paris','Dijon','Lille']
    },
    'Germany':{
        'num_times_visited':8,
        'cities_visited':['Stuttgart','Berlin']}
}

print(travel_log_dict['Germany']['cities_visited'][0])