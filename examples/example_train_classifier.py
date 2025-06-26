from VisualDetectionAPI import train_classifier

if __name__=='__main__':

    # FOR train
    train_classifier(
        train_path='train',
        test_path='',

        batch_size=8,
        epochs=200,
        classifier_names=["cat", "dog"],

        checkpoint_path='checkpoint',

        img_size=128,
        milestones=[0.5, 0.8, 0.9],
        warm=1,
        lr=1e-4,
        tensorboard=False

    )

