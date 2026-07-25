# AWS Sound Button Portfolio

## 1. プロジェクト概要

### 目的

AWSインフラエンジニア就職用ポートフォリオ

### コンセプト

AWSインフラを主役とした就職用ポートフォリオ

画面中央に大きなボタンを配置し、

・ボタンを押すとかわいい音が鳴る
・累計押下回数を表示する

アプリはできるだけシンプルにし、AWS Portfolio aws-sound-button
AWS設計・構築・運用をアピールすることを目的とする。

---

## 2. 使用技術

### AWS

・VPC
・Public Subnet
・Internet Gateway
・Route Table
・Security Group
・EC2
・IAM
・Route53
・S3
・DynamoDB
・CloudWatch
・（CloudFront：必要なら追加）

### ミドルウェア

・Docker
・Nginx

### バックエンド

・FastAPI（Python）

### IaC

・Terraform

### バージョン管理

・Git
・GitHub

---

## 3. AWS構成

### システム構成

Internet
↓
Route53
↓
EC2
↓
Docker
↓
Nginx
↓
FastAPI
↓
DynamoDB

S3（音声ファイル）

### 管理・運用

・Terraform
・IAM
・CloudWatch

## 4. 開発ロードマップ

1. GitHub初期設定
2. Terraform（AWS基盤）
3. Docker導入
4. Nginx構築
5. Webページ作成（HTML/CSS/JavaScript）
6. FastAPI実装
7. DynamoDB連携
8. S3連携
9. CloudWatch設定
10. Route53
11. HTTPS
12. README完成

---

## 5. 決定事項

- フロントはHTML/CSS/JavaScript
- DynamoDBには押下回数のみ保存
- AWSインフラエンジニアとして評価されやすく、面接で説明しやすい構成を優先する。
- ### GitHub Flow運用ルール
- mainブランチへ直接コミットしない
- 作業開始前にIssueを作成する
- Issueごとに feature/xxx ブランチを作成する
- 作業はfeatureブランチで行う
- 作業完了後にCommit・Pushする
- Pull Requestを作成する
- 内容を確認してMergeする
- Merge後にIssueをCloseする

## 6. 最終フェーズ

- Route53で独自ドメイン設定
- HTTPS対応（Let's Encrypt）
- README最終更新
- GitHub公開

### ゴール

AWSインフラエンジニアの面接において、
設計・構築・運用について説明できるポートフォリオを完成させる。
