docker start cd7242

export $(cat .env)

#原本為 eval $(cat .env | sed 's/^/export /')
#但shell script 不能這麼做export，故直接去掉eval()
#並改以 source執行，而非 ./ 執行。

#原本以為上法可，但後來確認不行。最後改為 export $(cat .env)



