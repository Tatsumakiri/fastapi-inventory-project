# FastAPI在庫管理API

## 概要
本プロジェクトは、PythonのFastAPIを使用して作成した在庫管理用のREST APIです。
商品情報の登録、一覧取得、更新、削除といった基本的なCRUD機能を実装しています。

バックエンド開発の基礎であるAPI設計、データベース連携、Dockerによる開発環境構築を学習する目的で作成しました。

## 使用技術
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- Git / GitHub

## 主な機能
- 商品情報の登録
- 商品一覧の取得
- 商品情報の更新
- 商品情報の削除
- PostgreSQLへのデータ保存
- Swagger UIによるAPI確認

## 工夫した点
FastAPIのルーティング、Pydanticによるデータ検証、SQLAlchemyを利用したデータベース操作を分けて実装しました。
また、Docker Composeを使用することで、アプリケーションとデータベースを同時に起動できるようにしました。

## 今後追加したい機能
- JWT認証機能
- ユーザー管理機能
- エラーハンドリングの改善
- AWSなどのクラウド環境へのデプロイ
