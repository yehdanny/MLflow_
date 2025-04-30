import os
import tempfile

import mlflow
import yaml
remote_server_uri = "http://127.0.0.1:8080"  #mlflow server --host 127.0.0.1 --port 8080

def simple_tracking(x=1, y=2):
    with mlflow.start_run():
        mlflow.log_param("x_inital", x)
        mlflow.log_param("y", y)

        progress = {}
        for i in range(100):
            progress[f"step_{i:05d}"] = f"{x} + {y}"
            x += y
            mlflow.log_metric("x", x)

        with tempfile.TemporaryDirectory() as t_path:
            with open(os.path.join(t_path, "progress.yaml"), "w") as y_file:
                yaml.dump(progress, y_file)
            mlflow.log_artifact(os.path.join(t_path, "progress.yaml"))


if __name__ == "__main__":
    simple_tracking(1, 2)
    simple_tracking(3, 4)