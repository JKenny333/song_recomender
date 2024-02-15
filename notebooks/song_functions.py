{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7111f409-22b5-4086-8b36-0a263854f44e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_playlist_tracks(username, playlist_id):\n",
    "    results = sp.user_playlist_tracks(username,playlist_id,market=\"GB\")\n",
    "    tracks = results['items']\n",
    "    while results['next']:\n",
    "        results = sp.next(results)\n",
    "        tracks.extend(results['items'])\n",
    "    return tracks\n",
    "\n",
    "\n",
    "def load(filename = \"filename.pickle\"): \n",
    "    try: \n",
    "        with open(filename, \"rb\") as f: \n",
    "            return pickle.load(f) \n",
    "        \n",
    "    except FileNotFoundError: \n",
    "        print(\"File not found!\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
