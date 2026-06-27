from flask import Flask, render_template

app = Flask(__name__)

bikes = [
    {
        "id": 1,
        "name": "Royal Enfield Classic 350",
        "price": "₹2,15,000",
        "color": "Stealth Black",
        "brand": "Royal Enfield",
        "engine": "349 cc",
        "mileage": "35 km/l",
        "top_speed": "114 km/h",
        "rating": "4.8",
        "image": "https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=900&q=80"
    },
    {
        "id": 2,
        "name": "Yamaha R15 V4",
        "price": "₹1,95,000",
        "color": "Racing Blue",
        "brand": "Yamaha",
        "engine": "155 cc",
        "mileage": "45 km/l",
        "top_speed": "140 km/h",
        "rating": "4.7",
        "image": "https://images.unsplash.com/photo-1609630875171-b1321377ee65?auto=format&fit=crop&w=900&q=80"
    },
    {
        "id": 3,
        "name": "KTM Duke 390",
        "price": "₹3,30,000",
        "color": "Orange",
        "brand": "KTM",
        "engine": "398 cc",
        "mileage": "28 km/l",
        "top_speed": "170 km/h",
        "rating": "4.9",
        "image": "https://images.unsplash.com/photo-1517846693594-1567da72af75?auto=format&fit=crop&w=900&q=80"
    },
    {
        "id": 4,
        "name": "TVS Apache RTR 160",
        "price": "₹1,45,000",
        "color": "Red",
        "brand": "TVS",
        "engine": "159.7 cc",
        "mileage": "47 km/l",
        "top_speed": "114 km/h",
        "rating": "4.6",
        "image": "https://images.unsplash.com/photo-1558981359-219d6364c9c8?auto=format&fit=crop&w=900&q=80"
    },
    {
        "id": 5,
        "name": "BMW G310R",
        "price": "₹3,10,000",
        "color": "White",
        "brand": "BMW",
        "engine": "313 cc",
        "mileage": "30 km/l",
        "top_speed": "145 km/h",
        "rating": "4.8",
        "image": "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=900&q=80"
    },
    {
        "id": 6,
        "name": "Kawasaki Ninja ZX-6R",
        "price": "₹11,20,000",
        "color": "Lime Green",
        "brand": "Kawasaki",
        "engine": "636 cc",
        "mileage": "20 km/l",
        "top_speed": "250 km/h",
        "rating": "5.0",
        "image": "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&w=900&q=80"
    }
]

offers = [
    {
        "title": "Flat ₹20,000 OFF",
        "description": "On Royal Enfield Classic 350"
    },
    {
        "title": "0% EMI",
        "description": "Available for 12 Months"
    },
    {
        "title": "Free Helmet",
        "description": "With Every Premium Bike"
    }
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        bikes=bikes,
        offers=offers
    )


@app.route("/bikes")
def bike_list():
    return render_template(
        "bikes.html",
        bikes=bikes
    )


@app.route("/offers")
def offer_page():
    return render_template(
        "offers.html",
        offers=offers
    )


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/booking/<int:bike_id>")
def booking(bike_id):

    bike = next(
        (bike for bike in bikes if bike["id"] == bike_id),
        None
    )

    if bike:
        return render_template(
            "booking.html",
            bike=bike
        )

    return "<h2>Bike Not Found</h2>"


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
