<div id="top"></div>
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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<!--
<div align="center">
  <a href="https://github.com/chrisjackr/Comptrain_Project">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
-->

<h3 align="center">Comptrain Project</h3>

  <p align="center">
    Simple webscraper to collect and save daily Comptrain CrossFit workouts.
    <!--
    <br />
    <a href="https://github.com/chrisjackr/Comptrain_Project"><strong>Explore the docs »</strong></a>
    <br />
-->
    <br />
    <!--
    <a href="https://github.com/chrisjackr/Comptrain_Project">View Demo</a>
    ·
    -->
    <a href="https://github.com/chrisjackr/Comptrain_Project/issues">Report Bug</a>
    ·
    <a href="https://github.com/chrisjackr/Comptrain_Project/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <!--<li><a href="#prerequisites">Prerequisites</a></li>-->
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <!--<li><a href="#usage">Usage</a></li>-->
    <!--<li><a href="#roadmap">Roadmap</a></li>-->
    <!--<li><a href="#contributing">Contributing</a></li>-->
    <!--<li><a href="#license">License</a></li>-->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->

This project is a simple webscraper that collects a CrossFit workout that is posted daily on the COMPTRAIN website. The script also saves the date and description to a file-based SQL database. The purpose of this project was to practise webscraping with _requests_, html parsing with _bs4_ and database manipulation with _sqlite3_. 

UPDATE:   See <a href="https://github.com/chrisjackr/Comptrain_Project">here</a> for my most recent webscraping project.

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps:

<!--
### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
-->

### Installation

1. Clone the repository to a suitable directory
   ```sh
   git clone https://github.com/chrisjackr/Comptrain_Project.git
   ```
2. Create virtual environment and install packages from requirements.txt
   ```sh
   cd ../Comptrain_Project
   py -m venv venv_name
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES 
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

<p align="right">(<a href="#top">back to top</a>)</p>
-->


<!-- ROADMAP 
## Roadmap

- [] Feature 1
- [] Feature 2
- [] Feature 3
    - [] Nested Feature

See the [open issues](https://github.com/chrisjackr/Comptrain_Project/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>
-->


<!-- CONTRIBUTING 
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>
-->


<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
-->


<!-- CONTACT -->
## Contact

Chris - chrisjackr

Project Link: [https://github.com/chrisjackr/Comptrain_Project](https://github.com/chrisjackr/Comptrain_Project)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []() See the <a href="https://comptrain.co/">COMPTRAIN website</a> for fantatic CrossFit workouts and programs!


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/chrisjackr/Comptrain_Project.svg?style=for-the-badge
[contributors-url]: https://github.com/chrisjackr/Comptrain_Project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/chrisjackr/Comptrain_Project.svg?style=for-the-badge
[forks-url]: https://github.com/chrisjackr/Comptrain_Project/network/members
[stars-shield]: https://img.shields.io/github/stars/chrisjackr/Comptrain_Project.svg?style=for-the-badge
[stars-url]: https://github.com/chrisjackr/Comptrain_Project/stargazers
[issues-shield]: https://img.shields.io/github/issues/chrisjackr/Comptrain_Project.svg?style=for-the-badge
[issues-url]: https://github.com/chrisjackr/Comptrain_Project/issues
[license-shield]: https://img.shields.io/github/license/chrisjackr/Comptrain_Project.svg?style=for-the-badge
[license-url]: https://github.com/chrisjackr/Comptrain_Project/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
