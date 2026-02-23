def ft_count_harvest_recursive(days: int = None) -> None:
    if days is None:
        days: int = int(input("Days until harvest: "))
        ft_count_harvest_recursive(days)
        print("Harvest time!")
    if days > 1:
        ft_count_harvest_recursive(days - 1)
    print(f"Day {days}")

ft_count_harvest_recursive()