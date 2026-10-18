# FindNodeOrParent

- RVA: `0x003E5C10`–`0x003E5C2C` (길이 `28` bytes)
- VA: `0x00000001403E5C10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00094F14`
- 디코드: `9`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_003E5A63](Unknown_function_003E5A63.md) at `0x003E5A75`
- [RtlLookupFirstMatchingElementGenericTableAvl](RtlLookupFirstMatchingElementGenericTableAvl_function_003E5B70.md) at `0x003E5B9E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003E5C26` → [sub_003E5CCE + 0x1](Unknown_function_003E5CCE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003E5C10  40 56                           push rsi
003E5C12  57                              push rdi
003E5C13  41 56                           push r14
003E5C15  48 83 EC 20                     sub rsp, 0x20
003E5C19  83 79 2C 00                     cmp dword ptr [rcx + 0x2c], 0
003E5C1D  4D 8B F0                        mov r14, r8
003E5C20  48 8B F2                        mov rsi, rdx
003E5C23  48 8B F9                        mov rdi, rcx
003E5C26  0F 84 A3 00 00 00               je 0x1403e5ccf
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall FindNodeOrParent(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void FindNodeOrParent(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E5C10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E5C10[BB_003E5C10]
```
