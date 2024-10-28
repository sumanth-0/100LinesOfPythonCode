import time
import threading

class PostScheduler:
    def __init__(self):
        self.posts = []

    def schedule_post(self, content, post_time):
        """Schedule a post to be posted at a specific time."""
        self.posts.append((content, post_time))

    def start_scheduling(self):
        """Start the scheduling process for all posts."""
        while self.posts:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            for post in self.posts[:]:  # Iterate over a copy of the list
                content, post_time = post
                if current_time >= post_time:
                    print(f"Posting: {content} at {current_time}")
                    self.posts.remove(post)

def main():
    scheduler = PostScheduler()
    
    while True:
        content = input("Enter the post content: ")
        post_time = input("Enter the post time (YYYY-MM-DD HH:MM:SS): ")
        scheduler.schedule_post(content, post_time)
        print(f"Post scheduled: {content} at {post_time}")
        
        if input("Do you want to schedule another post? (yes/no): ").lower() != 'yes':
            break

    threading.Thread(target=scheduler.start_scheduling, daemon=True).start()
    while scheduler.posts:
        time.sleep(1)  # Keep the main thread alive while posts are scheduled

if __name__ == "__main__":
    main()
