#lang racket

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (binary-tree-paths root)
  (match root
    [#f (list)]
    [(tree-node v #f #f) (list (format "~a" v))]
    [(tree-node v l r)
     (map (curry string-append (format "~a->" v))
          (append (binary-tree-paths l) (binary-tree-paths r)))]))
