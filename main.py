import tkinter as tk
from tkinter import ttk, filedialog

class CkptSampler:
    def __init__(self, master):
        self.master = master
        self.master.title("Checkpoint Sampler")

        # Initialize variables
        self.ckpt_var = tk.StringVar(value="model 1.3.ckpt")
        self.prompt_var = tk.StringVar(value="a painting of a virus monster playing guitar")
        self.outdir_var = tk.StringVar()
        self.ddim_steps_var = tk.IntVar(value=50)
        self.fixed_code_var = tk.BooleanVar()
        self.ddim_eta_var = tk.DoubleVar(value=0.0)
        self.n_iter_var = tk.IntVar(value=1)
        self.H_var = tk.IntVar(value=512)
        self.W_var = tk.IntVar(value=512)
        self.C_var = tk.IntVar(value=4)
        self.f_var = tk.IntVar(value=8)
        self.n_samples_var = tk.IntVar(value=5)
        self.n_rows_var = tk.IntVar(value=0)
        self.scale_var = tk.DoubleVar(value=7.5)
        self.from_file_var = tk.StringVar()
        self.seed_var = tk.IntVar(value=42)
        self.small_batch_var = tk.BooleanVar()
        self.precision_var = tk.StringVar(value="autocast")

        # Create widgets
        ttk.Label(self.master, text="Ckpt File:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        ttk.Entry(self.master, textvariable=self.ckpt_var, width=40).grid(row=0, column=1, columnspan=2, pady=5, sticky=tk.W)

        ttk.Label(self.master, text="Prompt:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        ttk.Entry(self.master, textvariable=self.prompt_var, width=40).grid(row=1, column=1, columnspan=2, pady=5, sticky=tk.W)

        ttk.Label(self.master, text="Output Directory:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        ttk.Entry(self.master, textvariable=self.outdir_var, width=30).grid(row=2, column=1, pady=5, sticky=tk.W)
        ttk.Button(self.master, text="Browse", command=self.browse_outdir).grid(row=2, column=2, pady=5, sticky=tk.W)

        ttk.Label(self.master, text="DDIM Steps:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        ttk.Entry(self.master, textvariable=self.ddim_steps_var, width=10).grid(row=3, column=1, columnspan=2, pady=5, sticky=tk.W)

        ttk.Checkbutton(self.master, text="Fixed Code", variable=self.fixed_code_var).grid(row=4, column=1, columnspan=2, pady=5, sticky=tk.W)

        ttk.Label(self.master, text="DDIM Eta:").grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
        ttk.Entry(self.master, textvariable=self.ddim_eta_var, width=10).grid(row=5, column=1, columnspan=2, pady=5, sticky=tk.W)

        ttk.Label(self.master, text="Number of Iterations:").grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)
        ttk.Entry(self.master, textvariable=self.n_iter_var, width=10).grid(row=6, column=1, columnspan=2, pady=5, sticky=tk.W)

        # Add more widgets for the remaining parameters...

        ttk.Button(self.master, text="Start Processing", command=self.start_processing).grid(row=20, column=0, columnspan=3, pady=20)

    def browse_outdir(self):
        directory = filedialog.askdirectory()
        self.outdir_var.set(directory)

    def start_processing(self):
        # Retrieve values for the parameters
        ckpt = self.ckpt_var.get()
        prompt = self.prompt_var.get()
        outdir = self.outdir_var.get()
        ddim_steps = self.ddim_steps_var.get()
        fixed_code = self.fixed_code_var.get()
        ddim_eta = self.ddim_eta_var.get()
        n_iter = self.n_iter_var.get()

        # Retrieve values for the remaining parameters...

        # Print or use the values as needed
        print("Ckpt:", ckpt)
        print("Prompt:", prompt)
        print("Output Directory:", outdir)
        print("DDIM Steps:", ddim_steps)
        print("Fixed Code:", fixed_code)
        print("DDIM Eta:", ddim_eta)
        print("Number of Iterations:", n_iter)

        # Perform further actions based on the parameter values


if __name__ == "__main__":
    root = tk.Tk()
    app = CkptSampler(root)
    root.mainloop()
