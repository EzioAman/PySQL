import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def fetch_students_info(table):
    query = "SELECT * FROM Students"
    fetch_data_info(query, table)

def fetch_teachers_info(table):
    query = "SELECT * FROM Staff"
    fetch_data_info(query, table)

def fetch_salary_info(table):
    query = "SELECT * FROM Salary"
    fetch_data_info(query, table)

def fetch_custom_data(table, query_entry):
    query = query_entry.get("1.0", "end-1c")  # Get the entire text from the Text widget
    if not query.strip():  # Check if query is empty or contains only whitespace
        messagebox.showerror("Error", "Please enter a query.")
        return  # Stop further execution
    fetch_data_info(query, table)  # Call the fetch_data_info function with the custom query

def fetch_data_info(query, table):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Arkoarceus@99",
            database="aman"
        )

        # Create a cursor object to execute SQL queries
        cur = conn.cursor()

        # Execute the SQL query
        cur.execute(query)

        # Check if the query is a SELECT query
        is_select_query = query.strip().lower().startswith('select')

        if is_select_query:
            # Fetch column names from the cursor description
            columns = [column[0] for column in cur.description]

            # Fetch all rows from the result set
            rows = cur.fetchall()

            if not rows:
                messagebox.showinfo("Info", "Query executed successfully but returned no rows.")
            else:
                # Update table columns based on fetched column names
                table['columns'] = columns
                for col in columns:
                    table.heading(col, text=col)

                # Clear existing data in the table
                table.delete(*table.get_children())

                # Insert fetched rows into the table
                for row in rows:
                    table.insert('', tk.END, values=row)

                # Update the table to adjust size
                table.update_idletasks()

                # Calculate required table height based on number of rows
                row_height = 24  # Assuming each row height is 24 pixels
                table_height = min(800, len(rows) * row_height + 25)  # Add some extra space
                table_canvas.config(scrollregion=table_canvas.bbox("all"), height=table_height)

        else:
            # For non-SELECT queries (UPDATE, INSERT, DELETE), commit changes
            conn.commit()
            messagebox.showinfo("Info", "Query executed successfully and database updated.")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except mysql.connector.Error as err:
        # Handle MySQL errors
        messagebox.showerror("MySQL Error", f"Error executing query: {err}")

def update_query_entry(event=None):
    # Calculate the number of lines required for the current query text
    num_lines = query_entry.get("1.0", "end-1c").count('\n') + 1
    # Update the height of the Text widget based on the number of lines
    query_entry.config(height=num_lines)

# Create the main Tkinter window
root = tk.Tk()
root.title("Dynamic Table Display")
root.geometry("900x600")
root.maxsize(1920, 1080)  # Limit maximum window size

# Create a frame for buttons, entry, and table
frame = tk.Frame(root, bg="light grey")
frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Create buttons to fetch specific data
students_button = tk.Button(frame, text="Fetch Students", command=lambda: fetch_students_info(table), bg="sky blue", fg="white")
students_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

teachers_button = tk.Button(frame, text="Fetch staffs", command=lambda: fetch_teachers_info(table), bg="sky blue", fg="white")
teachers_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

salary_button = tk.Button(frame, text="Fetch Salary", command=lambda: fetch_salary_info(table), bg="sky blue", fg="white")
salary_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

# Create a Text widget for custom SQL query
query_entry = tk.Text(frame, height=4, width=50)
query_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")
# Bind an event handler to update the query entry height dynamically
query_entry.bind('<KeyRelease>', update_query_entry)

# Create a button to execute custom query
custom_query_button = tk.Button(frame, text="Execute Custom Query", command=lambda: fetch_custom_data(table, query_entry), bg="sky blue", fg="white")
custom_query_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

# Create a canvas to contain the treeview and scrollbar
table_canvas = tk.Canvas(frame)
table_canvas.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Create a treeview to display information in table form
table = ttk.Treeview(table_canvas)
table.grid(row=0, column=0, sticky="nsew")

# Add scrollbar
scrollbar_y = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
scrollbar_y.grid(row=3, column=3, sticky="ns")
table.configure(yscroll=scrollbar_y.set)

# Adjust scroll region to the width of the table
table_width = min(1280, sum(table.column(c)["width"] for c in table["columns"]) + 5)  # Reduce padding between columns
table_canvas.configure(scrollregion=table_canvas.bbox("all"), width=table_width)

# Set a minimum width for the first column
table.column('#0', minwidth=0, width=0)

# Configure frame to expand in both rows and columns
frame.grid_rowconfigure(3, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

# Run the Tkinter event loop
root.mainloop()
