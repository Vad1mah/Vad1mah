fun main() {

    val r = Rect(2, 2, 4, 5)
    print("Текущие свойства прямоугольника: $r")

    val rotationPointX = 10
    val rotationPointY = 10

    println("\nПоворот")
    for (i in 0 until 4) {
        r.rotate(RotateDirection.CounterClockwise, rotationPointX, rotationPointY)
        println("После поворота: $r")
    }

    println("\nПеремещение")
    r.move(22, -55); println(r)
    r.move(-18, 42); println(r)

    println("\nМасштабирование")
    r.resize(10); println(r)
    r.resize(-15); println(r)


    val c = Circle(3, 5, 5)
    print("\nТекущие свойства круга: $c")

    println("\nПоворот")
    for (i in 0..3) {
        c.rotate(RotateDirection.CounterClockwise, 22, 22)
        println(c)
    }

    println("\nПеремещение")
    c.move(-28, -10); println(c)
    c.move(50, 11); println(c)

    println("\nМасштабирование")
    c.resize(-5); println(c)
    c.resize(13); println(c)


    val s = Square(4, 4, 2)
    print("\nТекущие свойства квадрата: $s")

    println("\nПоворот")
    for (i in 0..3) {
        c.rotate(RotateDirection.Clockwise, 1, 5)
        println(s)
    }
    println("\nПеремещение")
    c.move(5, 16); println(s)
    c.move(-22, 37); println(s)

    println("\nМасштабирование")
    c.resize(1); println(s)
    c.resize(-2); print(s)
}