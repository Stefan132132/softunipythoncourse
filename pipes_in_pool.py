volume_pool = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours_worker_gone = float(input())

liters_full = pipe1 * hours_worker_gone + pipe2 * hours_worker_gone

procent_volume = (liters_full / volume_pool) * 100
procent_pipe1 = (pipe1 * hours_worker_gone / liters_full) * 100
procent_pipe2 = (pipe2 * hours_worker_gone / liters_full) * 100

if liters_full <= volume_pool:
    print(f"The pool is {procent_volume:.2f}% full. Pipe 1: {procent_pipe1:.2f}%. Pipe 2: {procent_pipe2:.2f}%.")
elif volume_pool < liters_full:
    overflow_liters = liters_full - volume_pool
    print(f"For {hours_worker_gone:.2f} hours the pool overflows with {overflow_liters:.2f} liters.")