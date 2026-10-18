# TtmpStopCallout

- RVA: `0x00776C24`–`0x00776CE5` (길이 `193` bytes)
- VA: `0x0000000140776C24`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AAF70`
- 디코드: `47`개 명령, `193/193` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00776C64` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00776C98` → [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) (function, `0x00955D80`)
- `0x00776CA4` → [TtmpGetCalloutTagFromCalloutType](TtmpGetCalloutTagFromCalloutType_function_007765A0.md) (function, `0x007765A0`)
- `0x00776CC1` → [TtmiLogCalloutStop](TtmiLogCalloutStop_function_00779014.md) (function, `0x00779014`)
- `0x00776CC6` → [TtmpAcquireSessionLock](../70/TtmpAcquireSessionLock_function_00700408.md) (function, `0x00700408`)

### Direct callers
- [TtmiSessionDeviceListWorker](TtmiSessionDeviceListWorker_function_00775CA0.md) at `0x00775DEB`
- [TtmpCallAssignedToTerminal](TtmpCallAssignedToTerminal_function_00775F70.md) at `0x00775FD8`
- [TtmpCallSetBuiltinPanelState](TtmpCallSetBuiltinPanelState_function_0077600C.md) at `0x00776072`
- [TtmpCallSetDisplayState](TtmpCallSetDisplayState_function_0077608C.md) at `0x007760FC`
- [TtmpCallSetInputMode](TtmpCallSetInputMode_function_0077613C.md) at `0x007761A1`
- [TtmpUpdatePrimaryDisplayWnf](TtmpUpdatePrimaryDisplayWnf_function_00776CEC.md) at `0x00776D6C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00776C64` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00776C24  4C 8B DC                        mov r11, rsp
00776C27  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00776C2B  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00776C2F  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00776C33  57                              push rdi
00776C34  48 81 EC 90 00 00 00            sub rsp, 0x90
00776C3B  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
00776C45  8B EA                           mov ebp, edx
00776C47  48 8B 71 18                     mov rsi, qword ptr [rcx + 0x18]
00776C4B  48 8B F8                        mov rdi, rax
00776C4E  48 2B 79 20                     sub rdi, qword ptr [rcx + 0x20]
00776C52  48 8B D9                        mov rbx, rcx
00776C55  48 85 F6                        test rsi, rsi
00776C58  74 43                           je 0x140776c9d
00776C5A  33 D2                           xor edx, edx
00776C5C  49 8D 4B 98                     lea rcx, [r11 - 0x68]
00776C60  44 8D 42 60                     lea r8d, [rdx + 0x60]
00776C64  E8 D7 FF F4 FF                  call 0x1406c6c40
00776C69  48 83 63 18 00                  and qword ptr [rbx + 0x18], 0
00776C6E  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00776C73  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00776C78  45 33 C9                        xor r9d, r9d
00776C7B  C7 44 24 30 15 00 00 00         mov dword ptr [rsp + 0x30], 0x15
00776C83  C6 84 24 88 00 00 00 01         mov byte ptr [rsp + 0x88], 1
00776C8B  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00776C90  45 8D 41 60                     lea r8d, [r9 + 0x60]
00776C94  41 8D 49 57                     lea ecx, [r9 + 0x57]
00776C98  E8 E3 F0 1D 00                  call 0x140955d80
00776C9D  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00776CA0  4C 8B 53 08                     mov r10, qword ptr [rbx + 8]
00776CA4  E8 F7 F8 FF FF                  call 0x1407765a0
00776CA9  41 8B 4A 10                     mov ecx, dword ptr [r10 + 0x10]
00776CAD  44 8B C8                        mov r9d, eax
00776CB0  4D 8B 42 18                     mov r8, qword ptr [r10 + 0x18]
00776CB4  41 8B 52 48                     mov edx, dword ptr [r10 + 0x48]
00776CB8  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00776CBD  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
00776CC1  E8 4E 23 00 00                  call 0x140779014
00776CC6  E8 3D 97 F8 FF                  call 0x140700408
00776CCB  4C 8D 9C 24 90 00 00 00         lea r11, [rsp + 0x90]
00776CD3  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00776CD7  49 8B 6B 18                     mov rbp, qword ptr [r11 + 0x18]
00776CDB  49 8B 73 20                     mov rsi, qword ptr [r11 + 0x20]
00776CDF  49 8B E3                        mov rsp, r11
00776CE2  5F                              pop rdi
00776CE3  C3                              ret
00776CE4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmpStopCallout(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m10;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (144);
    v_rdi = (result) - (*(unsigned __int64 *)(a1 + 32));
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        a2 = 0;
        a1 = v_rsp - 104;
        a3 = a2 + 96;
        result = memset(a1, a2, a3, a4);
        a2 = v_stack_m68;
        a4 = 0;
        v_stack_m68 = 21;
        v_stack_m10 = 1;
        v_stack_m60 = *(unsigned __int64 *)(a1 + 24);
        a3 = a4 + 96;
        a1 = a4 + 87;
        result = NtPowerInformation(a1, a2, a3, a4);
    }
    result = TtmpGetCalloutTagFromCalloutType((unsigned int)(*(unsigned int *)(a1 + 16)), a2, a3, a4);
    v_stack_m70 = v_rdi;
    v_stack_m78 = (unsigned int)((unsigned int)(a2));
    result = TtmiLogCalloutStop((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 16)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24), (unsigned int)((unsigned int)(result)));
    result = TtmpAcquireSessionLock((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 16)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 24), (unsigned int)((unsigned int)(result)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmpStopCallout(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint8_t v_stack_m10;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (144);
    local_rdi = (result) - (*(uint64_t *)(arg1 + 0x20));
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        Arg2 = 0;
        Arg1 = local_rsp - 104;
        Arg3 = Arg2 + 96;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_stack_m68;
        Arg4 = 0;
        v_stack_m68 = 21;
        v_stack_m10 = 1;
        v_stack_m60 = *(uint64_t *)(arg1 + 0x18);
        Arg3 = Arg4 + 96;
        Arg1 = Arg4 + 87;
        result = NtPowerInformation(Arg1, Arg2, Arg3, Arg4);
    }
    result = TtmpGetCalloutTagFromCalloutType((uint32_t)(*(uint32_t *)(arg1 + 0x10)), Arg2, Arg3, Arg4);
    v_stack_m70 = local_rdi;
    v_stack_m78 = (uint32_t)((uint32_t)(Arg2));
    result = TtmiLogCalloutStop((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x48)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18), (uint32_t)((uint32_t)(result)));
    result = TtmpAcquireSessionLock((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x48)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18), (uint32_t)((uint32_t)(result)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00776C24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00776C24[BB_00776C24]
  bb_00776C5A[BB_00776C5A]
  bb_00776C9D[BB_00776C9D]
  bb_00776CE4[BB_00776CE4]
  bb_00776C24 -->|branch| bb_00776C9D
  bb_00776C24 -->|fallthrough| bb_00776C5A
  bb_00776C5A -->|flow| bb_00776C9D
```
