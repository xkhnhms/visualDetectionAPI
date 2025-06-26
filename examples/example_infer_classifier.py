from VisualDetectionAPI import infer_classifier
import cv2

if __name__=='__main__':

    # for infer 
    model_path = 'epoch-best-acc_1.0.pth'
    classifier_names =["cat","dog"]               
    classifier = infer_classifier(model_path,classifier_names,img_size=128)
    
    img=cv2.imread('4474192_rgb_region.png')
  
    pred_label,perc = classifier.infer(img)
    print('pred_label,perc: ',pred_label,perc)
