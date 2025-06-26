from VisualDetectionAPI import AuboRobot

if __name__ == '__main__':
    robot=AuboRobot("169.254.4.70")
    angle_cert_pose=robot.getTcpAnglePose()