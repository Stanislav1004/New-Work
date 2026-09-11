raw_port = "invalid_port"
try:
    port = int(raw_port)

except ValueError:
    print("ERROR: Invalid port number. Please provide a valid integer.")