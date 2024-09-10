import oci
from oci.core import ComputeClient

# OCIのConfigを読み込む (デフォルトでは ~/.oci/config)
config = oci.config.from_file()

# ComputeClientの初期化
compute_client = ComputeClient(config)

# インスタンスIDを指定
instance_id = "ocid1.instance.oc1.ap-tokyo-1.anxhiljrssl65iqcy5ej7e5m5x5ixoani3eqlww7ufme3p6ss4r3yiikyjva"  # ここに対象インスタンスのOCIDを入力

# インスタンスを起動する関数
def start_instance(instance_id):
    print(f"Starting instance {instance_id}...")
    compute_client.instance_action(instance_id, "START")
    print(f"Instance {instance_id} started.")

# インスタンスを停止する関数
def stop_instance(instance_id):
    print(f"Stopping instance {instance_id}...")
    compute_client.instance_action(instance_id, "SOFTSTOP")
    print(f"Instance {instance_id} stopped.")

if __name__ == "__main__":
    # 起動・停止のどちらかを実行する (例: 起動)
    action = input("Enter 'start' to start the instance or 'stop' to stop the instance: ").strip().lower()
    
    if action == 'start':
        start_instance(instance_id)
    elif action == 'stop':
        stop_instance(instance_id)
    else:
        print("Invalid action. Please enter 'start' or 'stop'.")
