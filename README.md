# FastAPI Inventory Project

FastAPI と PostgreSQL を使用して開発した在庫管理 REST API サーバープロジェクトです。

## Overview

本プロジェクトは、FastAPI と PostgreSQL を利用して開発した在庫管理用 REST API サーバーです。

商品の登録・一覧取得・更新・削除などの CRUD 機能を実装し、バックエンド開発に必要な API 設計、データベース連携、Docker を利用した開発環境構築について学習することを目的として作成しました。

また、Swagger UI を利用して API の動作確認ができるように構成しています。

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- Git / GitHub

---

## Features

- 商品登録(Create)
- 商品一覧取得(Read)
- 商品情報更新(Update)
- 商品削除(Delete)
- REST API 実装
- PostgreSQL データベース連携
- Docker ベースの開発環境構築
- Swagger UI による API 確認

---

## API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Run Project

### Docker 起動

```bash
docker compose up --build
```

---

## Example Request

### Create Item

POST `/items/`

```json
{
  "name": "apple",
  "quantity": 10
}
```

### Response

```json
{
  "id": 1,
  "name": "apple",
  "quantity": 10
}
```

---

## Project Structure

```text
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
└── routers/
```

---

## Points

- FastAPI のルーティング機能を利用し、機能ごとにコードを分割しました。
- SQLAlchemy を利用して PostgreSQL と連携しました。
- Docker Compose を使用し、バックエンドとデータベースを同時に起動できるように構築しました。
- Swagger UI を利用して API の動作確認を行えるようにしました。
- CRUD 処理を通して REST API の基本構成を学習しました。

---

## Future Improvements

- JWT 認証機能実装
- ユーザー管理機能追加
- テストコード追加
- Render / AWS デプロイ
- CI/CD パイプライン構築

---

## Author

GitHub: [Tatsumakiri](https://github.com/Tatsumakiri)
