def point_cloud_callback(self, cloud_msg):
    try:
        self.get_logger().info(
            f'POINT CLOUD RECEIVED | '
            f'Width: {cloud_msg.width} | '
            f'Height: {cloud_msg.height} | '
            f'Frame: {cloud_msg.header.frame_id}'
        )

        points = point_cloud2.read_points(
            cloud_msg,
            field_names=('x', 'y', 'z'),
            skip_nans=True
        )

        count = 0
        samples = []

        for point in points:
            count += 1

            if len(samples) < 5:
                samples.append(
                    (
                        float(point[0]),
                        float(point[1]),
                        float(point[2])
                    )
                )

        self.get_logger().info(
            f'Valid point count: {count}'
        )

        for i, (x, y, z) in enumerate(samples):
            self.get_logger().info(
                f'Point {i}: '
                f'x={x:.3f}, '
                f'y={y:.3f}, '
                f'z={z:.3f} m'
            )

    except Exception as e:
        self.get_logger().error(
            f'Point cloud error: {e}'
        )
