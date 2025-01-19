<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/syanification/Kora">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Korify</h3>

  <p align="center">
    No Ears Left Out!
    <br />
    <a href="https://github.com/syanification/Kora"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/syanification/Kora/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/syanification/Kora/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

**Korify** is a groundbreaking app designed to revolutionize the music listening experience for users with specific needs. Our mission is to enhance the usability of Spotify, the world's most popular music streaming platform, by providing seamless voice input functionality. With Korify, music is just a command away, making it easier than ever to enjoy your favorite tunes without lifting a finger.

#### Key Features:

- **Request a Song**: Simply ask for the song you want to hear, and Korify will play it instantly. No more scrolling through endless playlists!
- **Skip a Song**: Not feeling the current track? Just say the word, and Korify will skip to the next song.
- **Play/Pause a Song**: Control playback effortlessly with your voice. Whether you're in the middle of a workout or cooking dinner, Korify has you covered.
- **Play/Pause Button**: For those moments when you prefer a tactile experience, our intuitive play/pause button is always within reach.
- **Next Song Button**: Easily skip to the next track with a simple press, ensuring your music flow is never interrupted.

#### Why Choose Korify?

Korify is dedicated to making music accessible and enjoyable for everyone. Our app is designed with user-friendliness in mind, ensuring that your listening experience is as smooth and intuitive as possible. Whether you're a busy professional, a multitasking parent, or someone with specific accessibility needs, Korify is here to enhance your music journey.

Join the Korify community today and discover a new way to experience music. With Korify, your favorite songs are always just a voice command away.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


- Python 3
- OpenAI Model Fine Tuning
- Kivy
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

If you're interested in checking out our project here are the steps to get started!

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html">Conda</a>
* <a href="https://developer.spotify.com/">Spotify Developer Account</a>
* <a href="https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key">OpenAI API Key</a>


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/syanification/Kora.git
   ```
2. Create a new conda environment with requirements.txt
    ```sh
    conda create --name your_env --file requirements.txt
    ```
3. Create a new file in `src/` called `gptConfit.py` and put your API key inside.
    ```py
    API_KEY="YOUR-KEY"
    ```
4. Create a file `api-config.json` inside of `config/` and put your secret key and cid inside.
    ```json
    {
        "scope": "playlist-modify-private playlist-modify-public user-modify-playback-state user-read-playback-state",
        "cid": "YOUR-CID",
        "secret": "YOUR-SECRET-KEY",
        "redirectURI": "http://localhost:8888/callback"
    }
    ```
5. Enter your conda environment.
    ```sh
    conda activate your_env
    ```
6. Run `MusicPlayer.py`
    ```sh
    python src/MusicPlayer.py
    ```
7. The first time you use a function you will be prompted to sign into spotify, once you log in you are good to go! Enjoy :\)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<!-- 
## Usage

Current functionality is as follows:

- Request a song via voice prompt
- Skip a song via voice prompt
- Play / Pause a song via voice prompt
- Play / Pause button
- Next song button

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This project would not have been possible without these fantastic resources:

* <a href="https://www.flaticon.com/free-icons/mic" title="mic icons">Mic icons created by Dave Gandy - Flaticon</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: img/preview.png


