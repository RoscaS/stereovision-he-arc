from sources.backend.gui.api import GUI_MANAGER


if __name__ == '__main__':
    GUI_MANAGER.init_frontend_connection()
    GUI_MANAGER.main_loop()
