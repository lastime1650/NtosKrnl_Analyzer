# PnpStartDevice

- RVA: `0x00499E60`–`0x00499F06` (길이 `166` bytes)
- VA: `0x0000000140499E60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BBA4`
- 디코드: `40`개 명령, `166/166` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00499E95` → [PoFxPrepareDevice](PoFxPrepareDevice_function_00499F0C.md) (function, `0x00499F0C`)
- `0x00499EAF` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00499EE3` → [PnpSendIrp](../27/PnpSendIrp_function_00271DF4.md) (function, `0x00271DF4`)

### Direct callers
- [PnpStartDeviceNode](../../page/8F/PnpStartDeviceNode_function_008FE38C.md) at `0x008FE451`
- [PnpStartDeviceNode](../../page/8F/PnpStartDeviceNode_function_008FE38C.md) at `0x008FE540`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00499E60  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00499E65  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00499E6A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00499E6F  57                              push rdi
00499E70  48 81 EC 80 00 00 00            sub rsp, 0x80
00499E77  49 8B F0                        mov rsi, r8
00499E7A  48 8B EA                        mov rbp, rdx
00499E7D  48 8B D9                        mov rbx, rcx
00499E80  48 85 C9                        test rcx, rcx
00499E83  74 7D                           je 0x140499f02
00499E85  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00499E8C  48 8B 78 28                     mov rdi, qword ptr [rax + 0x28]
00499E90  B2 01                           mov dl, 1
00499E92  48 8B CF                        mov rcx, rdi
00499E95  E8 72 00 00 00                  call 0x140499f0c
00499E9A  33 D2                           xor edx, edx
00499E9C  C7 87 9C 00 00 00 01 00 00 00   mov dword ptr [rdi + 0x9c], 1
00499EA6  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00499EAB  44 8D 42 48                     lea r8d, [rdx + 0x48]
00499EAF  E8 8C CD 22 00                  call 0x1406c6c40
00499EB4  48 8B 87 A0 01 00 00            mov rax, qword ptr [rdi + 0x1a0]
00499EBB  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00499EC0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00499EC5  4C 8B CD                        mov r9, rbp
00499EC8  48 8B 87 A8 01 00 00            mov rax, qword ptr [rdi + 0x1a8]
00499ECF  48 8B CB                        mov rcx, rbx
00499ED2  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00499ED7  66 C7 44 24 30 1B 00            mov word ptr [rsp + 0x30], 0x1b
00499EDE  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00499EE3  E8 0C 7F DD FF                  call 0x140271df4
00499EE8  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
00499EF0  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00499EF4  49 8B 6B 18                     mov rbp, qword ptr [r11 + 0x18]
00499EF8  49 8B 73 20                     mov rsi, qword ptr [r11 + 0x20]
00499EFC  49 8B E3                        mov rsp, r11
00499EFF  5F                              pop rdi
00499F00  C3                              ret
00499F01  CC                              int3
00499F02  33 FF                           xor edi, edi
00499F04  EB 8A                           jmp 0x140499e90
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpStartDevice(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (128);
    if (a1 == 0) goto loc_00499F02;
loc_00499E90:
    result = PoFxPrepareDevice(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 40), 1, a3, a4);
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 40) + 156) = 1;
    result = memset(v_stack_m58, a2, a2 + 72, a4);
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 40) + 416);
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 40) + 424);
    v_stack_m58 = 27;
    v_stack_m68 = a3;
    result = PnpSendIrp(a1, v_stack_m58, a2 + 72, 0);
    return result;
loc_00499F02:
    v_rdi = 0;
    goto loc_00499E90;
}
```

## 5. (Beta) C Style

```c
int64_t PnpStartDevice(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (128);
    if (Arg1 == 0) goto loc_00499F02;
loc_00499E90:
    result = PoFxPrepareDevice(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x138) + 0x28), 1, Arg3, a4);
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x138) + 0x28) + 0x9C) = 1;
    result = memset(v_stack_m58, Arg2, Arg2 + 72, a4);
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x138) + 0x28) + 0x1A0);
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x138) + 0x28) + 0x1A8);
    v_stack_m58 = 27;
    v_stack_m68 = Arg3;
    result = PnpSendIrp(Arg1, v_stack_m58, Arg2 + 72, 0);
    return result;
loc_00499F02:
    local_rdi = 0;
    goto loc_00499E90;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00499E60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00499E60[BB_00499E60]
  bb_00499E85[BB_00499E85]
  bb_00499E90[BB_00499E90]
  bb_00499F01[BB_00499F01]
  bb_00499F02[BB_00499F02]
  bb_00499E60 -->|branch| bb_00499F02
  bb_00499E60 -->|fallthrough| bb_00499E85
  bb_00499E85 -->|flow| bb_00499E90
  bb_00499F01 -->|flow| bb_00499F02
  bb_00499F02 -->|branch| bb_00499E90
```
