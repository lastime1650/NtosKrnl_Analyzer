# SymCryptFdefModElementCopy

- RVA: `0x0053449C`–`0x005344BA` (길이 `30` bytes)
- VA: `0x000000014053449C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005344AF` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [SymCryptModElementCopy](../52/SymCryptModElementCopy_function_005258E8.md) at `0x005258EC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053449C  48 83 EC 28                     sub rsp, 0x28
005344A0  49 8B C0                        mov rax, r8
005344A3  49 3B D0                        cmp rdx, r8
005344A6  74 0C                           je 0x1405344b4
005344A8  44 8B 41 10                     mov r8d, dword ptr [rcx + 0x10]
005344AC  48 8B C8                        mov rcx, rax
005344AF  E8 8C 23 19 00                  call 0x1406c6840
005344B4  48 83 C4 28                     add rsp, 0x28
005344B8  C3                              ret
005344B9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModElementCopy(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = a3;
    if (a2 != a3) {
        a3 = *(unsigned int *)(a1 + 16);
        a1 = a3;
        result = memcpy(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModElementCopy(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Arg3;
    if (Arg2 != Arg3) {
        Arg3 = *(uint32_t *)(arg1 + 0x10);
        Arg1 = Arg3;
        result = memcpy(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053449C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0053449C[BB_0053449C]
  bb_005344A8[BB_005344A8]
  bb_005344B4[BB_005344B4]
  bb_005344B9[BB_005344B9]
  bb_0053449C -->|branch| bb_005344B4
  bb_0053449C -->|fallthrough| bb_005344A8
  bb_005344A8 -->|flow| bb_005344B4
```
