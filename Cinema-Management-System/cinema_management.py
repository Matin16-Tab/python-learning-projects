movies = [
    {
        "id":1,
        "name":"Inception",
        "genre":"Sci-Fi",
        "duration":148,
        "age_rating":13
    },
    {
        "id":2,
        "name":"Interstellar",
        "genre":"Sci-Fi",
        "duration":169,
        "age_rating":13
    },
    {
        "id":3,
        "name":"The Dark Knight",
        "genre":"Action",
        "duration":152,
        "age_rating":13
    },
    {
        "id":4,
        "name":"The Green Mile",
        "genre":"Drama",
        "duration":189,
        "age_rating":16
    },
    {
        "id":5,
        "name":"Coco",
        "genre":"Animation",
        "duration":105,
        "age_rating":7
    },
    {
        "id":6,
        "name":"Parasite",
        "genre":"Thriller",
        "duration":132,
        "age_rating":16
    }
]

screenings = [
    {
        "id":1,
        "movie_id":1,
        "date":"2026-11-10",
        "time":"10:00",
        "ticket_price":120000,
        "capacity":100
    },
    {
        "id":2,
        "movie_id":2,
        "date":"2026-11-10",
        "time":"13:30",
        "ticket_price":140000,
        "capacity":80
    },
    {
        "id":3,
        "movie_id":3,
        "date":"2026-11-10",
        "time":"17:00",
        "ticket_price":150000,
        "capacity":120
    },
    {
        "id":4,
        "movie_id":4,
        "date":"2026-11-10",
        "time":"20:30",
        "ticket_price":160000,
        "capacity":90
    },
    {
        "id":5,
        "movie_id":5,
        "date":"2026-11-11",
        "time":"10:30",
        "ticket_price":100000,
        "capacity":100
    },
    {
        "id":6,
        "movie_id":6,
        "date":"2026-11-11",
        "time":"13:00",
        "ticket_price":130000,
        "capacity":80
    },
    {
        "id":7,
        "movie_id":1,
        "date":"2026-11-11",
        "time":"16:00",
        "ticket_price":150000,
        "capacity":100
    },
    {
        "id":8,
        "movie_id":2,
        "date":"2026-11-11",
        "time":"20:00",
        "ticket_price":170000,
        "capacity":80
    },
    {
        "id":9,
        "movie_id":3,
        "date":"2026-11-12",
        "time":"10:00",
        "ticket_price":130000,
        "capacity":120
    },
    {
        "id":10,
        "movie_id":4,
        "date":"2026-11-12",
        "time":"14:00",
        "ticket_price":130000,
        "capacity":90
    },
    {
        "id":11,
        "movie_id":5,
        "date":"2026-11-12",
        "time":"17:00",
        "ticket_price":110000,
        "capacity":100
    },
    {
        "id":12,
        "movie_id":6,
        "date":"2026-11-12",
        "time":"20:30",
        "ticket_price":160000,
        "capacity":80
    }
]

reservations = [
    {
        "id":1,
        "screening_id":1,
        "customer_name":"Ali",
        "seat_number":12
    },
    {
        "id":2,
        "screening_id":1,
        "customer_name":"Sara",
        "seat_number":15
    },
    {
        "id":3,
        "screening_id":1,
        "customer_name":"Matin",
        "seat_number":20
    },
    {
        "id":4,
        "screening_id":2,
        "customer_name":"Reza",
        "seat_number":8
    },
    {
        "id":5,
        "screening_id":2,
        "customer_name":"Nima",
        "seat_number":14
    },
    {
        "id":6,
        "screening_id":3,
        "customer_name":"Arman",
        "seat_number":25
    },
    {
        "id":7,
        "screening_id":3,
        "customer_name":"Sara",
        "seat_number":30
    },
    {
        "id":8,
        "screening_id":5,
        "customer_name":"Matin",
        "seat_number":10
    }
]

reservation_id_tracker = {"next_id": 9}
def count_reservations(reservations, screening_id):
    total_reservation = 0
    for reserve in reservations:
        if reserve["screening_id"] == screening_id:
            total_reservation += 1
    return total_reservation

def is_seat_available(reservations, screening_id, seat_number):
    is_available = True
    for reserve in reservations:
        if reserve["screening_id"] == screening_id and reserve["seat_number"] == seat_number:
            is_available = False
    return is_available

def has_available_capacity(reservations, screening):
    available_capacity = False
    reserved_seats_count = count_reservations(reservations, screening["id"])
    if screening["capacity"] > reserved_seats_count:
        available_capacity = True
    return available_capacity

def reserve_ticket(reservations, screening, customer_name, seat_number, reservation_id_tracker):
    if 1 <= seat_number <= screening["capacity"]:
        available_capacity_screening = has_available_capacity(reservations, screening)

        if available_capacity_screening:
            available_seat = is_seat_available(
                reservations, screening["id"], seat_number
            )

            if available_seat:
                add_reserve = {
                    "id": reservation_id_tracker["next_id"],
                    "customer_name": customer_name,
                    "screening_id": screening["id"],
                    "seat_number": seat_number
                }

                reservations.append(add_reserve)
                reservation_id_tracker["next_id"] += 1

                return add_reserve

    return None

def cancel_reservation(reservations, reservation_id):
    for reservation in reservations:
        if reservation["id"] == reservation_id:
            reservations.remove(reservation)
            return reservation
    
def search_movie(movies, search_query):
    matched_movies = []
    for movie in movies:
        if search_query.lower() in movie["name"].lower():
            matched_movies.append(movie)
    return matched_movies

def group_movies_by_genre(movies):
    genres = {}
    for movie in movies:
        genre = movie["genre"]
        if genre in genres:
            genres[genre].append(movie["name"])
        else:
            genres[genre] = []
            genres[genre].append(movie["name"])
    return genres

def get_movie_details(movies, screenings, movie_name):
    movie_details = {}
    selected_movie = None
    for movie in movies:
        if movie["name"].lower() == movie_name.lower():
            selected_movie = movie
            movie_details["name"] = movie["name"]
            movie_details["genre"] = movie["genre"]
            movie_details["duration"] = movie["duration"]
            movie_details["age_rating"] = movie["age_rating"]
    if selected_movie == None:
        return None
    movie_screenings = []
    for screening in screenings:
        if screening["movie_id"] == selected_movie["id"]:
            movie_screenings.append(screening)
    movie_details["screenings"] = movie_screenings
    return movie_details

def calculate_screening_revenue(reservations, screening):
   total_reservations = count_reservations(reservations, screening["id"])
   total_screening_revenue = total_reservations * screening["ticket_price"]
   return total_screening_revenue

def calculate_total_revenue(reservations, screenings):
    total_revenue = 0
    for screening in  screenings:
        screening_revenue = calculate_screening_revenue(reservations, screening)
        total_revenue += screening_revenue
    return total_revenue

def rank_movies_by_tickets(movies, screenings, reservations):
    ranked_movies = []

    for movie in movies:
        movie_copy = movie.copy()
        total_ticket = 0

        for screening in screenings:
            if screening["movie_id"] == movie["id"]:
                total_ticket += count_reservations(
                    reservations, screening["id"]
                )

        movie_copy["reserved_ticket_count"] = total_ticket
        ranked_movies.append(movie_copy)

    ranked_movies = sorted(
        ranked_movies,
        key=lambda movie: movie["reserved_ticket_count"],
        reverse=True
    )

    return ranked_movies
    
def get_available_screenings(screenings, reservations):
    free_screenings = []
    for screening in screenings:
        available_capacity = has_available_capacity(reservations, screening)
        if available_capacity == True:
            free_screenings.append(screening)
    return free_screenings

def get_cinema_statistics(movies, screenings, reservations):
    statistics = {}
    statistics["movies_count"] = len(movies)
    statistics["screenings_count"] = len(screenings)
    statistics["reservations_count"] = len(reservations)
    total_capacity = 0
    for screening in screenings:
        total_capacity += screening["capacity"]
    statistics["available_seats"] = total_capacity - statistics["reservations_count"]
    statistics["total_capacity"] = total_capacity
    full_screenings_count = 0
    for screening in screenings:
        reserved_count = count_reservations(reservations, screening["id"])
        if reserved_count >= screening["capacity"]:
            full_screenings_count += 1
    statistics["full_screenings_count"] = full_screenings_count
    statistics["total_revenue"] = calculate_total_revenue(reservations, screenings)
    if total_capacity > 0:
        statistics["occupancy_rate"] = (statistics["reservations_count"] / total_capacity) * 100
    else:
        statistics["occupancy_rate"] = 0
    available_screenings = get_available_screenings(screenings, reservations)
    statistics["available_screenings"] = len(available_screenings)
    if len(screenings) > 0:
        total_revenue = statistics["total_revenue"]
        statistics["average_screening_revenue"] = total_revenue / len(screenings)
    else:
        statistics["average_screening_revenue"] = 0
    return statistics

def display_movies(movies, screenings, reservations):
    sorted_movies = rank_movies_by_tickets(movies, screenings, reservations)
    for movie in sorted_movies:
        print(movie["name"])
        print(movie["genre"])
        print(movie["duration"])
        print(movie["age_rating"])
        print(movie["reserved_ticket_count"])
