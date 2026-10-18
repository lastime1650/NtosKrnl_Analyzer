# sub_009BCBB2

- RVA: `0x009BCBB2`–`0x009BCBCB` (길이 `25` bytes)
- VA: `0x00000001409BCBB2`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009F16C`
- 디코드: `7`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009BCBC4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009BCBC4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009BCBBF` → [sub_009BCB28 + 0x54](Unknown_function_009BCB28.md) (`tail-transfer`)
  - `0x009BCBC9` → [sub_009BCB28 + 0x48](Unknown_function_009BCB28.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009BCBB2  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
009BCBB9  48 2B C6                        sub rax, rsi
009BCBBC  48 03 E8                        add rbp, rax
009BCBBF  EB BB                           jmp 0x1409bcb7c
009BCBC1  49 8B C4                        mov rax, r12
009BCBC4  E8 07 DF CF FF                  call 0x1406baad0
009BCBC9  EB A5                           jmp 0x1409bcb70
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009BCBB2(void)
{
    __int64 result;
    __int64 v_rbp;

    result = (-1) - (v_rsi);
    v_rbp = (v_rbp) + (result);
}
```

## 5. (Beta) C Style

```c
void sub_009BCBB2(void)
{
    int64_t result;
    int64_t local_rbp;

    result = (-1) - (local_rsi);
    local_rbp = (local_rbp) + (result);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009BCBB2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009BCBB2[BB_009BCBB2]
  bb_009BCBC1[BB_009BCBC1]
```
