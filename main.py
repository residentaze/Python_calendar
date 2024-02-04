from User import User
from Event import Event
from Calendar import Calendar




anar = User("Aнар", "6220702")
aynur = User("Айнур", "3992877")
alsu = User("Алсу", "123")
murad = User("Мурад", "123")
event_1 = Event("Собрание", aynur, "описание")
event_2 = Event("День рождения", aynur, "описание")

event_2.create_event("2024,02,03", "ежегодный")
event_1.create_event("2024,02,03", "ежегодный")

event_2.add_part(aynur, anar)
event_2.add_part(aynur, alsu)
event_2.add_part(aynur, murad)

event_2.participants_leavе(alsu)

event_2.del_participants(aynur, anar)

event_2.del_description(aynur)

event_2.change_description(aynur, "новое описание")

cal_1 = Calendar()
cal_1.add_event(event_2)
cal_1.add_event(event_1)
print(cal_1)
