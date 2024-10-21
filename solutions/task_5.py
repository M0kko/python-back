from datetime import datetime
def process_logs(
    logs: list[str]
) -> tuple[int, list[str], list[int], list[int], list[set[str]]]:
    """
        Функция обработки поступающих логов. Гарантируется, что записи в логах идут в хронологическом порядке.
        
        Возвращает следующий кортеж:
        1. Общее количество поставленных блоков всеми игроками
        2. Список ников игроков
        3. Список, хранящий общее время онлайна в секундах для каждого игрока в соответствии с предыдущим списком
        4. Список, хранящий общее кол-во поставленных блоков данным игроком
        5. Список из множеств названий достижений для каждого игрока
    """
    player_data = {}
    total_blocks = 0

    for log in logs:
        timestamp, player_event = log.split('] ')
        player_name, event_details = player_event.split(': ')
        event_name, *args = event_details.split(' ')
        player_name = player_name[1:-1]

        if player_name not in player_data:
            player_data[player_name] = {
                'online_time': 0,
                'blocks_placed': 0,
                'achivements': set(),
                'last_time': None
            }

        if event_name == 'connected':
            player_data[player_name]['last_time'] = timestamp
        elif event_name == 'disconnected':
            if player_data[player_name]['last_time']:
                start_time = player_data[player_name]['last_time']
                end_time = timestamp
                online_duration = (datetime.strptime(end_time+"]", "[%Y-%m-%d %H:%M:%S]") - 
                                   datetime.strptime(start_time+"]", "[%Y-%m-%d %H:%M:%S]")).total_seconds()
                player_data[player_name]['online_time'] += online_duration
                player_data[player_name]['last_time'] = None
        elif event_name == 'block_placed':
            player_data[player_name]['blocks_placed'] += 1
            total_blocks += 1
        elif event_name == 'achivement_unlocked':
            achievement_name = ' '.join(args)
            player_data[player_name]['achivements'].add(achievement_name)

    player_names = list(player_data.keys())
    online_times = [int(data['online_time']) for data in player_data.values()]
    blocks_placed = [data['blocks_placed'] for data in player_data.values()]
    achievements = [data['achivements'] for data in player_data.values()]

    return total_blocks, player_names, online_times, blocks_placed, achievements

print(process_logs([
    "[2024-10-05 20:10:00] [Steve]: connected",
    "[2024-10-05 20:11:30] [Steve]: block_placed 647, -100, 251",
    "[2024-10-05 20:12:10] [Steve]: block_placed 648, -100, 270",
    "[2024-10-05 20:15:00] [Alex]: connected",
    "[2024-10-05 20:15:01] [Steve]: block_placed 649, -100, 280",
    "[2024-10-05 20:16:15] [Alex]: achivement_unlocked taking_inventory",
    "[2024-10-05 20:16:30] [Alex]: block_placed 125, 424, -1265",
    "[2024-10-05 20:17:00] [Steve]: block_placed 10, 64, -30",
    "[2024-10-05 20:18:00] [Steve]: achivement_unlocked getting_an_upgrade",
    "[2024-10-05 20:20:40] [Steve]: disconnected",
    "[2024-10-05 20:21:10] [Alex]: achivement_unlocked benchmarking",
    "[2024-10-05 20:22:00] [Alex]: disconnected"
]))