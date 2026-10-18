# IopLogBlockedDriverEvent

- RVA: `0x0071BBFC`–`0x0071BC5D` (길이 `97` bytes)
- VA: `0x000000014071BBFC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `26`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0071BC0E` → [IoAllocateGenericErrorLogEntry](../../text/59/IoAllocateGenericErrorLogEntry_function_00597908.md) (function, `0x00597908`)
- `0x0071BC44` → [RtlStringCchCopyNW](../../text/47/RtlStringCchCopyNW_function_0047169C.md) (function, `0x0047169C`)
- `0x0071BC4C` → [IoWriteErrorLogEntry](../../text/4B/IoWriteErrorLogEntry_function_004B5B30.md) (function, `0x004B5B30`)

### Direct callers
- [IopLoadDriver](../99/IopLoadDriver_function_00997B54.md) at `0x00998463`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0071BC0E` → [IoAllocateGenericErrorLogEntry](../../text/59/IoAllocateGenericErrorLogEntry_function_00597908.md) (`PAGE` → `.text`)
  - `0x0071BC44` → [RtlStringCchCopyNW](../../text/47/RtlStringCchCopyNW_function_0047169C.md) (`PAGE` → `.text`)
  - `0x0071BC4C` → [IoWriteErrorLogEntry](../../text/4B/IoWriteErrorLogEntry_function_004B5B30.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0071BBFC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0071BC01  57                              push rdi
0071BC02  48 83 EC 20                     sub rsp, 0x20
0071BC06  48 8B F9                        mov rdi, rcx
0071BC09  41 8B D8                        mov ebx, r8d
0071BC0C  B1 B0                           mov cl, 0xb0
0071BC0E  E8 F5 BC E7 FF                  call 0x140597908
0071BC13  4C 8B D8                        mov r11, rax
0071BC16  48 85 C0                        test rax, rax
0071BC19  74 36                           je 0x14071bc51
0071BC1B  41 B9 3F 00 00 00               mov r9d, 0x3f
0071BC21  C7 40 02 00 00 01 00            mov dword ptr [rax + 2], 0x10000
0071BC28  66 C7 40 06 30 00               mov word ptr [rax + 6], 0x30
0071BC2E  48 8D 48 30                     lea rcx, [rax + 0x30]
0071BC32  C7 40 0C 24 04 00 C0            mov dword ptr [rax + 0xc], 0xc0000424
0071BC39  89 58 14                        mov dword ptr [rax + 0x14], ebx
0071BC3C  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
0071BC40  41 8D 51 01                     lea edx, [r9 + 1]
0071BC44  E8 53 5A D5 FF                  call 0x14047169c
0071BC49  49 8B CB                        mov rcx, r11
0071BC4C  E8 DF 9E D9 FF                  call 0x1404b5b30
0071BC51  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0071BC56  48 83 C4 20                     add rsp, 0x20
0071BC5A  5F                              pop rdi
0071BC5B  C3                              ret
0071BC5C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopLogBlockedDriverEvent(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = IoAllocateGenericErrorLogEntry(176, a2, a3, a4);
    if (result != 0) {
        a4 = 63;
        *(unsigned int *)(result + 2) = 0x10000ULL;
        *(unsigned __int16 *)(result + 6) = 48;
        a1 = result + 48;
        *(unsigned int *)(result + 12) = 0xC0000424ULL;
        *(unsigned int *)(result + 20) = (unsigned int)((unsigned int)(a3));
        a3 = *(unsigned __int64 *)(a1 + 8);
        a2 = a4 + 1;
        result = RtlStringCchCopyNW(a1, a2, a3, a4);
        a1 = result;
        result = IoWriteErrorLogEntry(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopLogBlockedDriverEvent(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = IoAllocateGenericErrorLogEntry(176, Arg2, Arg3, a4);
    if (result != 0) {
        a4 = 63;
        *(uint32_t *)(result + 0x2) = 0x10000ULL;
        *(uint16_t *)(result + 0x6) = 48;
        Arg1 = result + 48;
        *(uint32_t *)(result + 0xC) = 0xC0000424ULL;
        *(uint32_t *)(result + 0x14) = (uint32_t)((uint32_t)(Arg3));
        Arg3 = *(uint64_t *)(arg1 + 0x8);
        Arg2 = a4 + 1;
        result = RtlStringCchCopyNW(Arg1, Arg2, Arg3, a4);
        Arg1 = result;
        result = IoWriteErrorLogEntry(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0071BBFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0071BBFC[BB_0071BBFC]
  bb_0071BC1B[BB_0071BC1B]
  bb_0071BC51[BB_0071BC51]
  bb_0071BC5C[BB_0071BC5C]
  bb_0071BBFC -->|branch| bb_0071BC51
  bb_0071BBFC -->|fallthrough| bb_0071BC1B
  bb_0071BC1B -->|flow| bb_0071BC51
```
