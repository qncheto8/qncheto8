import process
import visual
import tui


def main():
    filename = 'disneyland_reviews.csv'
    data = process.load_data(filename)

    while True:
        choice = tui.display_main_menu()

        if choice == 'A':
            process_viewer = process.DataViewer(data)
            process_viewer.handle_sub_menu_a()
        elif choice == 'B':
            visualizer = visual.DataVisualizer(data)
            visualizer.handle_sub_menu_b()
        elif choice == 'C':
            park_name = tui.get_park_name()
            format_choice = tui.get_export_format()
            filename = tui.get_filename()
            exporter = process.ParkDataExporter(data, park_name)

            if format_choice == 'txt':
                exporter.export_to_txt(filename)
            elif format_choice == 'csv':
                exporter.export_to_csv(filename)
            elif format_choice == 'json':
                exporter.export_to_json(filename)
            else:
                tui.display_error("Invalid format choice. Please try again.")
        elif choice == 'D':
            tui.display_message("Exiting the program.")
            break
        else:
            tui.display_error("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
