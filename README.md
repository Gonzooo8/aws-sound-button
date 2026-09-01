# AWS Sound Button

AWS上に構築・公開した、シンプルなWebアプリケーションです。

画面上のボタンを押すと音声が再生され、累計押下回数が更新されます。

アプリケーション機能はシンプルにし、**TerraformによるAWSインフラ構築からDocker、Nginx、FastAPI、DynamoDB、S3、CloudWatch、Route 53、HTTPS公開までの一連の構築・運用を経験すること**を目的として作成しました。

## 公開URL

[https://okinawaaaaaaaaaaaaws.com](https://okinawaaaaaaaaaaaaws.com)

公開時間：08:00〜22:00（JST）

コスト最適化のため、22:00〜08:00はEC2を自動停止しています。

HTTPアクセスはNginxによってHTTPSへリダイレクトされます。

## システム構成

```text
Internet
   │
   ▼
Route 53
   │
   ▼
Elastic IP
   │
   ▼
EC2
│
├─ Docker Compose
│   ├─ Nginx
│   │    ↓
│   └─ FastAPI
│
├────────► DynamoDB
│          押下回数
│
└────────► S3
           音声ファイル

CloudWatch
ログ・メトリクス監視

```

## 使用技術

### AWS

- EC2
- VPC
- IAM
- DynamoDB
- S3
- CloudWatch
- Route 53
- EventBridge Scheduler

### Infrastructure / Backend

- Terraform
- Docker / Docker Compose
- Nginx
- Python
- FastAPI
- boto3

### Frontend

- HTML
- CSS
- JavaScript

### Development

- Git
- GitHub
- GitHub Issues / Pull Requests

## 主な機能

- ボタン押下による音声再生
- DynamoDBによる累計押下回数管理
- S3からの音声ファイル取得
- FastAPIによるAPI実装
- Nginxによるリバースプロキシ
- HTTP → HTTPSリダイレクト
- Let's EncryptによるHTTPS化
- CloudWatchによるログ・メトリクス監視
- TerraformによるAWSインフラのコード管理

## インフラ構成

Terraformを使用して、以下のAWSリソースをコード管理しています。

```text
AWS
├─ VPC
│  ├─ Internet Gateway
│  ├─ Route Table ── Public Subnetに関連付け
│  ├─ Security Group ── EC2に適用
│  └─ Public Subnet
│     └─ EC2
│
├─ IAM Role
├─ EventBridge Scheduler ── EC2を08:00起動 / 22:00停止
├─ DynamoDB
└─ S3
```

EC2上ではDocker Composeを使用し、NginxとFastAPIを別コンテナで実行しています。

FastAPIの8000番ポートは外部公開せず、Nginx経由でアクセスする構成です。

Terraform StateはローカルPCではなくS3 Remote Backendで管理しています。

S3 VersioningとState Lockを利用し、Stateの保護と複数環境からのTerraform実行を考慮した構成にしています。

## 開発フロー

GitHub Flowを使用しました。

```text
Issue
 ↓
Feature Branch
 ↓
実装・動作確認
 ↓
Pull Request
 ↓
Merge
 ↓
Issue Close
```

`main`へ直接コミットせず、Issue単位でfeatureブランチを作成して開発しました。

`main`ブランチにはGitHub Rulesetsを設定し、Pull Requestを経由して変更をマージする運用にしています。

## このプロジェクトで取り組んだこと

- TerraformによるInfrastructure as Code
- AWSネットワーク構築
- IAM最小権限設計
- Dockerを利用したアプリケーション環境構築
- Nginxによるリバースプロキシ
- FastAPIとAWSサービスの連携
- DynamoDBによるデータ管理
- S3によるファイル管理
- CloudWatchによる監視
- Route 53による独自ドメイン設定
- Let's EncryptによるHTTPS化
- GitHub Flowによる開発
- CloudWatch Logsやアプリケーションログを利用したトラブルシューティング
- EventBridge SchedulerによるEC2の自動停止・起動
- S3 Remote BackendによるTerraform State管理
- GitHub Rulesetsによるmainブランチ保護

## プロジェクトの目的

AWSサービスを個別に操作するだけでなく、

```text
設計
 ↓
Terraformによる構築
 ↓
アプリケーション実行
 ↓
AWSサービス連携
 ↓
監視
 ↓
DNS / HTTPS
 ↓
インターネット公開

```

までの一連の流れを経験することを目的として作成しました。

アプリケーション機能はあえてシンプルにし、AWSインフラ・Terraform・IAM・Docker・Nginx・監視・DNS・HTTPSなど、インフラ構築と運用を重点的に扱っています。
