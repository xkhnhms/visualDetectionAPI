from VisualDetectionAPI import infer_classifierRN
import cv2

if __name__=='__main__':

    model_path = 'best_epoch_38_0.99.pth'
    
    classifier_names =["cat", "dog"]
                        
    # for infer 
    img=cv2.imread('4474192_rgb_region.png')
    infer_classifier = infer_classifierRN(model_path,classifier_names,img_size=224)
    pred_label,perc = infer_classifier.infer(img)
    print('pred_label,perc: ',pred_label,perc)


