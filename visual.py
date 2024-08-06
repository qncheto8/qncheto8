import calendar
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import tui


class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def pie_chart_reviews_by_park(self):
        """Display a pie chart showing the number of reviews for each park."""
        park_counts = Counter(review['Branch'] for review in self.data)
        parks = list(park_counts.keys())
        counts = list(park_counts.values())

        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=parks, autopct='%1.1f%%', startangle=140)
        plt.title('Number of Reviews by Park')
        plt.axis('equal')
        plt.show()

    def bar_chart_average_scores(self):
        """Display a bar chart of average review scores for each park."""
        park_scores = {}

        for review in self.data:
            park = review['Branch']
            rating = int(review['Rating'])
            if park not in park_scores:
                park_scores[park] = []
            park_scores[park].append(rating)

        parks = list(park_scores.keys())
        averages = [sum(scores) / len(scores) for scores in park_scores.values()]

        plt.figure(figsize=(10, 12))
        plt.bar(parks, averages, color='skyblue')
        plt.title('Average Review Scores by Park')
        plt.xlabel('Park')
        plt.ylabel('Average Score')
        plt.ylim(0, 5)

        plt.xticks(rotation=45)
        plt.show()

    def top_10_locations_for_park(self, park):
        """Display a bar chart of the top 10 locations with the highest average rating for a park."""
        location_scores = {}

        for review in self.data:
            if review['Branch'] == park:
                location = review['Reviewer_Location']
                rating = int(review['Rating'])
                if location not in location_scores:
                    location_scores[location] = []
                location_scores[location].append(rating)

        average_scores = {location: sum(scores) / len(scores) for location, scores in location_scores.items()}
        top_10 = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)[:10]

        locations, scores = zip(*top_10)

        plt.figure(figsize=(12, 14))
        plt.bar(locations, scores, color='orange')
        plt.title(f'Top 10 Locations by Average Rating for {park}')
        plt.xlabel('Location')
        plt.ylabel('Average Rating')
        plt.ylim(0, 5)
        plt.xticks(rotation=45)
        plt.show()

    def average_rating_by_month(self, park):
        """Display a bar chart showing the average rating by month for a park."""
        monthly_scores = {month: [] for month in range(1, 13)}  # Initialize dictionary for months

        for review in self.data:
            if review['Branch'] == park:
                year_month = review['Year_Month']

                # Skip records with invalid or missing Year_Month
                if not year_month or '-' not in year_month:
                    continue

                try:
                    # Ensure the date is valid
                    date_obj = datetime.strptime(year_month, "%Y-%m")
                except ValueError:
                    # Skip invalid dates
                    continue

                rating = int(review['Rating'])
                month = date_obj.month  # Extract month
                monthly_scores[month].append(rating)

        # Calculate averages
        averages = []
        for month in range(1, 13):
            if monthly_scores[month]:
                avg_rating = sum(monthly_scores[month]) / len(monthly_scores[month])
            else:
                avg_rating = 0
            averages.append(avg_rating)

        # Prepare months for x-axis
        months = [calendar.month_name[i] for i in range(1, 13)]

        # Plot the bar chart
        plt.figure(figsize=(15, 15))
        plt.bar(months, averages, color='skyblue')
        plt.title(f'Average Rating by Month for {park}')
        plt.xlabel('Month')
        plt.ylabel('Average Rating')
        plt.ylim(0, 5)

        plt.grid(True, axis='y', linestyle='--', linewidth=0.7)
        plt.xticks(rotation=45)
        plt.show()

    def handle_sub_menu_b(self):
        """Handle the sub-menu for visualizing data (Option B)."""
        while True:
            choice = tui.display_sub_menu_b()

            if choice == '1':
                self.pie_chart_reviews_by_park()
            elif choice == '2':
                self.bar_chart_average_scores()
            elif choice == '3':
                park = tui.get_park_name()
                self.top_10_locations_for_park(park)
            elif choice == '4':
                park = tui.get_park_name()
                self.average_rating_by_month(park)
            elif choice == '5':
                break
            else:
                tui.display_error("Invalid choice. Please try again.")
