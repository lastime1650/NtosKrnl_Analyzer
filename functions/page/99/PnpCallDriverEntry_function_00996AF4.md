# PnpCallDriverEntry

- RVA: `0x00996AF4`–`0x00996B6C` (길이 `120` bytes)
- VA: `0x0000000140996AF4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009928C`
- 디코드: `34`개 명령, `120/120` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00996B31` → [PnpEnableWatchdog](../8F/PnpEnableWatchdog_function_008FB5C8.md) (function, `0x008FB5C8`)
- `0x00996B43` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00996B65` → [PnpDisableWatchdog](../95/PnpDisableWatchdog_function_00955B00.md) (function, `0x00955B00`)

### Direct callers
- [IopLoadDriver](IopLoadDriver_function_00997B54.md) at `0x00998241`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00996B43` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00996AF4  4C 8B DC                        mov r11, rsp
00996AF7  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00996AFB  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00996AFF  57                              push rdi
00996B00  48 83 EC 40                     sub rsp, 0x40
00996B04  49 83 63 D8 00                  and qword ptr [r11 - 0x28], 0
00996B09  48 8B DA                        mov rbx, rdx
00996B0C  49 89 4B E0                     mov qword ptr [r11 - 0x20], rcx
00996B10  49 8D 53 D8                     lea rdx, [r11 - 0x28]
00996B14  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00996B1D  48 8B F9                        mov rdi, rcx
00996B20  4C 8B 41 30                     mov r8, qword ptr [rcx + 0x30]
00996B24  B9 05 00 00 00                  mov ecx, 5
00996B29  49 83 C0 18                     add r8, 0x18
00996B2D  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00996B31  E8 92 4A F6 FF                  call 0x1408fb5c8
00996B36  48 8B F0                        mov rsi, rax
00996B39  48 8B D3                        mov rdx, rbx
00996B3C  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00996B40  48 8B CF                        mov rcx, rdi
00996B43  E8 88 3F D2 FF                  call 0x1406baad0
00996B48  8B D8                           mov ebx, eax
00996B4A  48 85 F6                        test rsi, rsi
00996B4D  75 13                           jne 0x140996b62
00996B4F  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00996B54  8B C3                           mov eax, ebx
00996B56  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00996B5B  48 83 C4 40                     add rsp, 0x40
00996B5F  5F                              pop rdi
00996B60  C3                              ret
00996B61  CC                              int3
00996B62  48 8B CE                        mov rcx, rsi
00996B65  E8 96 EF FB FF                  call 0x140955b00
00996B6A  EB E3                           jmp 0x140996b4f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpCallDriverEntry(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 32) = a1;
    a3 = (*(unsigned __int64 *)(a1 + 48)) + (24);
    *(unsigned __int64 *)(v_rsp - 24) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = PnpEnableWatchdog(5, v_rsp - 40, a3, a4);
    result = guard_dispatch_icall(a1, a2, a3, a4);
    if (result != 0) goto loc_00996B62;
loc_00996B4F:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00996B62:
    result = PnpDisableWatchdog(v_stack_p10, a2, a3, a4);
    goto loc_00996B4F;
}
```

## 5. (Beta) C Style

```c
int64_t PnpCallDriverEntry(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(void **)(local_rsp - 0x20) = Arg1;
    a3 = (*(uint64_t *)(arg1 + 0x30)) + (24);
    *(uint64_t *)(local_rsp - 0x18) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = PnpEnableWatchdog(5, local_rsp - 40, a3, a4);
    result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    if (result != 0) goto loc_00996B62;
loc_00996B4F:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00996B62:
    result = PnpDisableWatchdog(v_stack_p10, Arg2, a3, a4);
    goto loc_00996B4F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00996AF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00996AF4[BB_00996AF4]
  bb_00996B4F[BB_00996B4F]
  bb_00996B61[BB_00996B61]
  bb_00996B62[BB_00996B62]
  bb_00996AF4 -->|branch| bb_00996B62
  bb_00996AF4 -->|fallthrough| bb_00996B4F
  bb_00996B61 -->|flow| bb_00996B62
  bb_00996B62 -->|branch| bb_00996B4F
```
