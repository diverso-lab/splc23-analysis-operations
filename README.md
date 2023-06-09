# splc23-analysis-operations
Code repository for SPLC'23 - Analysis Operations On The Run: Beyond Static Feature Model Analysis

<div align="center">

  <a href="">[![Commits Syntax Checker](https://github.com/joszamama/splc23-analysis-operations/actions/workflows/commits.yml/badge.svg?branch=main)](https://github.com/joszamama/flamapy-api/actions/workflows/commits.yml)</a>
  
</div>

# 

<div id="top"></div>
<br />
<div align="center">

  <h3 align="center">SPLC'23 - Analysis Operations On The Run</h3>

  <p align="center">
    Code repository for SPLC'23 - Analysis Operations On The Run: Beyond Static Feature Model Analysis
    <br />
    <a href="https://github.com/joszamama/flamapy-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/joszamama/flamapy-api/issues">Request Feature</a>
  </p>
</div>
<!-- ABOUT THE PROJECT -->

## About The Project

This project uses FLAMA for computing all the necesary operations in the paper "SPLC'23 - Analysis Operations On The Run: Beyond Static Feature Model Analysis" 

Intended workflow explained:
* User deploys the API with Docker (see Instalation)
* User access the API, reads /api/v1/docs
* User can now start using the API


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Docker](https://www.docker.com/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [FLAMA](https://github.com/diverso-lab/core)
* [Flasgger](https://github.com/flasgger/flasgger)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

First, you will need to install [Docker](https://docs.docker.com/desktop/).

### Instalation

1. Clone the repository

2. If you are running Windows, run
  ```sh
  $ cd flamapy-api
  $ ./start-server.cmd
  ```
  
3. If you are running Linux or MacOS, run
  ```sh
  $ cd flamapy-api
  $ ./start-server.sh
  ```
  
This script will build, install and deploy the API in http://localhost:5000, you can access all the endpoints through an application like [Postman](https://www.postman.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

### API Documentation

All the documentation is registered with Swagger UI and OAS 3.0. It is accesible through /api/v1/docs.

<p align="right">(<a href="#top">back to top</a>)</p>

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

<p align="right">(<a href="#top">back to top</a>)</p>
