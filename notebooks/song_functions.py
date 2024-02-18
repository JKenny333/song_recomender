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
    "\n",
    "def playlist_audio_features(username, playlist_id):\n",
    "    # Get tracks\n",
    "    tracks = get_playlist_tracks(username, playlist_id)\n",
    "    \n",
    "    # Get track ids, skipping None\n",
    "    track_ids = [i['track']['id'] for i in tracks if i['track']['id'] is not None]\n",
    "        \n",
    "    # Chopping track ids list in chunks of 100 songs \n",
    "    chunk_size = 100\n",
    "    track_ids_chopped = [track_ids[i:i + chunk_size] for i in range(0, len(track_ids), chunk_size)]\n",
    "    \n",
    "    # Get audio features\n",
    "    af_list = []\n",
    "    for chunk in track_ids_chopped:\n",
    "        try:\n",
    "            af_list.extend(sp.audio_features(chunk))\n",
    "        except TypeError as e:\n",
    "            print(f\"Error retrieving audio features for chunk: {e}\")\n",
    "    \n",
    "    # Create dataframe\n",
    "    af_df = pd.DataFrame(af_list)\n",
    "\n",
    "    return af_df"
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
