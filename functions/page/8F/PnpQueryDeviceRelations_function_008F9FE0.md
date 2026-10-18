# PnpQueryDeviceRelations

- RVA: `0x008F9FE0`–`0x008FA04B` (길이 `107` bytes)
- VA: `0x00000001408F9FE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007FA5C`
- 디코드: `29`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008FA00C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008FA02C` → [PnpSendIrp](../../text/27/PnpSendIrp_function_00271DF4.md) (function, `0x00271DF4`)

### Direct callers
- [PipEnumerateDevice](PipEnumerateDevice_function_008F99E4.md) at `0x008F9AA3`
- [PipEnumerateDevice](PipEnumerateDevice_function_008F99E4.md) at `0x008F9B12`
- [PnpProcessRelation](../A0/PnpProcessRelation_function_00A04A4C.md) at `0x00A04B2A`
- [PnpProcessRelation](../A0/PnpProcessRelation_function_00A04A4C.md) at `0x00A04B99`
- [PiQueryDeviceRelations](../A4/PiQueryDeviceRelations_function_00A4BE8C.md) at `0x00A4C115`
- [PiQueryPowerRelations](../AA/PiQueryPowerRelations_function_00AA3F9C.md) at `0x00AA3FED`
- [sub_00B266CA](../B2/Unknown_function_00B266CA.md) at `0x00B266F1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008FA00C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008FA02C` → [PnpSendIrp](../../text/27/PnpSendIrp_function_00271DF4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F9FE0  48 8B C4                        mov rax, rsp
008F9FE3  48 89 58 08                     mov qword ptr [rax + 8], rbx
008F9FE7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
008F9FEB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
008F9FEF  57                              push rdi
008F9FF0  48 81 EC 80 00 00 00            sub rsp, 0x80
008F9FF7  8B DA                           mov ebx, edx
008F9FF9  49 8B F0                        mov rsi, r8
008F9FFC  33 D2                           xor edx, edx
008F9FFE  48 8B E9                        mov rbp, rcx
008FA001  48 8D 48 A8                     lea rcx, [rax - 0x58]
008FA005  49 8B F9                        mov rdi, r9
008FA008  44 8D 42 48                     lea r8d, [rdx + 0x48]
008FA00C  E8 2F CC DC FF                  call 0x1406c6c40
008FA011  4C 8B CE                        mov r9, rsi
008FA014  66 C7 44 24 30 1B 07            mov word ptr [rsp + 0x30], 0x71b
008FA01B  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
008FA020  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
008FA024  48 8B CD                        mov rcx, rbp
008FA027  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008FA02C  E8 C3 7D 97 FF                  call 0x140271df4
008FA031  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
008FA039  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
008FA03D  49 8B 6B 18                     mov rbp, qword ptr [r11 + 0x18]
008FA041  49 8B 73 20                     mov rsi, qword ptr [r11 + 0x20]
008FA045  49 8B E3                        mov rsp, r11
008FA048  5F                              pop rdi
008FA049  C3                              ret
008FA04A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpQueryDeviceRelations(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m50;
    unsigned __int16 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (128);
    a2 = 0;
    result = memset(v_rsp - 88, a2, a2 + 72, a4);
    v_stack_m58 = 0x71BULL;
    v_stack_m50 = (unsigned int)((unsigned int)(a2));
    v_stack_m68 = a4;
    result = PnpSendIrp(a1, v_stack_m58, a2 + 72, a3);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpQueryDeviceRelations(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m50;
    uint16_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (128);
    Arg2 = 0;
    result = memset(local_rsp - 88, Arg2, Arg2 + 72, Arg4);
    v_stack_m58 = 0x71BULL;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m68 = Arg4;
    result = PnpSendIrp(Arg1, v_stack_m58, Arg2 + 72, Arg3);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F9FE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008F9FE0[BB_008F9FE0]
  bb_008FA04A[BB_008FA04A]
```
