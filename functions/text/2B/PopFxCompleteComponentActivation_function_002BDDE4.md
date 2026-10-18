# PopFxCompleteComponentActivation

- RVA: `0x002BDDE4`–`0x002BDE5D` (길이 `121` bytes)
- VA: `0x00000001402BDDE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C748`
- 디코드: `34`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002BDDFC` → [PopFxDeviceCriticalRegionEnter](../4F/PopFxDeviceCriticalRegionEnter_function_004F09A0.md) (function, `0x004F09A0`)
- `0x002BDE12` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x002BDE28` → [PopFxIdleComponent](../2C/PopFxIdleComponent_function_002C01D8.md) (function, `0x002C01D8`)
- `0x002BDE35` → [PopFxDereferenceDevice](../27/PopFxDereferenceDevice_function_0027038C.md) (function, `0x0027038C`)
- `0x002BDE3D` → [PopFxDeviceCriticalRegionLeave](../4F/PopFxDeviceCriticalRegionLeave_function_004F1330.md) (function, `0x004F1330`)
- `0x002BDE56` → [PopFxActivateComponentDependents](PopFxActivateComponentDependents_function_002BE9F0.md) (function, `0x002BE9F0`)

### Direct callers
- [sub_002BD41B](Unknown_function_002BD41B.md) at `0x002BD6A6`
- [PopFxActivateComponentWorker](../2D/PopFxActivateComponentWorker_function_002D9F60.md) at `0x002D9FE9`
- [PopFxIdleWorkerTail](../43/PopFxIdleWorkerTail_function_0043CDA0.md) at `0x0043CF17`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002BDDE4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002BDDE9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
002BDDEE  57                              push rdi
002BDDEF  48 83 EC 20                     sub rsp, 0x20
002BDDF3  41 8A D8                        mov bl, r8b
002BDDF6  48 8B FA                        mov rdi, rdx
002BDDF9  48 8B F1                        mov rsi, rcx
002BDDFC  E8 9F 2B 23 00                  call 0x1404f09a0
002BDE01  F0 81 4A 58 00 00 00 80         lock or dword ptr [rdx + 0x58], 0x80000000
002BDE09  48 8D 4A 68                     lea rcx, [rdx + 0x68]
002BDE0D  45 33 C0                        xor r8d, r8d
002BDE10  33 D2                           xor edx, edx
002BDE12  E8 F9 14 08 00                  call 0x14033f310
002BDE17  84 DB                           test bl, bl
002BDE19  75 38                           jne 0x1402bde53
002BDE1B  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
002BDE1E  45 33 C9                        xor r9d, r9d
002BDE21  48 8B CE                        mov rcx, rsi
002BDE24  45 8D 41 01                     lea r8d, [r9 + 1]
002BDE28  E8 AB 23 00 00                  call 0x1402c01d8
002BDE2D  BA 08 00 00 00                  mov edx, 8
002BDE32  48 8B CE                        mov rcx, rsi
002BDE35  E8 52 25 FB FF                  call 0x14027038c
002BDE3A  48 8B CE                        mov rcx, rsi
002BDE3D  E8 EE 34 23 00                  call 0x1404f1330
002BDE42  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002BDE47  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
002BDE4C  48 83 C4 20                     add rsp, 0x20
002BDE50  5F                              pop rdi
002BDE51  C3                              ret
002BDE52  CC                              int3
002BDE53  48 8B CF                        mov rcx, rdi
002BDE56  E8 95 0B 00 00                  call 0x1402be9f0
002BDE5B  EB BE                           jmp 0x1402bde1b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxCompleteComponentActivation(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = PopFxDeviceCriticalRegionEnter(a1, a2, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(a2 + 104, a2, a3, a4);
    if ((unsigned __int8)((unsigned __int8)(a3)) != 0) goto loc_002BDE53;
loc_002BDE1B:
    a4 = 0;
    result = PopFxIdleComponent(a1, (unsigned int)(*(unsigned int *)(a2 + 16)), a4 + 1, a4);
    result = PopFxDereferenceDevice(a1, 8, a4 + 1, a4);
    result = PopFxDeviceCriticalRegionLeave(a1, 8, a4 + 1, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_002BDE53:
    result = PopFxActivateComponentDependents(0, 8, a4 + 1, a4);
    goto loc_002BDE1B;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxCompleteComponentActivation(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = PopFxDeviceCriticalRegionEnter(Arg1, Arg2, Arg3, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(Arg2 + 104, Arg2, Arg3, Arg4);
    if ((uint8_t)((uint8_t)(Arg3)) != 0) goto loc_002BDE53;
loc_002BDE1B:
    Arg4 = 0;
    result = PopFxIdleComponent(Arg1, (uint32_t)(*(uint32_t *)(arg2 + 0x10)), Arg4 + 1, Arg4);
    result = PopFxDereferenceDevice(Arg1, 8, Arg4 + 1, Arg4);
    result = PopFxDeviceCriticalRegionLeave(Arg1, 8, Arg4 + 1, Arg4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_002BDE53:
    result = PopFxActivateComponentDependents(0, 8, Arg4 + 1, Arg4);
    goto loc_002BDE1B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002BDDE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002BDDE4[BB_002BDDE4]
  bb_002BDE1B[BB_002BDE1B]
  bb_002BDE52[BB_002BDE52]
  bb_002BDE53[BB_002BDE53]
  bb_002BDDE4 -->|branch| bb_002BDE53
  bb_002BDDE4 -->|fallthrough| bb_002BDE1B
  bb_002BDE52 -->|flow| bb_002BDE53
  bb_002BDE53 -->|branch| bb_002BDE1B
```
