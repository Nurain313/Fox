import multiprocessing
import subprocess
import time
import os 


parent_dir = os.path.dirname(os.getcwd())


# Define the functions to run each script
def run_tv_show():
    fox_dir = os.path.join(parent_dir, 'fox')
    tv_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
    tv_show_file = os.path.join(tv_file_dir, 'tv_show_file')
    py_file = os.path.join(tv_show_file, 'tv_show.py')
    subprocess.run(["python", py_file])
  
  
def run_movie():
  #  time.sleep(5) # Wait for 5 seconds 
    fox_dir = os.path.join(parent_dir, 'fox')
    tv_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
    tv_show_file = os.path.join(tv_file_dir, 'movie_file')
    py_file = os.path.join(tv_show_file, 'movie.py')
    subprocess.run(["python", py_file])

def run_sms():
   # time.sleep(10)  # Wait for 10 seconds
    fox_dir = os.path.join(parent_dir, 'fox')
    tv_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
    tv_show_file = os.path.join(tv_file_dir, 'sms_file')
    py_file = os.path.join(tv_show_file, 'sms.py')
    subprocess.run(["python", py_file])
    
def run_fb():
   # time.sleep(15) # wait for 15 seconds
    fox_dir = os.path.join(parent_dir, 'fox')
    tv_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
    tv_show_file = os.path.join(tv_file_dir, 'fb_file')
    py_file = os.path.join(tv_show_file, 'fb.py')
    subprocess.run(["python", py_file])


def run_ig():
    fox_dir = os.path.join(parent_dir, 'fox')
    tv_file_dir = os.path.join(fox_dir, 'upcoming_movies_and_TV_show')
    tv_show_file = os.path.join(tv_file_dir, 'ig_file')
    py_file = os.path.join(tv_show_file, 'ig.py')
    subprocess.run(["python", py_file])


    

# Start the processes
if __name__ == '__main__':
    tv_show_process = multiprocessing.Process(target=run_tv_show)
    movie_process = multiprocessing.Process(target=run_movie)
    sms_process = multiprocessing.Process(target=run_sms)
    fb_process = multiprocessing.Process(target=run_fb)
    ig_process = multiprocessing.Process(target=run_ig)

    tv_show_process.start()
    movie_process.start()
    sms_process.start()
    fb_process.start()
    ig_process.start()

    # Wait for all processes to finish
    tv_show_process.join()
    movie_process.join()
    sms_process.join()
    fb_process.join()
    ig_process.join()

print ("All processes complete")