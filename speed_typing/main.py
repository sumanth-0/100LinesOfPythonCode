#!/usr/bin/env python3
import curses, random, time, argparse, nltk, os
from nltk.corpus import words
from statistics import mean, stdev

def setup_words():
    try:
        nltk.data.find('corpora/words'); return list(words.words())
    except Exception:
        try: nltk.download('words', quiet=True); return list(words.words())
        except Exception: return ['the','and','of','to','a','in','is','it','you','that']

def gen_text(n, wl):
    s=''; first=True
    while len(s) < n:
        w=random.choice(wl).lower()
        if len(w)>2:
            s += ('' if first else ' ') + w; first=False
    return s

class S:
    def __init__(self): self.correct=self.incorrect=self.corrections=0; self.time=0; self.cps=self.accuracy=self.wpm=0
    def calc(self,total,time_taken):
        self.time=max(0.1,time_taken); tt=self.correct+self.incorrect
        self.cps=tt/self.time; self.wpm=(self.correct/self.time*60)/5
        self.accuracy=self.correct/max(1,tt)*100

def run(stdscr,text):
    curses.init_pair(1,curses.COLOR_GREEN,0); curses.init_pair(2,curses.COLOR_RED,0)
    stdscr.timeout(100)
    stats=S(); typed=[]; pos=0; start=None; waiting=True; last_key=None; line=4
    stdscr.addstr(0,0,"Target:"); stdscr.addstr(1,0,text); stdscr.addstr(3,0,"Press ENTER to start or ESC to exit")
    while True:
        ch=stdscr.getch(); now=time.time()
        if ch==-1:
            if not waiting and last_key and (now-last_key>5): stdscr.addstr(5,0,"Still there? ESC to quit or any key to continue...")
            continue
        last_key=now
        if waiting:
            if ch==10: waiting=False; start=now; stdscr.clear(); stdscr.addstr(0,0,"Target:"); stdscr.addstr(1,0,text); stdscr.addstr(3,0,"Your input:"); stdscr.move(line,0); continue
            if ch==27: return stats
            continue
        if ch==10: break
        if ch==27: return stats
        if ch in (127,curses.KEY_BACKSPACE):
            if typed: typed.pop(); pos-=1; stats.corrections+=1; stdscr.move(line,0); stdscr.clrtoeol()
            for i,chc in enumerate(typed): stdscr.addstr(line,i,chc, curses.color_pair(1) if chc==text[i] else curses.color_pair(2))
            continue
        if ch<256 and chr(ch).isprintable() and pos<len(text):
            c=chr(ch); typed.append(c)
            if c==text[pos]: stats.correct+=1; col=1
            else: stats.incorrect+=1; col=2
            stdscr.addstr(line,pos,c,curses.color_pair(col)); pos+=1
    end=time.time(); stats.calc(len(text), (end-start) if start else 0); return stats

def show(attempts):
    print("\nStatistics\n"+"-"*40)
    for i,s in enumerate(attempts,1):
        tot=s.correct+s.incorrect
        print(f"\nAttempt {i}: total={tot} correct={s.correct} incorrect={s.incorrect} corrections={s.corrections} time={s.time:.2f}s wpm={s.wpm:.2f} acc={s.accuracy:.2f}%")
    if len(attempts)>1:
        wpms=[a.wpm for a in attempts]; cps=[a.cps for a in attempts]; acc=[a.accuracy for a in attempts]
        print("\nSummary\n"+"-"*40)
        print(f"Avg WPM: {mean(wpms):.2f}" + (f"  Std: {stdev(wpms):.2f}" if len(wpms)>1 else ""))
        print(f"Avg chars/sec: {mean(cps):.2f}  Avg acc: {mean(acc):.2f}%")


def main():
    p=argparse.ArgumentParser(); p.add_argument('-r','--repetitions',type=int,default=1); p.add_argument('-c','--characters',type=int,default=100)
    args=p.parse_args()
    wl=setup_words()
    texts=[gen_text(args.characters,wl) for _ in range(args.repetitions)]
    attempts=[]
    try:
        for i,t in enumerate(texts,1):
            if args.repetitions>1:
                input(f"\nTest {i}/{args.repetitions}. Press Enter when ready...")
            stats=curses.wrapper(run,t)
            if stats.correct==0 and stats.incorrect==0:
                print("\nTest cancelled"); break
            attempts.append(stats)
    except KeyboardInterrupt:
        print("\nInterrupted")
    if attempts: show(attempts)

if __name__=='__main__':
    main()
