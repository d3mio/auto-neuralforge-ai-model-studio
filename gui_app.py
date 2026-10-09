import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NeuralForgeAIStudio:
    def __init__(self, root):
        self.root = root
        self.root.title('NeuralForge AI Studio')
        self.root.geometry('1200x800')
        self.root.configure(bg='#2E3440')

        # Sidebar
        self.sidebar = tk.Frame(root, bg='#3B4252', width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Model Architecture
        self.model_arch_label = tk.Label(self.sidebar, text='Model Architecture', fg='#ECEFF4', bg='#3B4252')
        self.model_arch_label.pack(pady=10)
        self.model_arch_button = tk.Button(self.sidebar, text='Design Model', fg='#ECEFF4', bg='#4C566A', command=self.design_model)
        self.model_arch_button.pack(pady=5)

        # Performance Profiling
        self.profiling_label = tk.Label(self.sidebar, text='Performance Profiling', fg='#ECEFF4', bg='#3B4252')
        self.profiling_label.pack(pady=10)
        self.profiling_button = tk.Button(self.sidebar, text='Start Profiling', fg='#ECEFF4', bg='#4C566A', command=self.start_profiling)
        self.profiling_button.pack(pady=5)

        # Main Content
        self.main_content = tk.Frame(root, bg='#2E3440')
        self.main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Model Diagram
        self.model_diagram_frame = tk.Frame(self.main_content, bg='#2E3440')
        self.model_diagram_frame.pack(fill=tk.BOTH, expand=True)
        self.fig, self.ax = plt.subplots(figsize=(10, 6), facecolor='#2E3440')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.model_diagram_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def design_model(self):
        self.ax.clear()
        self.ax.set_title('Model Architecture Diagram', color='#ECEFF4')
        self.ax.plot([0, 1, 2], [0, 1, 0], color='#88C0D0', label='Layer 1')
        self.ax.plot([1, 2, 3], [0, 1, 0], color='#81A1C1', label='Layer 2')
        self.ax.legend()
        self.canvas.draw()

    def start_profiling(self):
        self.ax.clear()
        self.ax.set_title('Performance Profiling', color='#ECEFF4')
        self.ax.plot([0, 1, 2, 3], [0, 1, 0.5, 0.8], color='#8FBCBB', label='Performance')
        self.ax.legend()
        self.canvas.draw()

if __name__ == '__main__':
    root = tk.Tk()
    app = NeuralForgeAIStudio(root)
    root.mainloop()