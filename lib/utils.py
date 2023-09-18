import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from PIL import Image
import numpy as np

def usemodel(model_path):
  model = tf.saved_model.load(f"{model_path}/saved_model")
  label_map_path = f"{model_path}/labels.pbtxt"
  label_map = label_map_util.load_labelmap(label_map_path)
  categories = label_map_util.convert_label_map_to_categories(label_map,
                                                               max_num_classes=13, 
                                                               use_display_name=True)
  return model , categories

def run (model ,categories, image_path , save_name , min_score_thresh=.2 ) : 
  category_index = label_map_util.create_category_index(categories)
  image = Image.open(image_path).convert("RGB")
  image_np = np.array(image)
  input_tensor = tf.convert_to_tensor(image_np)
  input_tensor = input_tensor[tf.newaxis, ...]
  output_dict = model(input_tensor)
  num_detections = int(output_dict.pop('num_detections'))
  output_dict = {key: value[0, :num_detections].numpy() for key, value in output_dict.items()}
  output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
  viz_utils.visualize_boxes_and_labels_on_image_array(
                                                        image_np,
                                                        output_dict['detection_boxes'],
                                                        output_dict['detection_classes'],
                                                        output_dict['detection_scores'],
                                                        category_index,
                                                        use_normalized_coordinates=True,
                                                        max_boxes_to_draw=200,
                                                        min_score_thresh=min_score_thresh,
                                                        agnostic_mode=False)
  Imageresult = Image.fromarray(image_np)
  Imageresult.save(f"results/{save_name}.png")
