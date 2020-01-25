from sources.camera.CameraPair import CameraPair

def initialization_loop(frames, lines):

    if lines:
        CameraPair.draw_horizontal_lines(frames)

    jpgs = CameraPair.make_blobs_from(frames)

    return jpgs




