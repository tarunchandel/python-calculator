def find_winning_bidder(bids_list):
  highest_bid = 0
  highest_bidder = ""

  for name in bids_list:
    if bids_list[name] > highest_bid:
      highest_bidder = name
      highest_bid = bids_list[name]
  
  return([highest_bidder, highest_bid])