# PopDiagTraceDisplayBurstWin32kCallout

- RVA: `0x00AC1CF8`–`0x00AC1DA3` (길이 `171` bytes)
- VA: `0x0000000140AC1CF8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EA9C`
- 디코드: `37`개 명령, `171/171` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00AC1D88` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AC1D94` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00957933`

### Static image references
- `0x00AC1D06` → RVA `0x00E0A740` (`.data`; read)
- `0x00AC1D14` → RVA `0x00E07748` (`.data`; read)
- `0x00AC1D1B` → RVA `0x00E67A54` (`.data`; read)
- `0x00AC1D21` → RVA `0x00E0B579` (`.data`; read)
- `0x00AC1D2C` → RVA `0x00049469` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AC1D88` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AC1D94` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC1CF8  40 55                           push rbp
00AC1CFA  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00AC1CFF  48 81 EC A0 00 00 00            sub rsp, 0xa0
00AC1D06  48 8B 05 33 8A 34 00            mov rax, qword ptr [rip + 0x348a33]
00AC1D0D  48 33 C4                        xor rax, rsp
00AC1D10  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00AC1D14  83 3D 2D 5A 34 00 05            cmp dword ptr [rip + 0x345a2d], 5
00AC1D1B  8A 05 33 5D 3A 00               mov al, byte ptr [rip + 0x3a5d33]
00AC1D21  8A 0D 52 98 34 00               mov cl, byte ptr [rip + 0x349852]
00AC1D27  76 64                           jbe 0x140ac1d8d
00AC1D29  88 45 E8                        mov byte ptr [rbp - 0x18], al
00AC1D2C  48 8D 15 36 77 58 FF            lea rdx, [rip - 0xa788ca]
00AC1D33  88 4D E7                        mov byte ptr [rbp - 0x19], cl
00AC1D36  48 8D 45 E8                     lea rax, [rbp - 0x18]
00AC1D3A  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00AC1D3E  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00AC1D42  48 8D 45 E9                     lea rax, [rbp - 0x17]
00AC1D46  48 89 4D 17                     mov qword ptr [rbp + 0x17], rcx
00AC1D4A  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00AC1D4E  48 8D 0D F3 59 34 00            lea rcx, [rip + 0x3459f3]
00AC1D55  48 8D 45 F7                     lea rax, [rbp - 9]
00AC1D59  44 88 45 E9                     mov byte ptr [rbp - 0x17], r8b
00AC1D5D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC1D62  45 33 C9                        xor r9d, r9d
00AC1D65  45 33 C0                        xor r8d, r8d
00AC1D68  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
00AC1D70  48 C7 45 1F 01 00 00 00         mov qword ptr [rbp + 0x1f], 1
00AC1D78  48 C7 45 2F 01 00 00 00         mov qword ptr [rbp + 0x2f], 1
00AC1D80  48 C7 45 3F 01 00 00 00         mov qword ptr [rbp + 0x3f], 1
00AC1D88  E8 53 43 96 FF                  call 0x1404260e0
00AC1D8D  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00AC1D91  48 33 CC                        xor rcx, rsp
00AC1D94  E8 A7 A8 BE FF                  call 0x1406ac640
00AC1D99  48 81 C4 A0 00 00 00            add rsp, 0xa0
00AC1DA0  5D                              pop rbp
00AC1DA1  C3                              ret
00AC1DA2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceDisplayBurstWin32kCallout(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m76;
    unsigned __int8 v_stack_m77;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 3443251)) ^ (v_rsp);
    v_stack_m18 = result;
    result = *(unsigned __int8 *)(v_rip + 3824947);
    if ((*(unsigned int *)(v_rip + 3430957)) >= = 5) {
        v_stack_m77 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 3824947));
        a2 = v_rip - 10979530;
        v_stack_m78 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 3446866));
        result = v_stack_m77;
        v_stack_m38 = result;
        a1 = v_stack_m78;
        result = v_stack_m76;
        v_stack_m48 = a1;
        v_stack_m28 = result;
        a1 = v_rip + 3430899;
        result = v_stack_m68;
        v_stack_m76 = (unsigned __int8)(a3);
        v_stack_m80 = result;
        a4 = 0;
        a3 = 0;
        v_stack_m88 = 5;
        v_stack_m40 = 1;
        v_stack_m30 = 1;
        v_stack_m20 = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceDisplayBurstWin32kCallout(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint64_t v_stack_m76;
    uint8_t v_stack_m77;
    uint8_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x348A33)) ^ (local_rsp);
    v_stack_m18 = result;
    result = *(uint8_t *)(v_rip + 0x3A5D33);
    if ((*(uint32_t *)(v_rip + 0x345A2D)) >= = 5) {
        v_stack_m77 = (uint8_t)(*(uint8_t *)(v_rip + 0x3A5D33));
        Arg2 = v_rip - 10979530;
        v_stack_m78 = (uint8_t)(*(uint8_t *)(v_rip + 0x349852));
        result = v_stack_m77;
        v_stack_m38 = result;
        Arg1 = v_stack_m78;
        result = v_stack_m76;
        v_stack_m48 = Arg1;
        v_stack_m28 = result;
        Arg1 = v_rip + 3430899;
        result = v_stack_m68;
        v_stack_m76 = (uint8_t)(Arg3);
        v_stack_m80 = result;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_m88 = 5;
        v_stack_m40 = 1;
        v_stack_m30 = 1;
        v_stack_m20 = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC1CF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AC1CF8[BB_00AC1CF8]
  bb_00AC1D29[BB_00AC1D29]
  bb_00AC1D8D[BB_00AC1D8D]
  bb_00AC1DA2[BB_00AC1DA2]
  bb_00AC1CF8 -->|branch| bb_00AC1D8D
  bb_00AC1CF8 -->|fallthrough| bb_00AC1D29
  bb_00AC1D29 -->|flow| bb_00AC1D8D
```
