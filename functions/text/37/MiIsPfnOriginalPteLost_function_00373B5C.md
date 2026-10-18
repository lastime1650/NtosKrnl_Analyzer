# MiIsPfnOriginalPteLost

- RVA: `0x00373B5C`–`0x00373B75` (길이 `25` bytes)
- VA: `0x0000000140373B5C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `9`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00373B6E` → [MiCanPfnOriginalPteBeLost](MiCanPfnOriginalPteBeLost_function_00373D3C.md) (function, `0x00373D3C`)

### Direct callers
- [MiStoreWriteModifiedPages](../2B/MiStoreWriteModifiedPages_function_002B46C4.md) at `0x002B499F`
- [MiStoreWriteModifiedPages](../2B/MiStoreWriteModifiedPages_function_002B46C4.md) at `0x002B4D85`
- [MiGatherPagefilePages](MiGatherPagefilePages_function_00372B08.md) at `0x00372D70`
- [MiWriteCompletePfn](MiWriteCompletePfn_function_003737C4.md) at `0x00373812`
- [MiWriteCompletePfn](MiWriteCompletePfn_function_003737C4.md) at `0x0037393D`
- [MiWritePageFileHash](../38/MiWritePageFileHash_function_00381DC8.md) at `0x00381F2B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00373B5C  48 83 EC 28                     sub rsp, 0x28
00373B60  F6 41 22 10                     test byte ptr [rcx + 0x22], 0x10
00373B64  75 08                           jne 0x140373b6e
00373B66  33 C0                           xor eax, eax
00373B68  48 83 C4 28                     add rsp, 0x28
00373B6C  C3                              ret
00373B6D  CC                              int3
00373B6E  E8 C9 01 00 00                  call 0x140373d3c
00373B73  EB F3                           jmp 0x140373b68
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiIsPfnOriginalPteLost(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned __int8 *)(a1 + 34)) & (16)) != 0) goto loc_00373B6E;
    result = 0;
loc_00373B68:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00373B6E:
    result = MiCanPfnOriginalPteBeLost(a1, a2, a3, a4);
    goto loc_00373B68;
}
```

## 5. (Beta) C Style

```c
int64_t MiIsPfnOriginalPteLost(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint8_t *)(arg1 + 0x22)) & (16)) != 0) goto loc_00373B6E;
    result = 0;
loc_00373B68:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00373B6E:
    result = MiCanPfnOriginalPteBeLost(Arg1, a2, a3, a4);
    goto loc_00373B68;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x22` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00373B5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00373B5C[BB_00373B5C]
  bb_00373B66[BB_00373B66]
  bb_00373B68[BB_00373B68]
  bb_00373B6D[BB_00373B6D]
  bb_00373B6E[BB_00373B6E]
  bb_00373B5C -->|branch| bb_00373B6E
  bb_00373B5C -->|fallthrough| bb_00373B66
  bb_00373B66 -->|flow| bb_00373B68
  bb_00373B6D -->|flow| bb_00373B6E
  bb_00373B6E -->|branch| bb_00373B68
```
