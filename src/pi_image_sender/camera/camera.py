import time

import picamera

from .process_output import ProcessOutput


def start_sending(resolution: str = "VGA", format: str = "mjpeg") -> None:
    with picamera.PiCamera(resolution=resolution) as camera:
        camera.start_preview()
        time.sleep(2)
        output = ProcessOutput()
        camera.start_recording(output, format=format)
        while not output.done:
            camera.wait_recording(1)
        camera.stop_recording()
