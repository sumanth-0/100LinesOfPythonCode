from colorama import Fore, Style, init
from database import Database
from datetime import datetime, timedelta
import os

init(autoreset=True)

class TodoApp:
    def __init__(self):
        self.db = Database()
        self.priority_names = {1: "Low", 2: "Medium", 3: "High"}

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self):
        print(Fore.CYAN + "=" * 60)
        print(Fore.CYAN + "              ADVANCED TODO APPLICATION")
        print(Fore.CYAN + "=" * 60)

    def display_task(self, task):
        task_id, title, description, priority, category, due_date, completed, created_at = task
        
        status = Fore.GREEN + "✓ Completed" if completed else Fore.YELLOW + "○ Pending"
        priority_color = Fore.RED if priority == 3 else Fore.YELLOW if priority == 2 else Fore.GREEN
        priority_text = f"{priority_color}{self.priority_names[priority]}"
        
        print(f"\n{Fore.WHITE}[{task_id}] {Fore.BLUE}{title}")
        print(f"   {Fore.WHITE}Description: {description}")
        print(f"   {Fore.WHITE}Category: {Fore.MAGENTA}{category}")
        print(f"   {Fore.WHITE}Priority: {priority_text}")
        print(f"   {Fore.WHITE}Due Date: {due_date if due_date else 'No due date'}")
        print(f"   {Fore.WHITE}Status: {status}{Style.RESET_ALL}")

    def add_task(self):
        print(Fore.YELLOW + "\n--- Add New Task ---")
        title = input("Title: ").strip()
        if not title:
            print(Fore.RED + "Title cannot be empty!")
            return
        
        description = input("Description: ").strip()
        
        print("\nPriority Levels:")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        try:
            priority = int(input("Select priority (1-3): "))
            if priority not in [1, 2, 3]:
                priority = 1
        except:
            priority = 1
        
        category = input("Category: ").strip() or "General"
        
        due_date = input("Due date (YYYY-MM-DD) or leave empty: ").strip()
        
        self.db.add_task(title, description, priority, category, due_date if due_date else None)
        print(Fore.GREEN + "Task added successfully!")

    def view_tasks(self, tasks=None, title="All Tasks"):
        if tasks is None:
            tasks = self.db.get_all_tasks()
        
        self.clear_screen()
        self.display_header()
        print(Fore.YELLOW + f"\n--- {title} ---")
        
        if not tasks:
            print(Fore.RED + "No tasks found!")
            return
        
        for task in tasks:
            self.display_task(task)

    def view_pending_tasks(self):
        tasks = self.db.get_pending_tasks()
        self.view_tasks(tasks, "Pending Tasks")

    def view_completed_tasks(self):
        tasks = self.db.get_completed_tasks()
        self.view_tasks(tasks, "Completed Tasks")

    def view_tasks_by_category(self):
        categories = self.db.get_categories()
        if not categories:
            print(Fore.RED + "No categories found!")
            return
        
        print(Fore.YELLOW + "\nAvailable Categories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        try:
            choice = int(input("\nSelect category: "))
            if 1 <= choice <= len(categories):
                tasks = self.db.get_tasks_by_category(categories[choice-1])
                self.view_tasks(tasks, f"Tasks in {categories[choice-1]}")
            else:
                print(Fore.RED + "Invalid selection!")
        except:
            print(Fore.RED + "Invalid input!")

    def view_today_tasks(self):
        tasks = self.db.get_today_tasks()
        self.view_tasks(tasks, "Today's Tasks")

    def mark_task_complete(self):
        self.view_pending_tasks()
        try:
            task_id = int(input("\nEnter task ID to mark as complete: "))
            self.db.mark_completed(task_id)
            print(Fore.GREEN + "Task marked as complete!")
        except:
            print(Fore.RED + "Invalid task ID!")

    def mark_task_pending(self):
        self.view_completed_tasks()
        try:
            task_id = int(input("\nEnter task ID to mark as pending: "))
            self.db.mark_pending(task_id)
            print(Fore.GREEN + "Task marked as pending!")
        except:
            print(Fore.RED + "Invalid task ID!")

    def delete_task(self):
        self.view_tasks()
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            self.db.delete_task(task_id)
            print(Fore.GREEN + "Task deleted successfully!")
        except:
            print(Fore.RED + "Invalid task ID!")

    def search_tasks(self):
        keyword = input("Enter search keyword: ").strip()
        if not keyword:
            print(Fore.RED + "Please enter a keyword to search!")
            return
        
        tasks = self.db.search_tasks(keyword)
        self.view_tasks(tasks, f"Search Results for '{keyword}'")

    def update_task(self):
        self.view_tasks()
        try:
            task_id = int(input("\nEnter task ID to update: "))
            
            print(Fore.YELLOW + "\nLeave field empty to keep current value:")
            title = input("New title: ").strip()
            description = input("New description: ").strip()
            
            print("\nPriority Levels:")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            priority_input = input("New priority (1-3): ").strip()
            priority = int(priority_input) if priority_input else None
            
            category = input("New category: ").strip()
            due_date = input("New due date (YYYY-MM-DD): ").strip()
            
            self.db.update_task(task_id, 
                              title if title else None,
                              description if description else None,
                              priority,
                              category if category else None,
                              due_date if due_date else None)
            
            print(Fore.GREEN + "Task updated successfully!")
            
        except:
            print(Fore.RED + "Invalid input!")

    def show_statistics(self):
        all_tasks = self.db.get_all_tasks()
        pending_tasks = self.db.get_pending_tasks()
        completed_tasks = self.db.get_completed_tasks()
        categories = self.db.get_categories()
        
        self.clear_screen()
        self.display_header()
        print(Fore.YELLOW + "\n--- Statistics ---")
        print(f"{Fore.WHITE}Total Tasks: {len(all_tasks)}")
        print(f"{Fore.YELLOW}Pending Tasks: {len(pending_tasks)}")
        print(f"{Fore.GREEN}Completed Tasks: {len(completed_tasks)}")
        print(f"{Fore.MAGENTA}Categories: {len(categories)}")
        
        if all_tasks:
            completion_rate = (len(completed_tasks) / len(all_tasks)) * 100
            print(f"{Fore.CYAN}Completion Rate: {completion_rate:.1f}%")

    def main_menu(self):
        while True:
            self.clear_screen()
            self.display_header()
            
            print(Fore.GREEN + "\nMain Menu:")
            print("1.  View All Tasks")
            print("2.  View Pending Tasks")
            print("3.  View Completed Tasks")
            print("4.  View Today's Tasks")
            print("5.  View Tasks by Category")
            print("6.  Add New Task")
            print("7.  Update Task")
            print("8.  Mark Task as Complete")
            print("9.  Mark Task as Pending")
            print("10. Delete Task")
            print("11. Search Tasks")
            print("12. Show Statistics")
            print("13. Exit")
            
            try:
                choice = int(input(Fore.YELLOW + "\nEnter your choice (1-13): "))
                
                if choice == 1:
                    self.view_tasks()
                elif choice == 2:
                    self.view_pending_tasks()
                elif choice == 3:
                    self.view_completed_tasks()
                elif choice == 4:
                    self.view_today_tasks()
                elif choice == 5:
                    self.view_tasks_by_category()
                elif choice == 6:
                    self.add_task()
                elif choice == 7:
                    self.update_task()
                elif choice == 8:
                    self.mark_task_complete()
                elif choice == 9:
                    self.mark_task_pending()
                elif choice == 10:
                    self.delete_task()
                elif choice == 11:
                    self.search_tasks()
                elif choice == 12:
                    self.show_statistics()
                elif choice == 13:
                    print(Fore.GREEN + "Goodbye!")
                    break
                else:
                    print(Fore.RED + "Invalid choice! Please try again.")
                
                input(Fore.YELLOW + "\nPress Enter to continue...")
                
            except ValueError:
                print(Fore.RED + "Please enter a valid number!")
                input(Fore.YELLOW + "\nPress Enter to continue...")

if __name__ == "__main__":
    app = TodoApp()
    try:
        app.main_menu()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nApplication interrupted!")
    finally:
        app.db.close()