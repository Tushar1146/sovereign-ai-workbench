# SIH Demo Guide

## Goal

Demonstrate an end-to-end confidential industrial workflow using synthetic Pump P-102 data.

## Demo Inputs

1. Pump maintenance manual PDF
2. Pump inspection report PDF
3. Pump sensor CSV
4. Pump equipment image

## Demo Prompt

> Analyze Pump P-102 using the available documents, sensor data and image. Identify abnormalities, compare findings with the maintenance manual, provide an evidence-backed recommendation and prepare a maintenance report.

## Expected Flow

1. User submits the task.
2. Model Router classifies the task and selects an available local model.
3. RAG searches the local knowledge base.
4. Relevant document evidence is displayed.
5. Sensor data is analyzed with local tools.
6. Vision/OCR is used when a local vision model is available.
7. Agent cross-checks findings against the maintenance manual.
8. Evidence-backed recommendation is produced.
9. Word/Excel/PPT/PDF deliverables can be generated locally.
10. Audit logs capture the important actions.
11. Security panel shows local processing and external API activity.

## Demo Safety

Use synthetic data only. Do not upload MRPL or any other organization's confidential documents to a public repository or public demo environment.
