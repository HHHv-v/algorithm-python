h,m,k=map(int,input().split())
total_minutes=h*60+m+k
total_minutes%=24*60
print(f"{total_minutes//60} {total_minutes%60}")