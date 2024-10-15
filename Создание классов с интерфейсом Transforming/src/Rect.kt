// сочетание определения класса и конструктора одновременно объявляет переменные и задаёт их значения
class Rect(var cx: Int, var cy: Int, var width: Int, var height: Int) : Movable, Figure(), Transforming {

    var color: Int = -1 // при объявлении каждое поле нужно инициализировать

    lateinit var name: String // значение на момент определения неизвестно (только для объектных типов)
    // дополнительный конструктор вызывает основной
    constructor(rect: Rect) : this(rect.cx, rect.cy, rect.width, rect.height)

    override fun move(dx: Int, dy: Int) {
        cx += dx; cy += dy
    }

    override fun resize(zoom: Int) {
        width += zoom; height += zoom
    }

    override fun rotate(direction: RotateDirection, rotationCX: Int, rotationCY: Int) {
        val angle: Int = when (direction) {
            RotateDirection.Clockwise -> 90
            RotateDirection.CounterClockwise -> -90
        }
        val (newX, newY) = rotatePoint(cx, cy, rotationCX, rotationCY, angle)

        cx = newX; cy = newY
    }

    // для каждого класса area() определяется по-своему
    override fun area(): Float {
        return (width * height).toFloat() // требуется явное приведение к вещественному числу
    }

    override fun toString(): String {
        return "Rect(cx=$cx, cy=$cy, width=$width, height=$height)"
    }
}