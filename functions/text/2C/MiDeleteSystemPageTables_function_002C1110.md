# MiDeleteSystemPageTables

- RVA: `0x002C1110`–`0x002C11FA` (길이 `234` bytes)
- VA: `0x00000001402C1110`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E6A4`
- 디코드: `59`개 명령, `234/234` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002C115B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002C11B1` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C11BF` → [MiWalkPageTables](MiWalkPageTables_function_002C2710.md) (function, `0x002C2710`)
- `0x002C11CB` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002C11F3` → [MiLockWorkingSetSharedAtDpc](../23/MiLockWorkingSetSharedAtDpc_function_00239574.md) (function, `0x00239574`)

### Direct callers
- [MiDecommitSystemPageTables](MiDecommitSystemPageTables_function_002C1054.md) at `0x002C10E6`
- [MiMakeZeroedPageTablesEx](../3B/MiMakeZeroedPageTablesEx_function_003B59FC.md) at `0x003B5E29`

### Static image references
- `0x002C1171` → RVA `0x004916B0` (`MiDeleteSystemPageTable`; read)
- `0x002C117C` → RVA `0x00367830` (`MiDeleteSystemPageTableTail`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C1110  48 8B C4                        mov rax, rsp
002C1113  48 89 58 08                     mov qword ptr [rax + 8], rbx
002C1117  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
002C111B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
002C111F  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
002C1123  55                              push rbp
002C1124  48 8D 68 E8                     lea rbp, [rax - 0x18]
002C1128  48 81 EC 10 01 00 00            sub rsp, 0x110
002C112F  0F 57 C0                        xorps xmm0, xmm0
002C1132  49 8B F8                        mov rdi, r8
002C1135  8B DA                           mov ebx, edx
002C1137  4C 8B F1                        mov r14, rcx
002C113A  33 C0                           xor eax, eax
002C113C  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002C1141  33 D2                           xor edx, edx
002C1143  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002C1148  41 B8 C0 00 00 00               mov r8d, 0xc0
002C114E  49 8B F1                        mov rsi, r9
002C1151  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
002C1156  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
002C115B  E8 E0 5A 40 00                  call 0x1406c6c40
002C1160  8B 45 40                        mov eax, dword ptr [rbp + 0x40]
002C1163  83 E0 07                        and eax, 7
002C1166  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
002C116A  C1 E0 06                        shl eax, 6
002C116D  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
002C1171  48 8D 05 38 05 1D 00            lea rax, [rip + 0x1d0538]
002C1178  48 89 45 F8                     mov qword ptr [rbp - 8], rax
002C117C  48 8D 05 AD 66 0A 00            lea rax, [rip + 0xa66ad]
002C1183  48 89 45 00                     mov qword ptr [rbp], rax
002C1187  48 8D 44 24 20                  lea rax, [rsp + 0x20]
002C118C  48 89 45 08                     mov qword ptr [rbp + 8], rax
002C1190  C7 44 24 50 07 20 00 00         mov dword ptr [rsp + 0x50], 0x2007
002C1198  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
002C119D  48 89 75 80                     mov qword ptr [rbp - 0x80], rsi
002C11A1  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
002C11A6  44 0F 20 C0                     mov rax, cr8
002C11AA  49 8B CE                        mov rcx, r14
002C11AD  3C 02                           cmp al, 2
002C11AF  74 3D                           je 0x1402c11ee
002C11B1  E8 3A BA FB FF                  call 0x14027cbf0
002C11B6  88 44 24 59                     mov byte ptr [rsp + 0x59], al
002C11BA  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002C11BF  E8 4C 15 00 00                  call 0x1402c2710
002C11C4  8A 54 24 59                     mov dl, byte ptr [rsp + 0x59]
002C11C8  49 8B CE                        mov rcx, r14
002C11CB  E8 C0 C4 FB FF                  call 0x14027d690
002C11D0  4C 8D 9C 24 10 01 00 00         lea r11, [rsp + 0x110]
002C11D8  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
002C11DC  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
002C11E0  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
002C11E4  4D 8B 73 28                     mov r14, qword ptr [r11 + 0x28]
002C11E8  49 8B E3                        mov rsp, r11
002C11EB  5D                              pop rbp
002C11EC  C3                              ret
002C11ED  CC                              int3
002C11EE  C6 44 24 59 11                  mov byte ptr [rsp + 0x59], 0x11
002C11F3  E8 7C 83 F7 FF                  call 0x140239574
002C11F8  EB C0                           jmp 0x1402c11ba
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeleteSystemPageTables(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int8 v_stack_mB7;
    unsigned __int8 v_stack_mBF;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (272);
    result = 0;
    a2 = 0;
    v_stack_mD8 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm0;
    result = memset(v_stack_mC8, a2, 192, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 24 + 64))) & (7));
    v_stack_mF8 = (unsigned int)((unsigned int)(a2));
    result = (unsigned int)((result) << (6));
    v_stack_mC4 = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 24 - 8) = v_rip + 1901880;
    *(unsigned __int64 *)(v_rsp - 24) = v_rip + 681645;
    *(unsigned __int64 *)(v_rsp - 24 + 8) = v_stack_mF8;
    v_stack_mC8 = 0x2007ULL;
    v_stack_mA0 = a3;
    *(unsigned __int64 *)(v_rsp - 24 - 128) = a4;
    v_stack_mA8 = a1;
    if (((unsigned __int8)(v_cr8)) == 2) goto loc_002C11EE;
    result = MiLockWorkingSetShared(a1, a2, 192, a4);
    v_stack_mBF = (unsigned __int8)(result);
loc_002C11BA:
    result = MiWalkPageTables(v_stack_mC8, a2, 192, a4);
    result = MiUnlockWorkingSetShared(a1, v_stack_mBF, 192, a4);
    return result;
loc_002C11EE:
    v_stack_mB7 = 17;
    result = MiLockWorkingSetSharedAtDpc(a1, v_stack_mBF, 192, a4);
    goto loc_002C11BA;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeleteSystemPageTables(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint8_t v_stack_mB7;
    uint8_t v_stack_mBF;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (272);
    result = 0;
    Arg2 = 0;
    v_stack_mD8 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm0;
    result = memset(v_stack_mC8, Arg2, 192, Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x18 + 0x40))) & (7));
    v_stack_mF8 = (uint32_t)((uint32_t)(Arg2));
    result = (uint32_t)((result) << (6));
    v_stack_mC4 = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0x18 - 0x8) = v_rip + 1901880;
    *(uint64_t *)(local_rsp - 0x18) = v_rip + 681645;
    *(uint64_t *)(local_rsp - 0x18 + 0x8) = v_stack_mF8;
    v_stack_mC8 = 0x2007ULL;
    v_stack_mA0 = Arg3;
    *(uint64_t *)(local_rsp - 0x18 - 0x80) = Arg4;
    v_stack_mA8 = Arg1;
    if (((uint8_t)(v_cr8)) == 2) goto loc_002C11EE;
    result = MiLockWorkingSetShared(Arg1, Arg2, 192, Arg4);
    v_stack_mBF = (uint8_t)(result);
loc_002C11BA:
    result = MiWalkPageTables(v_stack_mC8, Arg2, 192, Arg4);
    result = MiUnlockWorkingSetShared(Arg1, v_stack_mBF, 192, Arg4);
    return result;
loc_002C11EE:
    v_stack_mB7 = 17;
    result = MiLockWorkingSetSharedAtDpc(Arg1, v_stack_mBF, 192, Arg4);
    goto loc_002C11BA;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C1110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C1110[BB_002C1110]
  bb_002C11B1[BB_002C11B1]
  bb_002C11BA[BB_002C11BA]
  bb_002C11ED[BB_002C11ED]
  bb_002C11EE[BB_002C11EE]
  bb_002C1110 -->|branch| bb_002C11EE
  bb_002C1110 -->|fallthrough| bb_002C11B1
  bb_002C11B1 -->|flow| bb_002C11BA
  bb_002C11ED -->|flow| bb_002C11EE
  bb_002C11EE -->|branch| bb_002C11BA
```
