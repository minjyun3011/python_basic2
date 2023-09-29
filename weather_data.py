def main():
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]
    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    total_temperature = sum(info["temperature"]for info in weather_information)
    print(f"全国の平均気温:{total_temperature / len(weather_information): .1f}℃")
    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    osaka_station = [info['station']for info in weather_information if info['prefecture'] == '大阪府']
    osaka_stations_str = ','.join(osaka_station)
    print(f"大阪府の駅名:{osaka_stations_str}")
    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fukuoka_temperature = [info['temperature'] for info in weather_information if info['prefecture'] == '福岡県']
    print(f'福岡県の平均気温: {sum(fukuoka_temperature) / len(fukuoka_temperature):.1f}℃')


if __name__ == '__main__':
    main()
