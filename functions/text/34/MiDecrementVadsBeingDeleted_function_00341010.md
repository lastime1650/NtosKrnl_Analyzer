# MiDecrementVadsBeingDeleted

- RVA: `0x00341010`–`0x0034103D` (길이 `45` bytes)
- VA: `0x0000000140341010`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00341032` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [MiFinishVadDeletion](../43/MiFinishVadDeletion_function_00430ED0.md) at `0x00431033`
- [MiCoalescePlaceholderAllocations](../../page/88/MiCoalescePlaceholderAllocations_function_0088095C.md) at `0x00880B01`
- [MiReserveUserMemory](../../page/88/MiReserveUserMemory_function_00884498.md) at `0x00884B92`
- [sub_00885634](../../page/88/Unknown_function_00885634.md) at `0x008857A8`
- [MiFinishPlaceholderVadReplacement](../../page/A8/MiFinishPlaceholderVadReplacement_function_00A87630.md) at `0x00A87676`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00341010  48 83 EC 28                     sub rsp, 0x28
00341014  B8 FF FF FF FF                  mov eax, 0xffffffff
00341019  F0 0F C1 81 E8 00 00 00         lock xadd dword ptr [rcx + 0xe8], eax
00341021  83 F8 01                        cmp eax, 1
00341024  75 11                           jne 0x140341037
00341026  48 8B 89 00 01 00 00            mov rcx, qword ptr [rcx + 0x100]
0034102D  45 33 C0                        xor r8d, r8d
00341030  33 D2                           xor edx, edx
00341032  E8 D9 E2 FF FF                  call 0x14033f310
00341037  48 83 C4 28                     add rsp, 0x28
0034103B  C3                              ret
0034103C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDecrementVadsBeingDeleted(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(0xFFFFFFFFULL);
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) == 1) {
        a1 = *(unsigned __int64 *)(a1 + 256);
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDecrementVadsBeingDeleted(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(0xFFFFFFFFULL);
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) == 1) {
        Arg1 = *(uint64_t *)(arg1 + 0x100);
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xE8` | `32` | `R/W` |
| `Arg1` | `+ 0x100` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00341010&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00341010[BB_00341010]
  bb_00341026[BB_00341026]
  bb_00341037[BB_00341037]
  bb_0034103C[BB_0034103C]
  bb_00341010 -->|branch| bb_00341037
  bb_00341010 -->|fallthrough| bb_00341026
  bb_00341026 -->|flow| bb_00341037
```
