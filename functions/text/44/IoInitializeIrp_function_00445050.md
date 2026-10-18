# IoInitializeIrp

- RVA: `0x00445050`–`0x004450E3` (길이 `147` bytes)
- VA: `0x0000000140445050`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065C48`
- 디코드: `38`개 명령, `147/147` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0044507B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004450DC` → [IovInitializeIrp](../../pagevrfy/BB/IovInitializeIrp_function_00BB9418.md) (function, `0x00BB9418`)

### Direct callers
- [IopAllocateReserveIrp](../29/IopAllocateReserveIrp_function_0029C218.md) at `0x0029C2F4`
- [IopAllocateReserveIrp](../29/IopAllocateReserveIrp_function_0029C218.md) at `0x0029C397`
- [IopAllocateReserveIrp](../29/IopAllocateReserveIrp_function_0029C218.md) at `0x0029C414`
- [IopAllocateBackpocketIrp](../59/IopAllocateBackpocketIrp_function_00596CE0.md) at `0x00596D96`
- [IopAllocateBackpocketIrp](../59/IopAllocateBackpocketIrp_function_00596CE0.md) at `0x00596E00`
- [IopAllocateBackpocketIrp](../59/IopAllocateBackpocketIrp_function_00596CE0.md) at `0x00596EC3`
- [IopAllocateBackpocketIrp](../59/IopAllocateBackpocketIrp_function_00596CE0.md) at `0x00596F14`
- [SmStorePhysicalRequestIssue](../../page/7A/SmStorePhysicalRequestIssue_function_007A732C.md) at `0x007A73C6`
- [WmipSendWmiIrpToTraceDeviceList](../../page/9E/WmipSendWmiIrpToTraceDeviceList_function_009E2988.md) at `0x009E2A30`
- [ViIrpAllocateLockedPacket](../../pagevrfy/B9/ViIrpAllocateLockedPacket_function_00B9E0AC.md) at `0x00B9E18D`

### Static image references
- `0x0044505F` → RVA `0x00F04A20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004450DC` → [IovInitializeIrp](../../pagevrfy/BB/IovInitializeIrp_function_00BB9418.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00445050  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00445055  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0044505A  57                              push rdi
0044505B  48 83 EC 20                     sub rsp, 0x20
0044505F  8B 05 BB F9 AB 00               mov eax, dword ptr [rip + 0xabf9bb]
00445065  48 8B D9                        mov rbx, rcx
00445068  49 0F BE F8                     movsx rdi, r8b
0044506C  0F B7 F2                        movzx esi, dx
0044506F  A8 10                           test al, 0x10
00445071  75 64                           jne 0x1404450d7
00445073  4C 8B C6                        mov r8, rsi
00445076  33 D2                           xor edx, edx
00445078  48 8B CB                        mov rcx, rbx
0044507B  E8 C0 1B 28 00                  call 0x1406c6c40
00445080  66 89 73 02                     mov word ptr [rbx + 2], si
00445084  8D 47 01                        lea eax, [rdi + 1]
00445087  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0044508C  88 43 43                        mov byte ptr [rbx + 0x43], al
0044508F  66 C7 03 06 00                  mov word ptr [rbx], 6
00445094  40 88 7B 42                     mov byte ptr [rbx + 0x42], dil
00445098  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004450A1  8A 88 4A 02 00 00               mov cl, byte ptr [rax + 0x24a]
004450A7  48 8D 43 20                     lea rax, [rbx + 0x20]
004450AB  88 4B 46                        mov byte ptr [rbx + 0x46], cl
004450AE  48 89 40 08                     mov qword ptr [rax + 8], rax
004450B2  48 89 00                        mov qword ptr [rax], rax
004450B5  48 8D 04 FD 1A 00 00 00         lea rax, [rdi*8 + 0x1a]
004450BD  48 03 C7                        add rax, rdi
004450C0  48 8D 04 C3                     lea rax, [rbx + rax*8]
004450C4  48 89 83 B8 00 00 00            mov qword ptr [rbx + 0xb8], rax
004450CB  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004450D0  48 83 C4 20                     add rsp, 0x20
004450D4  5F                              pop rdi
004450D5  C3                              ret
004450D6  CC                              int3
004450D7  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
004450DC  E8 37 43 77 00                  call 0x140bb9418
004450E1  EB 90                           jmp 0x140445073
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoInitializeIrp(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11270587)))) & (16)) != 0) goto loc_004450D7;
loc_00445073:
    a2 = 0;
    result = memset(a1, a2, (unsigned __int16)(a2), a4);
    *(unsigned __int16 *)(a1 + 2) = (unsigned __int16)((unsigned __int16)(a2));
    *(unsigned __int8 *)(a1 + 67) = (unsigned __int8)((__int8)(a3) + 1);
    *(unsigned __int16 *)(a1) = 6;
    *(unsigned __int8 *)(a1 + 66) = (unsigned __int8)((__int8)(a3));
    *(unsigned __int8 *)(a1 + 70) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586));
    *(unsigned __int64 *)(a1 + 32 + 8) = a1 + 32;
    *(unsigned __int64 *)(a1 + 32) = a1 + 32;
    result = ((__int8)(a3) * 8 + 26) + ((__int8)(a3));
    *(unsigned __int64 *)(a1 + 184) = a1 + result * 8;
    v_rsp = (v_rsp) + (32);
    return a1 + result * 8;
loc_004450D7:
    result = IovInitializeIrp(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586), a2, (unsigned __int16)(a2), v_stack_p28);
    goto loc_00445073;
}
```

## 5. (Beta) C Style

```c
int64_t IoInitializeIrp(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xABF9BB)))) & (16)) != 0) goto loc_004450D7;
loc_00445073:
    Arg2 = 0;
    result = memset(Arg1, Arg2, (uint16_t)(Arg2), a4);
    *(uint16_t *)(arg1 + 0x2) = (uint16_t)((uint16_t)(Arg2));
    *(uint8_t *)(arg1 + 0x43) = (uint8_t)((int8_t)(Arg3) + 1);
    *(uint16_t *)(arg1) = 6;
    *(uint8_t *)(arg1 + 0x42) = (uint8_t)((int8_t)(Arg3));
    *(uint8_t *)(arg1 + 0x46) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A));
    *(void **)(arg1 + 0x20 + 0x8) = Arg1 + 32;
    *(void **)(arg1 + 0x20) = Arg1 + 32;
    result = ((int8_t)(Arg3) * 8 + 26) + ((int8_t)(Arg3));
    *(void **)(arg1 + 0xB8) = Arg1 + result * 8;
    local_rsp = (local_rsp) + (32);
    return Arg1 + result * 8;
loc_004450D7:
    result = IovInitializeIrp(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A), Arg2, (uint16_t)(Arg2), v_stack_p28);
    goto loc_00445073;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x2` | `16` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x42` | `8` | `W` |
| `Arg1` | `+ 0x43` | `8` | `W` |
| `Arg1` | `+ 0x46` | `8` | `W` |
| `Arg1` | `+ 0xB8` | `64` | `W` |
| `Arg3` | `+ 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00445050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00445050[BB_00445050]
  bb_00445073[BB_00445073]
  bb_004450D6[BB_004450D6]
  bb_004450D7[BB_004450D7]
  bb_00445050 -->|branch| bb_004450D7
  bb_00445050 -->|fallthrough| bb_00445073
  bb_004450D6 -->|flow| bb_004450D7
  bb_004450D7 -->|branch| bb_00445073
```
