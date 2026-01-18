import heapq
import random
import time

def generate_dummy_data(n=20):
    data = []
    for i in range(n):
        symbol = f"HISSE_{random.randint(100, 999)}"
        score = round(random.randint(0, 100), 2)
        data.append((score, symbol))
    return data

def process_market_data(stean_data, k=5):
    top_stocks_heap = []

    for score, symbol in stean_data:
        print()
        print(f"> {symbol}: {score} <")

        if len(top_stocks_heap) < k:
            heapq.heappush(top_stocks_heap, (score, symbol))
            print(f"[Eklendi ({symbol})]")

        else:
            current_min_score = top_stocks_heap[0][0]

            if score > current_min_score:

                removed = heapq.heappushpop(top_stocks_heap, (score, symbol))
                print(f"[Eklendi ({symbol})] | [Silindi ({removed[1]} {removed[0]})]")
            else:
                print(f"[Yetersiz momentum ({symbol})]")
        
        time.sleep(0.6)
    return top_stocks_heap


if __name__ == "__main__":

    market_stream = generate_dummy_data(n=30)

    final_top_stocks = process_market_data(market_stream, k=5)
    print("Top 5 HISSE")
    final_top_stocks.sort(key=lambda x : x[0], reverse=True)
    for rank, (score, symbol) in enumerate(final_top_stocks, 1):
        print(f"{rank}. {symbol} : {score}")
