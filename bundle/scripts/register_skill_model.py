"""Log a skill as a pyfunc model version into a UC registered model.

Realizes the "skill as a Unity Catalog securable" thesis concretely: the skill's
behavior (here the trivial `behavior_echo` = uppercase) is wrapped as an MLflow
pyfunc model and registered to Unity Catalog, where it becomes a governable,
versioned securable (GRANT-able, lineage-tracked).

Run via the DAB: `databricks bundle run forge_register -t fevm -p fevm`.
"""
import argparse
import mlflow
import mlflow.pyfunc
import pandas as pd
from mlflow.models import infer_signature


class SkillModel(mlflow.pyfunc.PythonModel):
    """A skill behavior wrapped as a model. Stand-in for a real governed skill."""

    def predict(self, context, model_input):
        if hasattr(model_input, "iloc"):
            col = model_input.iloc[:, 0]
            return [str(x).upper() for x in col]
        return [str(x).upper() for x in model_input]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="Full UC name catalog.schema.model")
    ap.add_argument("--experiment", required=True, help="MLflow experiment path")
    args = ap.parse_args()

    mlflow.set_registry_uri("databricks-uc")
    mlflow.set_experiment(args.experiment)

    example = pd.DataFrame({"text": ["governed skills"]})
    signature = infer_signature(example, ["GOVERNED SKILLS"])

    with mlflow.start_run() as run:
        info = mlflow.pyfunc.log_model(
            artifact_path="model",
            python_model=SkillModel(),
            signature=signature,
            input_example=example,
            registered_model_name=args.model,
        )
        print(f"RESULT: registered {args.model} | run={run.info.run_id} | uri={info.model_uri}")


if __name__ == "__main__":
    main()
