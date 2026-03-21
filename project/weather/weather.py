import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os


def fetch_weather_data(latitude, longitude, days=7):
    """Fetch historical weather data from Open-Meteo API."""
    today = datetime.now()
    start = today - timedelta(days=days)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start.strftime("%Y-%m-%d"),
        "end_date": today.strftime("%Y-%m-%d"),
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def process_weather_data(data):
    """Convert API response to pandas DataFrame."""
    daily = data["daily"]

    df = pd.DataFrame(
        {
            "date": pd.to_datetime(daily["time"]),
            "max_temp": daily["temperature_2m_max"],
            "min_temp": daily["temperature_2m_min"],
            "precipitation": daily["precipitation_sum"],
        }
    )

    # Calculate derived columns
    df["avg_temp"] = (df["max_temp"] + df["min_temp"]) / 2
    df["temp_range"] = df["max_temp"] - df["min_temp"]

    return df


def create_visualization(df, city_name, output_file="weather_chart.png"):
    """Create and save weather visualization."""
    plt.figure(figsize=(12, 6))

    # Temperature plot
    plt.plot(
        df["date"], df["max_temp"], "r-o", label="Max Temp", linewidth=2, markersize=6
    )
    plt.plot(
        df["date"], df["min_temp"], "b-o", label="Min Temp", linewidth=2, markersize=6
    )
    plt.plot(df["date"], df["avg_temp"], "g--", label="Average", linewidth=2)

    # Styling
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.title(f"{city_name} Weather - Past Week", fontsize=14, fontweight="bold")
    plt.legend(loc="best")
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Chart saved to {output_file}")


def print_statistics(df):
    """Print weather statistics."""
    print("\n" + "=" * 50)
    print("WEATHER STATISTICS")
    print("=" * 50)

    print("\nTemperature:")
    print(f"  Average Max: {df['max_temp'].mean():.1f}°C")
    print(f"  Average Min: {df['min_temp'].mean():.1f}°C")
    print(f"  Overall Average: {df['avg_temp'].mean():.1f}°C")
    print(f"  Hottest: {df['max_temp'].max():.1f}°C")
    print(f"  Coldest: {df['min_temp'].min():.1f}°C")

    print("\nPrecipitation:")
    print(f"  Total: {df['precipitation'].sum():.1f}mm")
    print(f"  Rainy Days: {(df['precipitation'] > 0).sum()}")

    # Find extreme days
    hottest = df.loc[df["max_temp"].idxmax()]
    coldest = df.loc[df["min_temp"].idxmin()]

    print("\nExtreme Days:")
    print(
        f"  Hottest: {hottest['date'].strftime('%Y-%m-%d')} ({hottest['max_temp']:.1f}°C)"
    )
    print(
        f"  Coldest: {coldest['date'].strftime('%Y-%m-%d')} ({coldest['min_temp']:.1f}°C)"
    )


def save_data(df, output_file="weather_data.csv"):
    """Save DataFrame to CSV."""
    # Create directory if needed
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")


def main():
    """Main execution function."""
    # City coordinates
    cities = {
        "Kathmandu": (27.7172, 85.3240),
        "Pokhara": (28.2096, 83.9856),
        "Paris": (48.8566, 2.3522),
    }

    city_name = "Kathmandu"
    latitude, longitude = cities[city_name]

    print(f"Fetching weather data for {city_name}...")

    # Fetch data
    data = fetch_weather_data(latitude, longitude, days=7)
    if not data:
        return

    # Process
    df = process_weather_data(data)

    # Analyze
    print_statistics(df)

    # Visualize
    create_visualization(df, city_name, "data/weather_chart.png")

    # Save
    save_data(df, "data/weather_data.csv")

    print("\n All done!")


if __name__ == "__main__":
    main()
    3
