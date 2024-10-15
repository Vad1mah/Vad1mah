class Circle(var cx: Int, var cy: Int, var r: Int) : Movable, Figure(), Transforming {

    override fun move(dx: Int, dy: Int) {
        cx += dx; cy += dy
    }

    override fun resize(zoom: Int) {
        r += zoom
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
        return (Math.PI * r * r).toFloat()
    }

    override fun toString(): String {
        return "Circle(cx=$cx, cy=$cy, r=$r)"
    }
}