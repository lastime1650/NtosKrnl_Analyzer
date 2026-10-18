# McTemplateK0qqzqqjqzjztx_EtwWriteTransfer

- RVA: `0x005A7548`–`0x005A76FF` (길이 `439` bytes)
- VA: `0x00000001405A7548`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C87DC`
- 디코드: `101`개 명령, `439/439` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005A76DA` → [McGenEventWrite_EtwWriteTransfer](../42/McGenEventWrite_EtwWriteTransfer_function_00424FC8.md) (function, `0x00424FC8`)
- `0x005A76E6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiUEventMovePendingEventToSynchronousQueue](../../page/70/PiUEventMovePendingEventToSynchronousQueue_function_00700798.md) at `0x007008D0`
- [sub_00B1D4A4](../../page/B1/Unknown_function_00B1D4A4.md) at `0x00B1D53B`

### Static image references
- `0x005A7561` → RVA `0x00E0A740` (`.data`; read)
- `0x005A75D4` → RVA `0x006CB080` (` ?? ::FNODOBFM::`string'`; read)
- `0x005A769F` → RVA `0x00E06DA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005A7548  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005A754D  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
005A7552  55                              push rbp
005A7553  56                              push rsi
005A7554  57                              push rdi
005A7555  48 8D 6C 24 F0                  lea rbp, [rsp - 0x10]
005A755A  48 81 EC 10 01 00 00            sub rsp, 0x110
005A7561  48 8B 05 D8 31 86 00            mov rax, qword ptr [rip + 0x8631d8]
005A7568  48 33 C4                        xor rax, rsp
005A756B  48 89 45 00                     mov qword ptr [rbp], rax
005A756F  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
005A7573  48 8D 45 48                     lea rax, [rbp + 0x48]
005A7577  4C 8B 95 90 00 00 00            mov r10, qword ptr [rbp + 0x90]
005A757E  33 DB                           xor ebx, ebx
005A7580  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005A7585  48 83 C9 FF                     or rcx, 0xffffffffffffffff
005A7589  48 C7 44 24 48 04 00 00 00      mov qword ptr [rsp + 0x48], 4
005A7592  48 8D 45 50                     lea rax, [rbp + 0x50]
005A7596  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005A759B  4C 8B DA                        mov r11, rdx
005A759E  48 8B 95 80 00 00 00            mov rdx, qword ptr [rbp + 0x80]
005A75A5  44 8D 4B 0A                     lea r9d, [rbx + 0xa]
005A75A9  48 C7 44 24 58 04 00 00 00      mov qword ptr [rsp + 0x58], 4
005A75B2  4D 85 C0                        test r8, r8
005A75B5  74 16                           je 0x1405a75cd
005A75B7  48 8B C1                        mov rax, rcx
005A75BA  48 FF C0                        inc rax
005A75BD  66 41 39 1C 40                  cmp word ptr [r8 + rax*2], bx
005A75C2  75 F6                           jne 0x1405a75ba
005A75C4  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
005A75CB  EB 03                           jmp 0x1405a75d0
005A75CD  41 8B C1                        mov eax, r9d
005A75D0  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
005A75D4  48 8D 35 A5 3A 12 00            lea rsi, [rip + 0x123aa5]
005A75DB  48 8D 45 60                     lea rax, [rbp + 0x60]
005A75DF  89 5C 24 6C                     mov dword ptr [rsp + 0x6c], ebx
005A75E3  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
005A75E8  4D 85 C0                        test r8, r8
005A75EB  48 8D 45 68                     lea rax, [rbp + 0x68]
005A75EF  48 C7 44 24 78 04 00 00 00      mov qword ptr [rsp + 0x78], 4
005A75F8  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
005A75FC  4C 0F 44 C6                     cmove r8, rsi
005A7600  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
005A7604  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
005A7608  48 8D 45 78                     lea rax, [rbp + 0x78]
005A760C  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
005A7610  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
005A7615  48 C7 45 88 04 00 00 00         mov qword ptr [rbp - 0x78], 4
005A761D  48 C7 45 98 10 00 00 00         mov qword ptr [rbp - 0x68], 0x10
005A7625  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
005A762D  48 85 D2                        test rdx, rdx
005A7630  74 15                           je 0x1405a7647
005A7632  48 8B C1                        mov rax, rcx
005A7635  48 FF C0                        inc rax
005A7638  66 39 1C 42                     cmp word ptr [rdx + rax*2], bx
005A763C  75 F7                           jne 0x1405a7635
005A763E  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
005A7645  EB 03                           jmp 0x1405a764a
005A7647  41 8B C1                        mov eax, r9d
005A764A  48 85 D2                        test rdx, rdx
005A764D  89 45 B8                        mov dword ptr [rbp - 0x48], eax
005A7650  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
005A7657  48 0F 44 D6                     cmove rdx, rsi
005A765B  89 5D BC                        mov dword ptr [rbp - 0x44], ebx
005A765E  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
005A7662  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
005A7666  48 C7 45 C8 10 00 00 00         mov qword ptr [rbp - 0x38], 0x10
005A766E  4D 85 D2                        test r10, r10
005A7671  74 15                           je 0x1405a7688
005A7673  48 FF C1                        inc rcx
005A7676  66 41 39 1C 4A                  cmp word ptr [r10 + rcx*2], bx
005A767B  75 F6                           jne 0x1405a7673
005A767D  44 8D 0C 4D 02 00 00 00         lea r9d, [rcx*2 + 2]
005A7685  4D 85 D2                        test r10, r10
005A7688  4C 0F 44 D6                     cmove r10, rsi
005A768C  44 89 4D D8                     mov dword ptr [rbp - 0x28], r9d
005A7690  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
005A7697  4C 89 55 D0                     mov qword ptr [rbp - 0x30], r10
005A769B  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
005A769F  48 8D 0D FA F6 85 00            lea rcx, [rip + 0x85f6fa]
005A76A6  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
005A76AD  89 5D DC                        mov dword ptr [rbp - 0x24], ebx
005A76B0  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
005A76B4  41 B9 0D 00 00 00               mov r9d, 0xd
005A76BA  48 8D 44 24 30                  lea rax, [rsp + 0x30]
005A76BF  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
005A76C7  45 33 C0                        xor r8d, r8d
005A76CA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005A76CF  49 8B D3                        mov rdx, r11
005A76D2  48 C7 45 F8 08 00 00 00         mov qword ptr [rbp - 8], 8
005A76DA  E8 E9 D8 E7 FF                  call 0x140424fc8
005A76DF  48 8B 4D 00                     mov rcx, qword ptr [rbp]
005A76E3  48 33 CC                        xor rcx, rsp
005A76E6  E8 55 4F 10 00                  call 0x1406ac640
005A76EB  48 8B 9C 24 30 01 00 00         mov rbx, qword ptr [rsp + 0x130]
005A76F3  48 81 C4 10 01 00 00            add rsp, 0x110
005A76FA  5F                              pop rdi
005A76FB  5E                              pop rsi
005A76FC  5D                              pop rbp
005A76FD  C3                              ret
005A76FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall McTemplateK0qqzqqjqzjztx_EtwWriteTransfer(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 8794584)) ^ (v_rsp);
    v_stack_m28 = result;
    v_rbx = 0;
    v_stack_mE8 = v_stack_p20;
    a1 = (a1) | (-1);
    v_stack_mE0 = 4;
    v_stack_mD8 = a5;
    v_stack_mD0 = 4;
    if (a6 == 0) goto loc_005A75CD;
loc_005A75BA:
    result = (a1) + 1;
    if ((*(unsigned __int16 *)(a6 + result * 2)) != 0) goto loc_005A75BA;
    goto loc_005A75D0;
loc_005A75CD:
loc_005A75D0:
    v_stack_mC0 = (unsigned int)((unsigned int)((unsigned int)(v_rbx + 10)));
    v_stack_mBC = 0;
    v_stack_mB8 = a7;
    v_stack_mB0 = 4;
    v_stack_mA8 = a8;
    if (a6 == 0) { a6 = v_rip + 1194661; }
    v_stack_m98 = a9;
    v_stack_m88 = a10;
    v_stack_mC8 = a6;
    v_stack_mA0 = 4;
    v_stack_m90 = 16;
    v_stack_m80 = 4;
    if (a11 == 0) goto loc_005A7647;
loc_005A7635:
    result = (a1) + 1;
    if ((*(unsigned __int16 *)(a11 + result * 2)) != 0) goto loc_005A7635;
    goto loc_005A764A;
loc_005A7647:
loc_005A764A:
    v_stack_m70 = (unsigned int)((unsigned int)((unsigned int)(v_rbx + 10)));
    if (a11 == 0) { a11 = v_rip + 1194661; }
    v_stack_m6C = 0;
    v_stack_m78 = a11;
    v_stack_m68 = a12;
    v_stack_m60 = 16;
    if (a13 == 0) goto loc_005A7688;
loc_005A7673:
    a1 = (a1) + 1;
    if ((*(unsigned __int16 *)(a13 + a1 * 2)) != 0) goto loc_005A7673;
loc_005A7688:
    if (a13 == 0) { a13 = v_rip + 1194661; }
    v_stack_m50 = (unsigned int)(a1 * 2 + 2);
    v_stack_m58 = a13;
    v_stack_m48 = a14;
    v_stack_m4C = 0;
    v_stack_m38 = a15;
    v_stack_m40 = 4;
    a3 = 0;
    v_stack_m108 = v_stack_mF8;
    v_stack_m30 = 8;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 8779514, a2, a3, 13);
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 13);
    v_rsp = (v_rsp) + (272);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t McTemplateK0qqzqqjqzjztx_EtwWriteTransfer(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, int64_t Arg14, int64_t Arg15)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x8631D8)) ^ (local_rsp);
    v_stack_m28 = result;
    local_rbx = 0;
    v_stack_mE8 = v_stack_p20;
    Arg1 = (Arg1) | (-1);
    v_stack_mE0 = 4;
    v_stack_mD8 = Arg5;
    v_stack_mD0 = 4;
    if (Arg6 == 0) goto loc_005A75CD;
loc_005A75BA:
    result = (Arg1) + 1;
    if ((*(uint16_t *)(Arg6 + result * 2)) != 0) goto loc_005A75BA;
    goto loc_005A75D0;
loc_005A75CD:
loc_005A75D0:
    v_stack_mC0 = (uint32_t)((uint32_t)((uint32_t)(local_rbx + 10)));
    v_stack_mBC = 0;
    v_stack_mB8 = Arg7;
    v_stack_mB0 = 4;
    v_stack_mA8 = Arg8;
    if (Arg6 == 0) { Arg6 = v_rip + 1194661; }
    v_stack_m98 = Arg9;
    v_stack_m88 = Arg10;
    v_stack_mC8 = Arg6;
    v_stack_mA0 = 4;
    v_stack_m90 = 16;
    v_stack_m80 = 4;
    if (Arg11 == 0) goto loc_005A7647;
loc_005A7635:
    result = (Arg1) + 1;
    if ((*(uint16_t *)(Arg11 + result * 2)) != 0) goto loc_005A7635;
    goto loc_005A764A;
loc_005A7647:
loc_005A764A:
    v_stack_m70 = (uint32_t)((uint32_t)((uint32_t)(local_rbx + 10)));
    if (Arg11 == 0) { Arg11 = v_rip + 1194661; }
    v_stack_m6C = 0;
    v_stack_m78 = Arg11;
    v_stack_m68 = Arg12;
    v_stack_m60 = 16;
    if (Arg13 == 0) goto loc_005A7688;
loc_005A7673:
    Arg1 = (Arg1) + 1;
    if ((*(uint16_t *)(Arg13 + Arg1 * 2)) != 0) goto loc_005A7673;
loc_005A7688:
    if (Arg13 == 0) { Arg13 = v_rip + 1194661; }
    v_stack_m50 = (uint32_t)(Arg1 * 2 + 2);
    v_stack_m58 = Arg13;
    v_stack_m48 = Arg14;
    v_stack_m4C = 0;
    v_stack_m38 = Arg15;
    v_stack_m40 = 4;
    Arg3 = 0;
    v_stack_m108 = v_stack_mF8;
    v_stack_m30 = 8;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 8779514, Arg2, Arg3, 13);
    Arg1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, 13);
    local_rsp = (local_rsp) + (272);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005A7548&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005A7548[BB_005A7548]
  bb_005A75B7[BB_005A75B7]
  bb_005A75BA[BB_005A75BA]
  bb_005A75C4[BB_005A75C4]
  bb_005A75CD[BB_005A75CD]
  bb_005A75D0[BB_005A75D0]
  bb_005A7632[BB_005A7632]
  bb_005A7635[BB_005A7635]
  bb_005A763E[BB_005A763E]
  bb_005A7647[BB_005A7647]
  bb_005A764A[BB_005A764A]
  bb_005A7673[BB_005A7673]
  bb_005A767D[BB_005A767D]
  bb_005A7688[BB_005A7688]
  bb_005A76FE[BB_005A76FE]
  bb_005A7548 -->|branch| bb_005A75CD
  bb_005A7548 -->|fallthrough| bb_005A75B7
  bb_005A75B7 -->|flow| bb_005A75BA
  bb_005A75BA -->|branch| bb_005A75BA
  bb_005A75BA -->|fallthrough| bb_005A75C4
  bb_005A75C4 -->|branch| bb_005A75D0
  bb_005A75CD -->|flow| bb_005A75D0
  bb_005A75D0 -->|branch| bb_005A7647
  bb_005A75D0 -->|fallthrough| bb_005A7632
  bb_005A7632 -->|flow| bb_005A7635
  bb_005A7635 -->|branch| bb_005A7635
  bb_005A7635 -->|fallthrough| bb_005A763E
  bb_005A763E -->|branch| bb_005A764A
  bb_005A7647 -->|flow| bb_005A764A
  bb_005A764A -->|branch| bb_005A7688
  bb_005A764A -->|fallthrough| bb_005A7673
  bb_005A7673 -->|branch| bb_005A7673
  bb_005A7673 -->|fallthrough| bb_005A767D
  bb_005A767D -->|flow| bb_005A7688
```
