from sources.backend.gui.endpoints import GUI_MANAGER


if __name__ == '__main__':
    GUI_MANAGER.init_frontend_connection()
    GUI_MANAGER.start_loop()
