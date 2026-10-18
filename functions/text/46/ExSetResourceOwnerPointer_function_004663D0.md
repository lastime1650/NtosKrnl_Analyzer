# ExSetResourceOwnerPointer

- RVA: `0x004663D0`–`0x00466403` (길이 `51` bytes)
- VA: `0x00000001404663D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `15`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004663EF` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004663F8` → [ExpSetResourceOwnerPointerEx](../34/ExpSetResourceOwnerPointerEx_function_00343E20.md) (function, `0x00343E20`)

### Direct callers
- [CcSetBcbOwnerPointer](../../page/71/CcSetBcbOwnerPointer_function_007103B0.md) at `0x007103D4`
- [CcSetBcbOwnerPointer](../../page/71/CcSetBcbOwnerPointer_function_007103B0.md) at `0x007103EB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004663D0  48 83 EC 38                     sub rsp, 0x38
004663D4  F6 41 1A 01                     test byte ptr [rcx + 0x1a], 1
004663D8  74 1B                           je 0x1404663f5
004663DA  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004663E0  45 33 C9                        xor r9d, r9d
004663E3  4C 8B C1                        mov r8, rcx
004663E6  B9 C6 01 00 00                  mov ecx, 0x1c6
004663EB  41 8D 51 0E                     lea edx, [r9 + 0xe]
004663EF  E8 6C 72 09 00                  call 0x1404fd660
004663F4  CC                              int3
004663F5  45 33 C0                        xor r8d, r8d
004663F8  E8 23 DA ED FF                  call 0x140343e20
004663FD  48 83 C4 38                     add rsp, 0x38
00466401  C3                              ret
00466402  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExSetResourceOwnerPointer(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    if (((*(unsigned __int8 *)(a1 + 26)) & (1)) != 0) {
        a4 = 0;
        a3 = a1;
        a1 = 454;
        a2 = a4 + 14;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a3 = 0;
    result = ExpSetResourceOwnerPointerEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExSetResourceOwnerPointer(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    if (((*(uint8_t *)(arg1 + 0x1A)) & (1)) != 0) {
        Arg4 = 0;
        Arg3 = Arg1;
        Arg1 = 454;
        Arg2 = Arg4 + 14;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg3 = 0;
    result = ExpSetResourceOwnerPointerEx(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004663D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004663D0[BB_004663D0]
  bb_004663DA[BB_004663DA]
  bb_004663F5[BB_004663F5]
  bb_00466402[BB_00466402]
  bb_004663D0 -->|branch| bb_004663F5
  bb_004663D0 -->|fallthrough| bb_004663DA
  bb_004663DA -->|flow| bb_004663F5
```
