# devcontainer

### 概要

開発環境(コンテナ)を用意してvscode上で弄れる。
環境は一度設定ファイルを用意すればあとはvscodeを開くだけで構築が完了する。

### 必要なもの

- Dockerfile
- devcontainer.json
  - Dockerfileの情報、コンテナにインストールする拡張機能、VSCodeの設定等を定義

### 環境構築(sample)

- ディレクトリ構成

```
.
└── DEVCONTAINER_SAMPLE
    ├── .devcontainer
    │   ├── Dockerfile
    │   └── devcontainer.json
```

- 起動手順

1. vscode画面左下をクリック
2. メニューより「Remote-Containers: Open Folder in Container...」をクリック

# UnitTest

### UnitTestとは

- クラスやメソッドの単位を対象として行うテスト。
- テストが自動化されている
- 開発者自身が行う

### UnitTestの目的や考え方

[ユニットテストにまつわる10の勘違い](https://dev.classmethod.jp/articles/10_errors_about_unit_testing/)

### PythonにおけるUnitTest

主に使われているフレームワークが以下２つ。

- UnitTests
pythonの標準ライブラリ

- pytest
pipでインストール可能
