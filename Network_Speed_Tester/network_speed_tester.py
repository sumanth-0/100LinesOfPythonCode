import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()

    try:
        print("Finding best server...")
        st.get_best_server()

        print("Testing download speed...")
        download_speed = st.download()
        print("Testing upload speed...")
        upload_speed = st.upload()

        # Convert speeds to Mbps
        download_speed_mbps = download_speed / 1_000_000
        upload_speed_mbps = upload_speed / 1_000_000

        print(f"Download Speed: {download_speed_mbps:.2f} Mbps")
        print(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")

    except speedtest.SpeedtestBestServerFailure as e:
        print(f"Error finding best server: {e}")
    except speedtest.SpeedtestException as e:
        print(f"Error performing speed test: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_internet_speed()
