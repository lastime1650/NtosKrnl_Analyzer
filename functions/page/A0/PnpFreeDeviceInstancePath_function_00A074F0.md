# PnpFreeDeviceInstancePath

- RVA: `0x00A074F0`–`0x00A0753F` (길이 `79` bytes)
- VA: `0x0000000140A074F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068790`
- 디코드: `22`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A07504` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x00A07522` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00A07538` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [IopDestroyDeviceNode](IopDestroyDeviceNode_function_00A06A3C.md) at `0x00A06AD8`
- [PiBuildDeviceNodeInstancePath](PiBuildDeviceNodeInstancePath_function_00A08DEC.md) at `0x00A08EF0`

### Static image references
- `0x00A074FD` → RVA `0x00F8CB40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A07504` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x00A07522` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x00A07538` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A074F0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A074F5  57                              push rdi
00A074F6  48 83 EC 20                     sub rsp, 0x20
00A074FA  48 8B D9                        mov rbx, rcx
00A074FD  48 8D 0D 3C 56 58 00            lea rcx, [rip + 0x58563c]
00A07504  E8 97 70 80 FF                  call 0x14020e5a0
00A07509  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00A0750D  33 FF                           xor edi, edi
00A0750F  48 85 C9                        test rcx, rcx
00A07512  75 1F                           jne 0x140a07533
00A07514  48 8D 0D 25 56 58 00            lea rcx, [rip + 0x585625]
00A0751B  89 7B 28                        mov dword ptr [rbx + 0x28], edi
00A0751E  48 89 7B 30                     mov qword ptr [rbx + 0x30], rdi
00A07522  E8 99 A4 84 FF                  call 0x1402519c0
00A07527  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A0752C  48 83 C4 20                     add rsp, 0x20
00A07530  5F                              pop rdi
00A07531  C3                              ret
00A07532  CC                              int3
00A07533  BA 50 6E 70 49                  mov edx, 0x49706e50
00A07538  E8 33 B3 17 00                  call 0x140b82870
00A0753D  EB D5                           jmp 0x140a07514
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpFreeDeviceInstancePath(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAcquireFastMutex(v_rip + 5789244, a2, a3, a4);
    v_rdi = 0;
    if (*(unsigned __int64 *)(a1 + 48) != 0) goto loc_00A07533;
loc_00A07514:
    *(unsigned int *)(a1 + 40) = 0;
    *(unsigned __int64 *)(a1 + 48) = 0;
    result = ExReleaseFastMutex(v_rip + 5789221, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A07533:
    result = ExFreePoolWithTag(v_rip + 5789221, (unsigned int)(0x49706E50ULL), a3, a4);
    goto loc_00A07514;
}
```

## 5. (Beta) C Style

```c
int64_t PnpFreeDeviceInstancePath(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAcquireFastMutex(v_rip + 5789244, a2, a3, a4);
    local_rdi = 0;
    if (*(uint64_t *)(arg1 + 0x30) != 0) goto loc_00A07533;
loc_00A07514:
    *(uint32_t *)(arg1 + 0x28) = 0;
    *(uint64_t *)(arg1 + 0x30) = 0;
    result = ExReleaseFastMutex(v_rip + 5789221, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A07533:
    result = ExFreePoolWithTag(v_rip + 5789221, (uint32_t)(0x49706E50ULL), a3, a4);
    goto loc_00A07514;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `32` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A074F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A074F0[BB_00A074F0]
  bb_00A07514[BB_00A07514]
  bb_00A07532[BB_00A07532]
  bb_00A07533[BB_00A07533]
  bb_00A074F0 -->|branch| bb_00A07533
  bb_00A074F0 -->|fallthrough| bb_00A07514
  bb_00A07532 -->|flow| bb_00A07533
  bb_00A07533 -->|branch| bb_00A07514
```
