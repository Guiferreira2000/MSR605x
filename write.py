from msr605x import MSR605X

def is_valid_track1(data):
    """ Validate Track 1: Can be alphanumeric """
    return all(c.isalnum() or c in ' .,^%$#@!*()-+=[]{};:<>/\\|~?_' for c in data)

def is_valid_track2(data):
    """ Validate Track 2: Must be numeric """
    return data.isdigit()

def is_valid_track3(data):
    """ Validate Track 3: Must be numeric """
    return data.isdigit()

def write_tracks(msr, track1, track2, track3):
    """ Write data to each track with validation """
    # if not is_valid_track1(track1):
    #     raise ValueError("Invalid data for Track 1. Must be alphanumeric.")
    # if not is_valid_track2(track2):
    #     raise ValueError("Invalid data for Track 2. Must be numeric only.")
    # if not is_valid_track3(track3):
    #     raise ValueError("Invalid data for Track 3. Must be numeric only.")

    msr.write_track(1, track1.encode('utf-8'))
    msr.write_track(2, track2.encode('utf-8'))
    msr.write_track(3, track3.encode('utf-8'))

def main():
    msr = MSR605X()
    try:
        msr.connect()
        print("Connected to MSR605X. Ready to write data.")

        while True:
            # Input data for each track
            track1_data = "%TESTE02?"
            track2_data = "12347"
            track3_data = ";1234?"

            # Validate and write data to card
            try:
                print("Please swipe the card now...")
                write_tracks(msr, track1_data, track2_data, track3_data)
                print("Data successfully written to the card. Please swipe another card or Ctrl+C to exit.")
            except ValueError as ve:
                print(ve)

            input("Press Enter after you swipe the card...")

    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
