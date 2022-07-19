python tools/infer.py \
--weights /root/YOLOv6/runs/train/exp/weights/31.pt \
--source /root/YOLOv6/data_test/images/test \
--yaml data/dataset.yaml \
--save-txt \
--conf-thres 0.6 \