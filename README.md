# fastapi-inventory-project
# FastAPI Inventory Project

FastAPI と PostgreSQL を使用して開発した在庫管理 REST API サーバープロジェクトです。

## Overview

このプロジェクトは、商品の在庫情報を管理するためのバックエンド API サーバーです。  
CRUD(Create, Read, Update, Delete) 機能を実装し、Docker を利用して開発環境を構築しました。

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose

## Features

- 商品登録(Create)
- 商品一覧取得(Read)
- 商品情報更新(Update)
- 商品削除(Delete)
- REST API 実装
- PostgreSQL データベース連携
- Docker ベースの開発環境構築

## API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

## Run Project

### Docker 起動

```bash
docker compose up --build
```

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

## Future Improvements

- JWT 認証実装
- ユーザー管理機能
- テストコード追加
- Render/AWS デプロイ
- CI/CD パイプライン構築

## Author

GitHub:
https://github.com/Tatsumakiri# fastapi-inventory-project
