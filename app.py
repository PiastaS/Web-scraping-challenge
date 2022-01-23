{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc721f3f-6515-45fb-ba87-23dda3f12f5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect\n",
    "import pymongo\n",
    "import scrape_mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4855c576-e65a-4931-897d-11c28b2abf35",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create an instance of Flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0eeaca0c-f9b0-452f-b202-01f263e8a2b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use PyMongo to establish Mongo connection\n",
    "client = pymongo.MongoClient('mongodb://localhost:27017')\n",
    "db = client.mars_db\n",
    "collection = db.mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c2cbc12-6e8a-453c-9551-a61fd84886b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Se route using data from PyMongo\n",
    "@app.route('/')\n",
    "def index():\n",
    "    mars = collection.find_one()\n",
    "    return render_template('index.html', mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5450dd33-0e3a-469c-afa7-a9c581ccd983",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/scrape')\n",
    "def scrape():\n",
    "    scrape_mars.scrape()\n",
    "    return redirect('/', code = 302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a7f9283-0fac-49a1-90f5-8ed8255c21d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
