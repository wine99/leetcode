#lang racket

(define (letter-combinations digits)
  (define ht #hash((#\2 . ("a" "b" "c"))
                   (#\3 . ("d" "e" "f"))
                   (#\4 . ("g" "h" "i"))
                   (#\5 . ("j" "k" "l"))
                   (#\6 . ("m" "n" "o"))
                   (#\7 . ("p" "q" "r" "s"))
                   (#\8 . ("t" "u" "v"))
                   (#\9 . ("w" "x" "y" "z"))))
  (match (string-length digits)
    [0 '()]
    [1 (hash-ref ht (string-ref digits 0))]
    [_ (map (curry apply string-append)
            (cartesian-product (hash-ref ht (string-ref digits 0))
                               (letter-combinations (substring digits 1))))]))
