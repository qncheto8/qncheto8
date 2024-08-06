import csv
import json
import tui


class DataViewer:
    def __init__(self, data):
        self.data = data

    def display_reviews_for_park(self, park):
        """Display all reviews for a specific park."""
        park_reviews = [review for review in self.data if review['Branch'] == park]
        if not park_reviews:
            tui.display_message(f"No reviews found for park: {park}")
        else:
            tui.display_message(f"Displaying reviews for {park}:")
            for review in park_reviews:
                tui.display_message(
                    f"Review ID: {review['Review_ID']}, Rating: {review['Rating']}, "
                    f"Reviewer: {review['Reviewer_Location']}"
                )

    def count_reviews_from_location(self, park, location):
        """Count and display the number of reviews from a specific location."""
        count = sum(
            1 for review in self.data if review['Branch'] == park and review['Reviewer_Location'] == location
        )
        tui.display_message(f"Number of reviews from {location} for {park}: {count}")

    def average_rating_for_year(self, park, year):
        """Calculate and display the average rating for a park in a specific year."""
        reviews = [
            review for review in self.data if review['Branch'] == park and review['Year_Month'].startswith(year)
        ]
        if not reviews:
            tui.display_message(f"No reviews found for {park} in year {year}.")
            return

        total_rating = sum(int(review['Rating']) for review in reviews)
        average_rating = total_rating / len(reviews)
        tui.display_message(f"Average rating for {park} in {year}: {average_rating:.2f}")

    def average_score_per_park_by_location(self):
        """Display the average score per park by reviewer location."""
        scores_by_location = {}

        for review in self.data:
            park = review['Branch']
            location = review['Reviewer_Location']
            rating = int(review['Rating'])

            if park not in scores_by_location:
                scores_by_location[park] = {}
            if location not in scores_by_location[park]:
                scores_by_location[park][location] = []
            scores_by_location[park][location].append(rating)

        for park, locations in scores_by_location.items():
            tui.display_message(f"\n{park}:")
            for location, scores in locations.items():
                average_score = sum(scores) / len(scores)
                tui.display_message(f"Location: {location}, Average Rating: {average_score:.2f}")

    def handle_sub_menu_a(self):
        """Handle the sub-menu for viewing data (Option A)."""
        while True:
            choice = tui.display_sub_menu_a()

            if choice == '1':
                park = tui.get_park_name()
                self.display_reviews_for_park(park)
            elif choice == '2':
                park = tui.get_park_name()
                location = tui.get_location_name()
                self.count_reviews_from_location(park, location)
            elif choice == '3':
                park = tui.get_park_name()
                year = tui.get_year()
                self.average_rating_for_year(park, year)
            elif choice == '4':
                self.average_score_per_park_by_location()
            elif choice == '5':
                break
            else:
                tui.display_error("Invalid choice. Please try again.")


class ParkDataExporter:
    def __init__(self, data, park):
        self.data = data
        self.park = park
        self.aggregated_data = self.aggregate_data()

    def aggregate_data(self):
        total_reviews = 0
        positive_reviews = 0
        total_score = 0
        countries = set()

        for review in self.data:
            if review['Branch'] == self.park:
                total_reviews += 1
                rating = int(review['Rating'])
                if rating >= 4:
                    positive_reviews += 1
                total_score += rating
                countries.add(review['Reviewer_Location'])

        if total_reviews > 0:
            average_score = total_score / total_reviews
        else:
            average_score = 0

        return {
            "Total Reviews": total_reviews,
            "Positive Reviews": positive_reviews,
            "Average Score": average_score,
            "Unique Countries": len(countries)
        }

    def export_to_txt(self, filename):
        with open(filename, 'w') as f:
            for key, value in self.aggregated_data.items():
                f.write(f"{key}: {value}\n")

    def export_to_csv(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.aggregated_data.keys())
            writer.writerow(self.aggregated_data.values())

    def export_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.aggregated_data, f, indent=4)


def load_data(filename):
    """Load data from a CSV file into a list of dictionaries."""
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        tui.display_message(f"Dataset loaded successfully. Total rows: {len(data)}")
        return data
    except FileNotFoundError:
        tui.display_error(f"The file '{filename}' was not found.")
        return []
