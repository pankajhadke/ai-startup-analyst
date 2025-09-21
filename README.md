# AI Analyst for Startup Evaluation (phaAI-gen)

## Overview

This project, phaAI-gen, is an AI-powered analyst platform. It streamlines the evaluation of early-stage startups. It synthesizes unstructured founder materials (pitch decks in JPG and PDF format) and external benchmark data to generate concise, actionable investment deal notes.

## Key Features

-   **Intelligent Ingestion:** Extracts text from both image-based (JPG) and multi-page (PDF) documents using Google Cloud Vision.
-   **AI-Powered Summary:** Uses Google's Vertex AI (Gemini model) to generate a professional executive summary.
-   **Dynamic Benchmarking:** Compares startup metrics against sector-specific and geographic data from a local CSV file.
-   **Automated Risk Assessment:** Flags potential risks based on predefined rules and benchmark comparisons.
-   **Structured Output:** Delivers a clear, human-readable deal note through an intuitive web-based user interface.

## Tech Stack

-   **Google Cloud:** Cloud Vision, Vertex AI (Gemini), Cloud Run.
-   **Python:** Flask (web framework), `pdf2image` (for PDF handling).
-   **Other:** Docker (for containerization on Cloud Run).

## Live Demo

Check out the live prototype running on Google Cloud Run:

**[https://phaai-gen-1043984975656.asia-southeast1.run.app/]**

**[phaAI-gen]**

## GitHub Repository

**[https://github.com/pankajhadke/ai-startup-analyst.git]**

## Getting Started

For detailed setup and testing instructions for this prototype, please refer to the **[INSTRUCTIONS.md](INSTRUCTIONS.md)** file in this repository.
