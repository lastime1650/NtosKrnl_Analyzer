# VmpLogSparseSlatFill

- RVA: `0x0064DC38`–`0x0064DD5D` (길이 `293` bytes)
- VA: `0x000000014064DC38`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A68C4`
- 디코드: `64`개 명령, `293/293` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064DC75` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0064DD42` → [tlgWriteEx_EtwWriteEx](../4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x0064DD4E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [VmpFillSlat](../42/VmpFillSlat_function_0042A014.md) at `0x0042A0C9`

### Static image references
- `0x0064DC46` → RVA `0x00E0A740` (`.data`; read)
- `0x0064DC54` → RVA `0x00F02458` (`.data`; read)
- `0x0064DCEF` → RVA `0x000534B9` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064DC38  40 55                           push rbp
0064DC3A  48 8D 6C 24 B9                  lea rbp, [rsp - 0x47]
0064DC3F  48 81 EC 00 01 00 00            sub rsp, 0x100
0064DC46  48 8B 05 F3 CA 7B 00            mov rax, qword ptr [rip + 0x7bcaf3]
0064DC4D  48 33 C4                        xor rax, rsp
0064DC50  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0064DC54  4C 8B 15 FD 47 8B 00            mov r10, qword ptr [rip + 0x8b47fd]
0064DC5B  4C 8B DA                        mov r11, rdx
0064DC5E  66 44 89 45 87                  mov word ptr [rbp - 0x79], r8w
0064DC63  41 83 3A 05                     cmp dword ptr [r10], 5
0064DC67  0F 86 DA 00 00 00               jbe 0x14064dd47
0064DC6D  BA 01 00 00 00                  mov edx, 1
0064DC72  49 8B CA                        mov rcx, r10
0064DC75  E8 26 0E DE FF                  call 0x14042eaa0
0064DC7A  33 D2                           xor edx, edx
0064DC7C  84 C0                           test al, al
0064DC7E  0F 84 C3 00 00 00               je 0x14064dd47
0064DC84  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0064DC8D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0064DC94  8B 81 D0 01 00 00               mov eax, dword ptr [rcx + 0x1d0]
0064DC9A  49 8B CA                        mov rcx, r10
0064DC9D  89 45 8B                        mov dword ptr [rbp - 0x75], eax
0064DCA0  48 8D 45 8B                     lea rax, [rbp - 0x75]
0064DCA4  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0064DCA8  48 8D 45 8F                     lea rax, [rbp - 0x71]
0064DCAC  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0064DCB0  48 8D 45 87                     lea rax, [rbp - 0x79]
0064DCB4  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0064DCB8  41 0F B7 C0                     movzx eax, r8w
0064DCBC  C1 E0 04                        shl eax, 4
0064DCBF  89 45 FF                        mov dword ptr [rbp - 1], eax
0064DCC2  48 8D 45 93                     lea rax, [rbp - 0x6d]
0064DCC6  48 89 45 07                     mov qword ptr [rbp + 7], rax
0064DCCA  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0064DCCE  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
0064DCD2  48 8D 45 9F                     lea rax, [rbp - 0x61]
0064DCD6  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0064DCDA  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
0064DCDD  89 45 97                        mov dword ptr [rbp - 0x69], eax
0064DCE0  48 8D 45 97                     lea rax, [rbp - 0x69]
0064DCE4  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0064DCE8  48 8D 45 A7                     lea rax, [rbp - 0x59]
0064DCEC  89 55 03                        mov dword ptr [rbp + 3], edx
0064DCEF  48 8D 15 C3 57 A0 FF            lea rdx, [rip - 0x5fa83d]
0064DCF6  44 89 4D 93                     mov dword ptr [rbp - 0x6d], r9d
0064DCFA  45 33 C9                        xor r9d, r9d
0064DCFD  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0064DD02  C7 44 24 30 09 00 00 00         mov dword ptr [rsp + 0x30], 9
0064DD0A  48 C7 45 CF 04 00 00 00         mov qword ptr [rbp - 0x31], 4
0064DD12  44 89 45 8F                     mov dword ptr [rbp - 0x71], r8d
0064DD16  48 C7 45 DF 04 00 00 00         mov qword ptr [rbp - 0x21], 4
0064DD1E  48 C7 45 EF 02 00 00 00         mov qword ptr [rbp - 0x11], 2
0064DD26  4C 89 5D F7                     mov qword ptr [rbp - 9], r11
0064DD2A  48 C7 45 0F 04 00 00 00         mov qword ptr [rbp + 0xf], 4
0064DD32  48 C7 45 1F 08 00 00 00         mov qword ptr [rbp + 0x1f], 8
0064DD3A  48 C7 45 2F 04 00 00 00         mov qword ptr [rbp + 0x2f], 4
0064DD42  E8 01 C6 E5 FF                  call 0x1404aa348
0064DD47  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
0064DD4B  48 33 CC                        xor rcx, rsp
0064DD4E  E8 ED E8 05 00                  call 0x1406ac640
0064DD53  48 81 C4 00 01 00 00            add rsp, 0x100
0064DD5A  5D                              pop rbp
0064DD5B  C3                              ret
0064DD5C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpLogSparseSlatFill(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, unsigned int a6)
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
    unsigned int v_stack_m4C;
    unsigned __int64 v_stack_m4F;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mBC;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int16 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;

    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 8112883)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_mC8 = (unsigned __int16)(a3);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9127933))) <= 5) goto loc_0064DD47;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 9127933), 1, a3, a4);
    a2 = 0;
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(result + 184);
        result = *(unsigned int *)(a1 + 464);
        a1 = *(unsigned __int64 *)(v_rip + 9127933);
        v_stack_mC4 = (unsigned int)(result);
        result = v_stack_mC4;
        v_stack_m88 = result;
        result = v_stack_mC0;
        v_stack_m78 = result;
        result = v_stack_mC8;
        v_stack_m68 = result;
        result = (unsigned __int16)(a3);
        result = (unsigned int)((result) << (4));
        v_stack_m50 = (unsigned int)(result);
        result = v_stack_mBC;
        v_stack_m48 = result;
        result = a5;
        v_stack_mB0 = result;
        result = v_stack_mB0;
        v_stack_m38 = result;
        result = a6;
        v_stack_mB8 = (unsigned int)(result);
        result = v_stack_mB8;
        v_stack_m28 = result;
        result = v_stack_mA8;
        v_stack_m4C = 0;
        a2 = v_rip - 6268989;
        v_stack_mBC = a4;
        a4 = 0;
        v_stack_mD0 = result;
        v_stack_mD8 = 9;
        v_stack_m80 = 4;
        v_stack_mC0 = a3;
        v_stack_m70 = 4;
        v_stack_m60 = 2;
        v_stack_m58 = a2;
        v_stack_m40 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteEx_EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (256);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VmpLogSparseSlatFill(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6)
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
    uint32_t v_stack_m4C;
    uint64_t v_stack_m4F;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mBC;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint16_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;

    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x7BCAF3)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_mC8 = (uint16_t)(Arg3);
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8B47FD))) <= 5) goto loc_0064DD47;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x8B47FD), 1, Arg3, Arg4);
    Arg2 = 0;
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(result + 0xB8);
        result = *(uint32_t *)(Arg1 + 0x1D0);
        Arg1 = *(uint64_t *)(v_rip + 0x8B47FD);
        v_stack_mC4 = (uint32_t)(result);
        result = v_stack_mC4;
        v_stack_m88 = result;
        result = v_stack_mC0;
        v_stack_m78 = result;
        result = v_stack_mC8;
        v_stack_m68 = result;
        result = (uint16_t)(Arg3);
        result = (uint32_t)((result) << (4));
        v_stack_m50 = (uint32_t)(result);
        result = v_stack_mBC;
        v_stack_m48 = result;
        result = Arg5;
        v_stack_mB0 = result;
        result = v_stack_mB0;
        v_stack_m38 = result;
        result = Arg6;
        v_stack_mB8 = (uint32_t)(result);
        result = v_stack_mB8;
        v_stack_m28 = result;
        result = v_stack_mA8;
        v_stack_m4C = 0;
        Arg2 = v_rip - 6268989;
        v_stack_mBC = Arg4;
        Arg4 = 0;
        v_stack_mD0 = result;
        v_stack_mD8 = 9;
        v_stack_m80 = 4;
        v_stack_mC0 = Arg3;
        v_stack_m70 = 4;
        v_stack_m60 = 2;
        v_stack_m58 = Arg2;
        v_stack_m40 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (256);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064DC38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064DC38[BB_0064DC38]
  bb_0064DC6D[BB_0064DC6D]
  bb_0064DC84[BB_0064DC84]
  bb_0064DD47[BB_0064DD47]
  bb_0064DD5C[BB_0064DD5C]
  bb_0064DC38 -->|branch| bb_0064DD47
  bb_0064DC38 -->|fallthrough| bb_0064DC6D
  bb_0064DC6D -->|branch| bb_0064DD47
  bb_0064DC6D -->|fallthrough| bb_0064DC84
  bb_0064DC84 -->|flow| bb_0064DD47
```
