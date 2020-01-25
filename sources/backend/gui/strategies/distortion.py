from sources.backend.camera.CameraPair import CameraPair


def distortion_loop(frames, lines, distorded):
    if not distorded:
        CameraPair.apply_corrections(frames)

    if lines:
        CameraPair.draw_horizontal_lines(frames)

    jpgs = CameraPair.make_blobs_from(frames)

    return jpgs
