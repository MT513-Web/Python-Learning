import Day_31_json_logic

data = Day_31_json_logic.load_data("Day_31_my_data.json")

new_book = {"Title": "Namal", "Author": "Nimra Ahmad", "Price": 1500}
data["Book1"] = new_book

#save it back to file
print(Day_31_json_logic.save_data("Day_31_my_data.json", data))