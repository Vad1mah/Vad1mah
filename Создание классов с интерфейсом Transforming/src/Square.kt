class Square(var cx: Int, var cy: Int, var width: Int) : Movable, Figure(), Transforming {

    override fun move(dx: Int, dy: Int) {
        cx += dx; cy += dy
    }

    override fun resize(zoom: Int) {
        width += zoom
    }

    override fun rotate(direction: RotateDirection, rotationCX: Int, rotationCY: Int) {
        val angle: Int = when (direction) {
            RotateDirection.Clockwise -> 90
            RotateDirection.CounterClockwise -> -90
        }
        val (newX, newY) = rotatePoint(cx, cy, rotationCX, rotationCY, angle)

        cx = newX; cy = newY
    }

    override fun area(): Float {
        return (width * width).toFloat()
    }

    override fun toString(): String {
        return "Circle(cx=$cx, cy=$cy, width=$width)"
    }
}