from VisualDetectionAPI import train_classifierRN

if __name__=='__main__':

    train_path = 'train'
    test_path = 'val'
    classifier_names =["cat", "dog"]
                        
    # for train
    train_classifierRN(
        train_path,
        test_path,

        classifier_names,

        results_dir='results',

        batch_size=8,
        epochs=200,
        num_workers=4,

        img_size=256,
        lr=1e-3,
        model_name='classifierRN',
    )

