from VisualDetectionAPI import test_classifierRN

if __name__=='__main__':

    # for test
    img_path = 'val'
    model_path = 'best_epoch_38_0.99.pth'
    classifier_names = ["cat","dog"]                
    results_output = test_classifierRN(
        img_path,
        model_path,
        classifier_names,
        img_size=224,
    )

    for file_name, result,perc in results_output:
        print('file_name:', file_name)
        print('predicted:', result)
        print('perc:', perc)

