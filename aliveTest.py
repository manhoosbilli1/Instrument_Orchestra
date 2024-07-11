import serial
import time

# Function to initialize serial connection
def init_serial(port, baudrate=9600, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        if ser.is_open:
            print(f"Connected to {ser.name}")
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

# Function to send a command and read the response
def send_command(ser, command):
    try:
        ser.write((command + '\n').encode())
        time.sleep(0.1)  # Give the device some time to respond
        response = ser.readline().decode().strip()
        return response
    except Exception as e:
        print(f"Error communicating with device: {e}")
        return None

# Function to close serial connection
def close_serial(ser):
    try:
        ser.close()
        if not ser.is_open:
            print("Serial connection closed")
    except Exception as e:
        print(f"Error closing serial port: {e}")

# Main function to demonstrate usage
def main():
    port = 'COM3'  # Replace with your port
    baudrate = 9600
    timeout = 1

    ser = init_serial(port, baudrate, timeout)
    if ser:
        # Send command to identify the device
        response = send_command(ser, '*IDN?')
        if response:
            print(f"Device Identification: {response}")

        # Example command to set voltage on channel 1 to 5V
        command = 'VOLT 5, (@1)'
        response = send_command(ser, command)
        if response:
            print(f"Response to VOLT command: {response}")

        # Example command to read voltage on channel 1
        command = 'MEAS:VOLT? (@1)'
        response = send_command(ser, command)
        if response:
            print(f"Measured Voltage on Channel 1: {response}")

        close_serial(ser)

if __name__ == '__main__':
    main()
