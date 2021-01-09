if __name__=='__main__':
    print('This is module, not program!')
    input('Press enter to continue...')
else:
    from os import name as os_type
    if not str(os_type)=='nt':
        print('This module is only for windows, not for '+str(os_type)+'!')
        input('Press enter to continue...')
    else:
        from os import startfile as run_prog
        from os import environ as env
        from os import system as cmd_run
        from os import access as file_exists
        from os import F_OK as file_exists_params
        from os import remove as del_file
        from asyncio import sleep as async_time_sleep
        from time import sleep as time_sleep
        
        exe_name='iexplorer_api.exe'
        use_7_theme=True
        config='''
            :width
            1024
            :height
            768
            :min_width
            800
            :min_height
            600
            :align_x
            center
            :align_y
            center
            :custom_x
            100
            :custom_y
            100
            :alpha
            255
            :icon
            icons\iexplorer.ico
            :caption
            Pixelsuft IExplorer API
            :show_url_in_caption
            false
            
            Shit in this block doesn\'t work :(
            :system_close
            true
            :system_minimize
            true
            :system_maximize
            
            true
            :on_top
            false
            :border_style
            sizeable
            :chroma_key
            false
            :chroma_key_color
            clLime
            :redirect_to_file
            iexplorer_api_default.html
            :caption_on
            iexplorer_api_default.html
            Hello, world!
            :redirect_to_file_on
            error404
            iexplorer_api_default.html
            :can_close
            true
            :endconfig
        '''[1:].replace('   ','')
        
        def run():
            if use_7_theme==True:
                env['__COMPAT_LAYER']='WinXPSp3'
            temp_file=open("iexplorer_config.txt","w")
            temp_file.write(config.replace('   ',''))
            temp_file.close()
            run_prog(exe_name)
        
        def reload_config():
            temp_file=open("iexplorer_config.txt","w")
            temp_file.write(config.replace('   ',''))
            temp_file.close()
            temp_file_new=open("iexplorer_config_reloaded.txt","w")         
            temp_file_new.write("config reloaded!")
            temp_file_new.close()
            while True:
                if file_exists("iexplorer_config_reload_ok.txt",file_exists_params)==True:
                    del_file("iexplorer_config_reload_ok.txt")
                    del_file("iexplorer_config_reloaded.txt")
                    del_file("iexplorer_config.txt")
                    break
        
        def terminate():
            temp_file_new=open("iexplorer_terminate.txt","w")         
            temp_file_new.write("You must terminate!")
            temp_file_new.close()
            while True:
                if file_exists("iexplorer_terminated.txt",file_exists_params)==True:
                    del_file("iexplorer_terminate.txt")
                    del_file("iexplorer_terminated.txt")
                    del_file("iexplorer_config.txt")
                    if file_exists("iexplorer_url.txt",file_exists_params)==True:
                        del_file("iexplorer_url.txt")
                    break
        
        def get_url():
            if file_exists("iexplorer_url.txt",file_exists_params)==True:
                temp_file=open("iexplorer_url.txt","r")
                url=str(temp_file.read().slpit('\n')[0])
                temp_file.close()
                return str(url)
            else:
                return None
        
        def is_running(check_interval=1.5):
            temp_file_new=open("iexplorer_is_running.txt","w")         
            temp_file_new.write("You are running?!")
            temp_file_new.close()
            time_sleep(int(check_interval))
            if file_exists("iexplorer_i_am_running.txt",file_exists_params)==True:
                del_file("iexplorer_is_running.txt")
                del_file("iexplorer_i_am_running.txt")
                return True
            else:
                del_file("iexplorer_is_running.txt")
                return False
        
        def task_kill():
            cmd_run('taskkill /f /im '+exe_name)
            if file_exists("iexplorer_config.txt",file_exists_params)==True:
                del_file("iexplorer_config.txt")
                if file_exists("iexplorer_url.txt",file_exists_params)==True:
                    del_file("iexplorer_url.txt")