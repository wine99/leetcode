#lang racket

(define (generate-parenthesis n)
  (define add-l (curry string-append "("))
  (define add-r (curry string-append ")"))
  (define (recur l r)
    (match* (l r)
      [(0 _) (list (make-string r #\)))]
      [(_ _) #:when (= l r) (map add-l (recur (sub1 l) r))]
      [(_ _) #:when (< l r)
       (append (map add-l (recur (sub1 l) r))
               (map add-r (recur l (sub1 r))))]))
  (recur n n))
