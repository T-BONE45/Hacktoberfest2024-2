import brahe

# Define the satellite's initial conditions
satellite = brahe.Satellite(
    name="My Satellite",
    mass=100,  # kg
    position=[-7100, -5100, 2000],  # km
    velocity=[-3.5, 2.5, 0.5],  # km/s
)

# Define the simulation time span
start_time = brahe.Time("2024-10-09 00:00:00")
end_time = brahe.Time("2024-10-10 00:00:00")

# Run the simulation
satellite.propagate(start_time, end_time)

# Print the satellite's position and velocity at each time step
for time, state in satellite.history.items():
    print(f"Time: {time}, Position: {state.position}, Velocity: {state.velocity}")
