from VisualDetectionAPI import AGGripperControl

if __name__ == '__main__':
    dh_client=AGGripperControl()
    dh_client.dh_init(True)
    while True:
        print("请输入指令： cmd: num  a:结束")
        cmd = input()
        if cmd == 'a':
            break
        else:
            dh_client.control_gripper(int(cmd))
