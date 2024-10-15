interface Transforming {
    fun resize(zoom: Int)
    fun rotate(direction: RotateDirection, rotationCX: Int, rotationCY: Int)

    // Поворачиваем точку (x, y) вокруг точки (cx, cy) на заданный угол
    fun rotatePoint(x: Int, y: Int, cx: Int, cy: Int, angle: Int): Pair<Int, Int> {
        return when (angle) {
            90 -> Pair(cx - (y - cy), cy + (x - cx))   // против часовой стрелки
            -90 -> Pair(cx + (y - cy), cy - (x - cx))  // по часовой стрелке
            else -> throw IllegalArgumentException("Угол должен быть 90 или -90 градусов")
        }
    }

}

enum class RotateDirection {
    // направление вращения фигуры на 90 градусов
    Clockwise, CounterClockwise
}
