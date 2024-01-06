from Shipment.logger import logging
from Shipment.exception import shippingException
import sys
from Shipment.pipeline.training_pipeline import TrainPipeline

if __name__=="__main__":
    obj=TrainPipeline()
    obj.run_pipeline()