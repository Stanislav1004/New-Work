def make_alert(server_name, status_code):
    if status_code == 200:
        return f"Server {server_name} is up and running."
    else:
        return f"Server {server_name} is down. Status code: {status_code}"

msg1 = make_alert("web_server", 200)
msg2 = make_alert("db-server", 500)

try:
    print(msg1, msg2)

except Exception as e:
    print(f"An error occurred: {e}")

print(msg1, msg2)