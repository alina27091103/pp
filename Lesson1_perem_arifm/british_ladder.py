steps_in_part=0
floor=0
total_seconds=0
PARTS_IN_FIOOR=2
SEC_LIVE_IN_STEP=10
print("/n============/n")
print("Данная прогрмма считает на сколько секунд увеличится ваша жизнь при поднятии пешком на этаж на котором вы живете")
print()
steps_in_part=int(input("Ведите количество ступенек в пролете: "))
floor=int(input("Введите этаж на котором вы жиете: "))
total_seconds=steps_in_part*PARTS_IN_FIOOR*floor*SEC_LIVE_IN_STEP
print()
print(f"Ваша жизнь при поднятии на {floor} этаж увеличится на {total_seconds} секунд")
print("/n===========/n")