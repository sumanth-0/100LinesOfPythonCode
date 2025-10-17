#!/usr/bin/env python3
import argparse
import sys

def square(n, filled=True):
    """Square (filled or hollow)."""
    for r in range(n):
        if filled or r in (0, n - 1):
            print('* ' * n)
        else:
            print('* ' + '  ' * (n - 2) + '*')

def right_triangle(n, filled=True):
    """Right-angled triangle (filled or hollow)."""
    for r in range(1, n + 1):
        if filled or r in (1, n):
            print('* ' * r)
        else:
            print('* ' + '  ' * (r - 2) + '*')

def pyramid(n):
    """Centered pyramid."""
    for r in range(n):
        print(' ' * (n - r - 1) + '* ' * (r + 1))

def diamond(n):
    """Diamond. n should be odd for symmetry; uses integer math otherwise."""
    mid = n // 2
    for r in range(n):
        dist = abs(mid - r)
        stars = mid - dist + 1
        print(' ' * dist + '* ' * stars)

def hourglass(n):
    """Hourglass (like inverted pyramid on top of pyramid)."""
    mid = (n + 1) // 2
    # top inverted pyramid
    for r in range(mid):
        print(' ' * r + '* ' * (mid - r))
    # bottom pyramid
    for r in range(mid - 1):
        print(' ' * (mid - r - 2) + '* ' * (r + 2))

def checkerboard(n):
    """Checkerboard pattern."""
    for r in range(n):
        row = []
        for c in range(n):
            row.append('# ' if (r + c) % 2 == 0 else '  ')
        print(''.join(row))

def x_pattern(n):
    """X pattern across an n x n grid."""
    for r in range(n):
        row = []
        for c in range(n):
            row.append('* ' if c == r or c == n - r - 1 else '  ')
        print(''.join(row))

PATTERNS = {
    'square': square,
    'triangle': right_triangle,
    'pyramid': pyramid,
    'diamond': diamond,
    'hourglass': hourglass,
    'checker': checkerboard,
    'x': x_pattern,
}

def parse_args(argv):
    p = argparse.ArgumentParser(description='Print ASCII art patterns.')
    p.add_argument('-p', '--pattern', choices=PATTERNS, default='diamond',
                   help='pattern name')
    p.add_argument('-s', '--size', type=int, default=7,
                   help='size (recommended odd for some patterns)')
    p.add_argument('--hollow', action='store_true',
                   help='use hollow variant where applicable')
    return p.parse_args(argv)

def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    n = max(1, args.size)
    func = PATTERNS[args.pattern]
    # Patterns that support filled/hollow
    if args.pattern in ('square', 'triangle'):
        func(n, not args.hollow)
    else:
        func(n)

if __name__ == '__main__':
    main()