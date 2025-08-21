import tkinter as tk

class ParticleSettingsWindow:
      def __init__(self, master, current_velocity, current_acceleration, particle_list):
            self.master = master
            
            self.particle_list = particle_list

            self.vel_x = current_velocity[0]
            self.vel_y = current_velocity[1]
            self.acc_x = current_acceleration[0]
            self.acc_y = current_acceleration[1]
            self.mass = 1
            self.radius = 1

            self.vel_x_var = tk.IntVar(value=self.vel_x)
            self.vel_y_var = tk.IntVar(value=self.vel_y)
            self.acc_x_var = tk.IntVar(value=self.acc_x)
            self.acc_y_var = tk.IntVar(value=self.acc_y)
            self.mass_var = tk.IntVar(value=self.mass)
            self.radius_var = tk.IntVar(value=self.radius)

            master.title("Particle Settings")

            # Horizontal velocity slider
            self.x_vel_label = tk.Label(master, text="Horizontal Velocity:")
            self.x_vel_scale = tk.Scale(master, variable=self.vel_x_var, from_= -20, to= 20, orient= tk.HORIZONTAL, command=self.update_x_vel)

            # Vertical velocity slider
            self.y_vel_label = tk.Label(master, text="Vertical Velocity:") 
            self.y_vel_scale = tk.Scale(master, variable=self.vel_y_var, from_= -20, to= 20, orient= tk.HORIZONTAL, command=self.update_y_vel)

            # Horizontal acceleration slider
            self.x_acc_label = tk.Label(master, text="Horizontal Acceleration:")
            self.x_acc_scale = tk.Scale(master, variable=self.acc_x_var, from_= -20, to= 20, orient= tk.HORIZONTAL, command=self.update_x_acc)

            # Vertical acceleration slider
            self.y_acc_label = tk.Label(master, text="Vertical Acceleration:")
            self.y_acc_scale = tk.Scale(master, variable=self.acc_y_var, from_= -20, to= 20, orient= tk.HORIZONTAL, command=self.update_y_acc)

            # Mass slider
            self.mass_label = tk.Label(master, text="Mass:")
            self.mass_scale = tk.Scale(master, variable=self.mass_var, from_= 1, to= 20, orient= tk.HORIZONTAL, command=self.update_mass)

            # Radius slider
            self.radius_label = tk.Label(master, text="Radius")
            self.radius_scale = tk.Scale(master, variable=self.radius_var, from_= 1, to=50, orient=tk.HORIZONTAL, command=self.update_radius)

            # Clear Button
            self.clear_button = tk.Button(master, text="Clear", command=self.clear_board)

            # Add all things to window
            self.x_vel_label.pack(anchor=tk.CENTER)
            self.x_vel_scale.pack(anchor=tk.CENTER)
            self.y_vel_label.pack(anchor=tk.CENTER)
            self.y_vel_scale.pack(anchor=tk.CENTER)
            self.x_acc_label.pack(anchor=tk.CENTER)
            self.x_acc_scale.pack(anchor=tk.CENTER)
            self.y_acc_label.pack(anchor=tk.CENTER)
            self.y_acc_scale.pack(anchor=tk.CENTER)
            self.mass_label.pack(anchor=tk.CENTER)
            self.mass_scale.pack(anchor=tk.CENTER)
            self.radius_label.pack(anchor=tk.CENTER)
            self.radius_scale.pack(anchor=tk.CENTER)  
            self.clear_button.pack(anchor=tk.CENTER)     

      def update_x_vel(self, val):
            self.vel_x = self.vel_x_var.get()

      def update_y_vel(self, val):
            self.vel_y = self.vel_y_var.get()

      def update_x_acc(self, val):
          self.acc_x = self.acc_x_var.get()

      def update_y_acc(self, val):
          self.acc_y = self.acc_y_var.get()

      def update_mass(self, val):
          self.mass = self.mass_var.get()
      
      def update_radius(self, val):
           self.radius = self.radius_var.get()

      def clear_board(self):
            self.particle_list.clear()


class GlobalSettingsWindow():
      def __init__(self, master):
            self.master = master

            self.gravity = 0
            
            self.gravity_var = tk.IntVar(self.gravity)

            # Gravity slider
            self.gravity_label = tk.Label(master, text="Gravity: (Not functioning currently)")
            self.gravity_scale = tk.Scale(master, variable=self.gravity_var, from_= -20, to= 20, orient= tk.HORIZONTAL, command=self.update_gravity)

            # Add Everything
            self.gravity_label.pack(anchor=tk.CENTER)
            self.gravity_scale.pack(anchor=tk.CENTER)
      
      def update_gravity(self):
           self.gravity = self.gravity_var.get()