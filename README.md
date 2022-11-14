<div id="top"></div>
<!--
*** Template from: https://github.com/othneildrew/Best-README-Template
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/smart-hostel-mgmt-sys">
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

<h3 align="center">Smart Hostel Management System</h3>

  <p align="center">
    a CS462 Internet Of Things: Technology and Application Project
    <br />
    <a href="https://github.com/smart-hostel-mgmt-sys"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/VCjBWMjaBcI">View Video Demo</a>
    ·
    <a href="https://github.com/smart-hostel-mgmt-sys/issues">Report Bug</a>
    ·
    <a href="https://github.com/smart-hostel-mgmt-sys/issues">Request Feature</a>
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
        <li><a href="#troubleshooting">Troubleshooting</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li> -->
    <li><a href="#roadmap">Roadmap</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li> -->
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Dashboard Screenshoot 
<img
  align="center"
  src="media/dashboard_table.png"
  alt="dashboard_table"
  title="dashboard_table"
  style="display: inline-block; margin: 0 auto; max-width: 200px">

### Video Demo 
[![Video Demo](https://img.youtube.com/vi/VCjBWMjaBcI/0.jpg)](https://www.youtube.com/watch?v=VCjBWMjaBcI)


### Built With
* [Micro:bits](https://microbit.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [InfluxDB](https://www.influxdata.com/)
* [Vue.js](https://vuejs.org)

<p align="right">(<a href="#top">back to top</a>)</p>

### Directories

- [`/back_end`](https://github.com/MarkMa512/smart-hostel-mgmt-sys/tree/master/back_end): Flask backend application that interact with InfluxDB and provides REST API for the Front-end dashboard to interact  with.  

- [`/data_collection`](https://github.com/MarkMa512/smart-hostel-mgmt-sys/tree/master/data_collection): Data collection for sense making and visualization.  

    - [`/data_collection/data`]()  
    The light and sound data collected on 11/10/22 and 13/10/22 from a room.  
    Format: date, time, sounds, light  
    
  - [`/data_collection/data_reciever`](https://github.com/MarkMa512/smart-hostel-mgmt-sys/tree/master/data_collection/data_receiver)  
    A node.js application that reads the serial data from reciever microbit. 

  - [`/data_collection/desktop_client`]()  
    Desktop client written in Python that logs the data to CSV file into the [`/data_collection/data`]() directory.  

  - [`/data_collection/dummy_data`]() 
    Simulated data for demonstration purposes

- [`/front_end`](): Vue.js front-end dashboard 

- [`/sensor_and_gateway`](): Microbit programs and gateway porgam


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
1. Ensure [Python 3.9](https://www.python.org/downloads/) or higher is installed 
2. Ensure [Node.js 16](https://nodejs.org/en/) or higher is installed

### Sensors and device configuration: 
1. sensor_microbit_door_microbit
- Micro-controller: [Micro:bit V2](https://microbit.org/new-microbit/)
- Micro-controller Program: [`/sensor_and_gateway/sensor_door_microbit.py`]() 
- Extension board: [Octopus:bit(EF03405)](https://www.elecfreaks.com/learn-en/microbitExtensionModule/octopus_bit.html) 
- Sensors: 
  - HC-SR-04 Ultrasonic Distance Sensor (2)
  - Magnetic Sensor 

2. sensor_microbit_window_microbit
- Micro-controller: [Micro:bit V1](https://microbit.org/new-microbit/)
- Micro-controller Program: [`/sensor_and_gateway/sensor_window_microbit.py`]()  
- Extension board: [YWRobot micro:bit IO Extension Board](http://wiki.ywrobot.net/index.php?title=(SKU:BRD080003)IO_Extension_Board扩展板适用于Micro:bit)
- Sensors
  - HC SR501 PIR Motion Sensor 


3. reciever_microbit
- Micro-controller: [Micro:bit V1](https://microbit.org/new-microbit/)
- Micro-controller Program: [`/sensor_and_gateway/reciever_microbit.py`]()  


### Installation

To get a local copy up and running, follow these simple example steps.

1. Clone the repo
   ```sh
   git clone https://github.com/MarkMa512/smart-hostel-mgmt-sys.git
   ```
2. Enter the directory with CMD (Windows) or Terminal (macOS)

3. 


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Troubleshooting -->
## Troubleshooting


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation]()_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap
- [x] Feature 1:
  - [x] Feature a: 
  - [x] Feature b: 
  - [x] Feature c:
- [x] Feature 2: 
  - [x] Feature a: 
  - [x] Feature b: 
  - [x] Feature c: 
- [x] Feature 3: 
  - [x] Feature a: 
  - [x] Feature b: 
  - [x] Feature c: 


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Team Member:
- [Jin Ningxian](https://github.com/jinningxian)
- [Ma Ningzhi](https://github.com/MarkMa512)
- [Ng Jing Wen](https://github.com/ngjw1599)
- [Tan Jun An](https://github.com/junan-tan-2019)
- [Tan Keah Keat](https://github.com/kk-tan-2019)

<p align="right">(<a href="#top">back to top</a>)</p>