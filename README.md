# Audio & Video Data Collection and Processing for Pedestrian Sensing

Welcome to the repository for our urban audio and video data collection and processing pipeline. This repository includes the necessary documentation and code to help you collect, annotate, and prepare audio and video files for modeling and analysis.

### Useful Links:
- 📦 **Download the Data**: Get access to the datasets on our [Huggingface page](https://huggingface.co/datasets/pseshadri9/ASPED).
- 🧠 **Training Code**: Explore the training code for our models in the [Model Repository](https://github.com/urbanaudiosensing/Models).
- 🌐 **More Information**: Visit our [official website](https://urbanaudiosensing.github.io) for further details about the data.


### What to Expect from This Repository

- **Acquisition**  
  - `sensor_deployment_guide` (PDF, Markdown): Documentation on how sensors were deployed to collect audio and video data.

- **Annotation**  
  - `ASPEDva`: Contains code for annotating pedestrian counts near audio recorders using video data.
    - `defining_csvformat.py`
    - `defining_ellipse_[session_name].py`
    - `labeling.py`
  - `ASPEDvb`: Additional annotation resources.
  - `(ASPEDvc)`: This folder is still under development and not yet public.

- **Processing**  
  - `Alignment`: Documentation and code to synchronize audio, video, and annotation files.
    - `video_and_label_alignment.ipynb`
    - `(audio_alignment.py)`: Not yet public. Aligns audio files.
    - `(final_alignment_checking.py)`: Not yet public. Ensures all data is correctly aligned.
    - `alignment_guide` (PDF, Markdown)
