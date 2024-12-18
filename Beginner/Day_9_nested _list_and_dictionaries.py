capitals = {
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bangalore"
}
travel_log = {
    "Tamil Nadu": ["Marina", "Kolli hills", "Yercaud"],
    "Karnataka": ["Mysore Palace", "Coorg", "Nandi hills"]
}
print(travel_log["Tamil Nadu"][1])
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])

travel_log = {
    "Tamil Nadu": {
        "cities_visited": ["Trichy", "Tenkasi", "Tirunelveli"],
        "total_visits": 5
    },
    "Karnataka": {
        "cities_visited": ["Mysore", "Coorg", "Hubili"],
        "total_visits": 4
    }
}
print(travel_log["Karnataka"]["cities_visited"][2])
