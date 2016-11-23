for i in {0..2}
do
	redis-cli lpush douban:start_urls https://book.douban.com/tag/小说?start=$[i * 10]
done
