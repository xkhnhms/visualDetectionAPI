from VisualDetectionAPI import test_classifier

if __name__=='__main__':

    # for test
    results_output = test_classifier(
        img_path = 'val/cat/',
        model_path = 'epoch-best-acc_1.0.pth',
        classifier_names = ["cat","dog"],
        img_size=128,
    )
    for file_name, result,perc in results_output:
        print('file_name:', file_name)
        print('predicted:', result)
        print('perc:', perc)

