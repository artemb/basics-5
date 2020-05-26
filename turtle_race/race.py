from turtle_race._lib import Race

race = Race()

turtle1 = race.new_turtle()
turtle2 = race.new_turtle()
turtle3 = race.new_turtle()
turtle4 = race.new_turtle()
turtle5 = race.new_turtle()

turtle1.set_speed(50)
turtle2.set_speed(50)
turtle3.set_speed(50)
turtle4.set_speed(50)
turtle5.set_speed(50)

# Коричневая, Синяя, Фиолетовая, Зеленая, Красная

race.run()