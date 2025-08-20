import tkinter as tk

class SettingsWindow:
    def __init__(self, master, current_velocity, current_acceleration):
        self.master = master
        
        self.vel_x = current_velocity[0]
        self.vel_y = current_velocity[1]
        self.acc_x = current_acceleration[0]
        self.acc_y = current_acceleration[1]
        self.gravity = 0

        self.vel_x_var = tk.IntVar(value=self.vel_x)
        self.vel_y_var = tk.IntVar(value=self.vel_y)
        self.acc_x_var = tk.IntVar(value=self.acc_x)
        self.acc_y_var = tk.IntVar(value=self.acc_y)
        self.gravity_var = tk.IntVar(value=self.gravity)

        master.title("Settings")

        # Horizontal velocity slider
        self.x_vel_label = tk.Label(master, text="Horizontal Velocity:")
        self.x_vel_scale = tk.Scale(master, variable=self.vel_x_var, from_= 0, to= 20, orient= tk.HORIZONTAL, command=self.update_x_vel)

        # Vertical velocity slider
        self.y_vel_label = tk.Label(master, text="Vertical Velocity:") 
        self.y_vel_scale = tk.Scale(master, variable=self.vel_y_var, from_= 0, to= 20, orient= tk.HORIZONTAL, command=self.update_y_vel)

        # Horizontal acceleration slider
        self.x_acc_label = tk.Label(master, text="Horizontal Acceleration:")
        self.x_acc_scale = tk.Scale(master, variable=self.acc_x_var, from_= 0, to= 20, orient= tk.HORIZONTAL, command=self.update_x_acc)

        # Vertical acceleration slider
        self.y_acc_label = tk.Label(master, text="Vertical Acceleration:")
        self.y_acc_scale = tk.Scale(master, variable=self.acc_y_var, from_= 0, to= 20, orient= tk.HORIZONTAL, command=self.update_y_acc)

        # Gravity slider
        self.gravity_label = tk.Label(master, text="Gravity: (Not functioning currently)")
        self.gravity_scale = tk.Scale(master, variable=self.gravity_var, from_= 0, to= 20, orient= tk.HORIZONTAL, command=self.update_gravity)

        # Add all things to window
        self.x_vel_label.pack(anchor=tk.CENTER)
        self.x_vel_scale.pack(anchor=tk.CENTER)
        self.y_vel_label.pack(anchor=tk.CENTER)
        self.y_vel_scale.pack(anchor=tk.CENTER)
        self.x_acc_label.pack(anchor=tk.CENTER)
        self.x_acc_scale.pack(anchor=tk.CENTER)
        self.y_acc_label.pack(anchor=tk.CENTER)
        self.y_acc_scale.pack(anchor=tk.CENTER)
        self.gravity_label.pack(anchor=tk.CENTER)
        self.gravity_scale.pack(anchor=tk.CENTER)        

    def update_x_vel(self, val):
            self.vel_x = self.vel_x_var.get()

    def update_y_vel(self, val):
            self.vel_y = self.vel_y_var.get()

    def update_x_acc(self, val):
          self.acc_x = self.acc_x_var.get()

    def update_y_acc(self, val):
          self.acc_y = self.acc_y_var.get()

    def update_gravity(self, val):
          self.gravity = self.gravity_var.get()
            


