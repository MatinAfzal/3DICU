from OpenGL.GL import GL_LINES


## World settings
WORLD_COLOR_R = 0.5
WORLD_COLOR_G = 0.5
WORLD_COLOR_B = 0.5
WORLD_COLOR_A = 0.5

## World axes settings
WORLD_AXES_VERTICES = [[-100, 0, 0], [100, 0, 0], [0, -100, 0], [0, 100, 0], [0, 0, -100], [0, 0, 100]]
WORLD_AXES_COLORS = [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]]
WORLD_AXES_DRAWTYPE = GL_LINES

## Chunk settings
CHUNK_COLOR_R = 1
CHUNK_COLOR_G = 1
CHUNK_COLOR_B = 1

## Camera settings
CAMERA_MOUSE_SENSITIVITY_X = 0.1
CAMERA_MOUSE_SENSITIVITY_Y = 0.1
CAMERA_MOVE_SENSITIVITY = 0.31
CAMERA_VIEW_ANGLE = 60
CAMERA_NEAR_PLANE = 0.01
CAMERA_FAR_PLANE = 10000
CAMERA_ROTATE_YAW_LOCAL = True
CAMERA_ROTATE_PITCH_LOCAL = True
CAMERA_ROTATE_PITCHUP_MAX = 170.0
CAMERA_ROTATE_PITCHDOWN_MAX = 30

## Screen settings
# SCREEN_POS_X = 850
# SCREEN_POS_Y = 200
SCREEN_POS_X = 100
SCREEN_POS_Y = 30
# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_MULTISAMPLEBUFFERS = 1
SCREEN_MULTISAMPLESAMPLES = 4
SCREEN_DEPTH_SIZE = 24
SCREEN_CAPTION_LOADING = "Loading..."
SCREEN_CAPTION = "3DICU V [Any]"
SCREEN_MAX_FPS = 60