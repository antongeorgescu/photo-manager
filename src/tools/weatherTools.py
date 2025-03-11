def format_weather_data(data):
    """Formats the weather data for display."""
    formatted_data = f"Weather Report:\n"
    formatted_data += f"Location: {data['location']}\n"
    formatted_data += f"Temperature: {data['temperature']}°C\n"
    formatted_data += f"Condition: {data['condition']}\n"
    return formatted_data


def parse_weather_response(response):
    """Parses the weather API response."""
    return {
        "location": response.get("name"),
        "temperature": response.get("main", {}).get("temp"),
        "condition": response.get("weather", [{}])[0].get("description"),
    }