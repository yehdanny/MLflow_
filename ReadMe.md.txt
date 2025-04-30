## 📊 MLflow 機器學習實驗管理平台

本專案採用 [MLflow](https://mlflow.org/) 作為機器學習與深度學習模型的實驗追蹤與管理工具。MLflow 是一個開源平台，支援完整的機器學習生命週期（ML lifecycle），涵蓋從實驗記錄、模型訓練、版本控管到部署的各個階段，能有效提升專案的可重現性與開發效率。

---

### 🔧 MLflow 核心組件

- **Tracking**：記錄每次實驗的參數（parameters）、評估指標（metrics）、模型產出（artifacts）與原始碼版本，便於實驗管理與結果比較。
- **Projects**：透過 `MLproject` 檔案標準化專案格式，支援使用 Conda 或 Docker 定義可重現的運行環境。
- **Models**：以統一格式（如 Python Function、ONNX、TorchScript）封裝模型，支援多種部署方式，例如本地部署、REST API 或雲端服務。
- **Model Registry**：集中管理模型的版本與階段狀態（如 Staging、Production），便於協作與與 CI/CD 整合。

---

### ☁️ 整合 Azure、LangChain 與其他 API

MLflow 支援與多種平台與工具整合，擴展其在大型應用中的靈活性與可擴充性：

- **Azure ML + MLflow**：
  - 可將本地實驗自動上傳至 Azure ML Studio 進行集中管理與部署。
  - 搭配 `azureml-mlflow` 模組，可無縫整合常用函式如 `mlflow.log_metric()`、`log_model()` 等。
  - 支援將模型部署為 Azure Web Service，便於大規模應用。

- **LangChain 整合**：
  - 在 RAG（Retrieval-Augmented Generation）與大型語言模型（LLM）應用中，可使用 MLflow 追蹤 chain 運行歷程、向量嵌入模型與查詢回傳內容。
  - 有助於開發具備監控能力與版本控制的 AI 應用，例如智能問答系統或多輪對話助手。

- **其他支援平台與工具**：
  - 自動部署至 **Docker**, **Kubernetes**, **SageMaker**, **Azure Functions**, **Google Cloud Run** 等平台。
  - 可整合 **TensorBoard**, **Optuna**, **Scikit-learn**, **PyTorch Lightning** 等框架進行超參數搜尋與訓練監控。

---

### 💡 MLflow 實際使用情境

MLflow 適用於任何需追蹤實驗與模型的工作流程，例如：

- 模型效能比較（不同架構、參數、資料前處理方式等）
- 快速記錄與視覺化訓練結果
- 模型部署版本控制與更新
- 跨平台、跨人員的協作專案管理

---

### 🚀 本專案的 MLflow 使用方式

- 所有實驗記錄將儲存在 `./mlruns/` 目錄中。
- 啟動本地 UI 可使用以下指令：
  ```bash
  mlflow ui   # 啟動 MLflow UI，預設於 http://localhost:5000
  mlflow server --host 127.0.0.1 --port 8080  # 另開服務於 http://127.0.0.1:8080

## Note : 
- [mlflow-param](./01_mlfow_基本參數/基本)

## Reference : 
- [Azure + mlflow](https://learn.microsoft.com/zh-tw/azure/machine-learning/concept-mlflow?view=azureml-api-2)
- [Langchain + mlflow](https://mlflow.org/docs/latest/llms/langchain/autologging)
- [mlflow 操作](https://medium.com/@wangpenhsuan/%E5%AF%A6%E4%BD%9C-mlflow-%E6%A8%A1%E5%9E%8B%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83-ml-%E5%AF%A6%E9%A9%97%E4%B8%8D%E5%86%8D%E9%9B%9C%E4%BA%82-4be96b777871)
