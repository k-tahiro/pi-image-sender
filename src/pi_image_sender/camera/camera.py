import time

import picamera

from .image_processor import ImageProcessor
from .process_output import ProcessOutput


def start_sending(
    resolution: str = "VGA",
    format: str = "mjpeg",
    processor_class=ImageProcessor,
    n_threads: int = 4,
) -> None:
    with picamera.PiCamera(resolution=resolution) as camera:
        camera.start_preview()
        time.sleep(2)
        output = ProcessOutput(processor_class, n_threads=n_threads)
        camera.start_recording(output, format=format)
        while not output.done:
            camera.wait_recording(1)
        camera.stop_recording()
