import subprocess
import time
import os 


parent_dir = os.path.dirname(os.getcwd())
fox_dir = os.path.join(parent_dir, 'fox')


tv_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
tv_show_file = os.path.join(tv_file_dir, 'tv_show_file')


movie_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
movie_file = os.path.join(movie_file_dir, 'movie_file')


sms_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
sms_file = os.path.join(sms_file_dir, 'sms_file')


fb_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
fb_file = os.path.join(fb_file_dir, 'fb_file')


ig_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
ig_file = os.path.join(ig_file_dir, 'ig_file')

    

# list of file paths to run
file_paths = [os.path.join(tv_show_file, 'tv_show.py'), os.path.join(movie_file, 'movie.py'), os.path.join(sms_file, 'sms.py'), os.path.join(fb_file, 'fb.py'), os.path.join(ig_file, 'ig.py')]

# create a list of subprocesses
procs = []
for file_path in file_paths:
    # get the directory of the file
    file_dir = os.path.dirname(file_path)
    # create the subprocess
    proc = subprocess.Popen(['python', file_path], cwd=file_dir)
    procs.append(proc)
    # wait for 50 seconds before running the next file
    time.sleep(50)

# wait for all subprocesses to complete
for proc in procs:
    proc.wait()
    time.sleep(5)

print ("updates will run again in 24 hours time")
time.sleep(24*60*60)
