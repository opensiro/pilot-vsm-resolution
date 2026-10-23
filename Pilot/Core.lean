/-!
Small proof-engineering exercise for VSM-RES-001.
This is original pilot code, not part of Resolution's Hironaka proof.
-/

namespace Pilot

universe u

def append {α : Type u} : List α → List α → List α
  | [], ys => ys
  | x :: xs, ys => x :: append xs ys

def reverse {α : Type u} : List α → List α
  | [] => []
  | x :: xs => append (reverse xs) [x]

theorem append_nil {α : Type u} (xs : List α) : append xs [] = xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp [append, ih]

theorem append_assoc {α : Type u} (xs ys zs : List α) :
    append (append xs ys) zs = append xs (append ys zs) := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp [append, ih]

theorem reverse_append {α : Type u} (xs ys : List α) :
    reverse (append xs ys) = append (reverse ys) (reverse xs) := by
  induction xs with
  | nil =>
      simp [append, reverse, append_nil]
  | cons x xs ih =>
      calc
        reverse (append (x :: xs) ys)
            = append (reverse (append xs ys)) [x] := rfl
        _ = append (append (reverse ys) (reverse xs)) [x] := by rw [ih]
        _ = append (reverse ys) (append (reverse xs) [x]) := by rw [append_assoc]
        _ = append (reverse ys) (reverse (x :: xs)) := rfl

theorem reverse_involutive {α : Type u} (xs : List α) :
    reverse (reverse xs) = xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
      calc
        reverse (reverse (x :: xs))
            = reverse (append (reverse xs) [x]) := rfl
        _ = append (reverse [x]) (reverse (reverse xs)) := by rw [reverse_append]
        _ = x :: xs := by simp [reverse, append, ih]

end Pilot
