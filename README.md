# 🚀 Smart Task Board

![App Screenshot](https://via.placeholder.com/800x400.png?text=Replace+this+with+a+screenshot+of+your+app!)

Hey there! 👋 Welcome to my Smart Task Board. 

I built this project to get hands-on experience with building and deploying a production-ready, 3-tier web application. It’s more than just a simple to-do list—it’s a fully containerized system built with modern tools and deployed live to the cloud on an AWS EC2 instance. 

Feel free to poke around the live version or spin it up on your own machine!

## 🌍 Try it out live
* **Live App:** [http://YOUR_EC2_PUBLIC_IP](http://YOUR_EC2_PUBLIC_IP) *(Notice there's no port number needed, thanks to Nginx!)*
* **Backend API Docs:** [http://YOUR_EC2_PUBLIC_IP:8000/docs](http://YOUR_EC2_PUBLIC_IP:8000/docs)

---

## 🛠️ The Tech Stack (What makes it tick)

I wanted to use industry-standard tools for every layer of this application:

* **The Frontend (UI):** Built with **Next.js**, **React**, and **Tailwind CSS**. It provides a snappy, beautiful user experience.
* **The Backend (API):** Powered by **Python** and **FastAPI**. It's incredibly fast and automatically generates interactive API documentation.
* **The Database:** **PostgreSQL** handles the permanent data storage safely and reliably.
* **The Infrastructure:** The whole system is containerized with **Docker & Docker Compose**, hidden behind an **Nginx** reverse proxy, and hosted on an **AWS EC2** Linux server.

---

## 🏗️ How it all connects

Here is a quick look at the architecture under the hood. When a user visits the site, Nginx acts as the traffic cop (on port 80), routing them to the Next.js frontend, which in turn grabs data from the Python backend!

```mermaid
graph TD;
    Client([💻 User's Browser]) -->|HTTP Port 80| Proxy[🚦 Nginx Reverse Proxy];
    
    subgraph "Docker Environment (AWS EC2)"
        Proxy -->|Routes to Port 3000| Frontend[⚛️ Next.js Frontend];
        Frontend -->|API Fetch Port 8000| Backend[🐍 FastAPI Backend];
        Backend -->|SQL Port 5432| Database[(🐘 PostgreSQL)];
    end
💻 Run it on your own machine
Want to test the code yourself? You don't need to install Python, Node, or PostgreSQL on your computer. Because the whole app is containerized, you just need Docker!

1. Clone this repository:
```bash
git clone https://www.google.com/search?q=https://github.com/shivamnagrgit/smart-task-board.git
cd smart-task-board
```

2. Start the magic (Docker):
```bash
docker compose up -d --build
or docker-compose up -d --build
```

3. Check it out:

Open your browser and go to http://localhost

To see the API docs, go to http://localhost:8000/docs

Thanks for checking out my project! If you have any feedback or questions, I'd love to connect.


### Don't forget this below things! 😉
1. Replace `YOUR_EC2_PUBLIC_IP` with your actual IP address.
2. Replace `YOUR_USERNAME` with your GitHub username.
3. Upload that real screenshot to replace the placeholder link at the top (using the GitHub Issues trick we talked about earlier).

How does this version feel? It's friendly, highly readable, but still packs a massive technical punch!

"IMPORTANT NOTE"
before doing this all you must change the ip address to your public ip adddress in a file named frontend/src/app look for a line saying  WARNING: Put your actual EC2 Public IP address here! 
