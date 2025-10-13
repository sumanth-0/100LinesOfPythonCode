from ascii_clock import ASCIIClock

def test_ascii_clock():
    """Test the ASCII clock functionality"""
    clock = ASCIIClock()

    print("Testing ASCII Clock...")
    print("=" * 50)

    # Test with current time
    current_time = clock.get_current_time()
    print(f"Current time: {current_time}")

    # Display the ASCII representation
    clock.display_bordered_clock()

    print("=" * 50)
    print("ASCII Clock test completed successfully!")
    print("Run 'python ascii_clock.py' to start the live clock.")


if __name__ == "__main__":
    test_ascii_clock()
