from facade.home_theater_facade import HomeTheaterFacade

def main():
    home_theater = HomeTheaterFacade()
    home_theater.watch_movie("Inception")
    home_theater.end_movie()

if __name__ == "__main__":
    main()
